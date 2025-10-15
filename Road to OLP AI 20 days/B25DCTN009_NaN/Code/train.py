import os, json, time, random, argparse
import numpy as np
import pandas as pd
from PIL import Image
from multiprocessing import cpu_count

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, models
from sklearn.model_model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from torch.amp import autocast, GradScaler
import torch.backends.cudnn as cudnn

def seed_all(s=42):
    random.seed(s); np.random.seed(s); torch.manual_seed(s)
    if torch.cuda.is_available(): torch.cuda.manual_seed_all(s)

class BirdDataset(Dataset):
    def __init__(self, df, img_dir, transform, class2id):
        self.df = df.reset_index(drop=True)
        self.dir = img_dir
        self.tf = transform
        self.class2id = class2id
    def __len__(self): return len(self.df)
    def __getitem__(self, i):
        row = self.df.iloc[i]
        img = Image.open(os.path.join(self.dir, row['image'])).convert('RGB')
        img = self.tf(img)
        y = self.class2id[row['label']]
        return img, y

def build_resnet18_scratch(num_classes: int):
    m = models.resnet18(weights=None)
    m.fc = nn.Linear(m.fc.in_features, num_classes)
    return m

def main(args):
    seed_all(42)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    cudnn.benchmark = (device == 'cuda')
    print("Device:", device)

    # CSV & mapping
    train_df = pd.read_csv(args.train_csv)
    labels_sorted = sorted(train_df['label'].unique())
    class2id = {c:i for i,c in enumerate(labels_sorted)}
    id2class = {i:c for c,i in class2id.items()}
    json.dump(class2id, open('class2id.json','w'), ensure_ascii=False)
    json.dump(id2class, open('id2class.json','w'), ensure_ascii=False)
    num_classes = len(labels_sorted)
    print("Số lớp:", num_classes)

    # mean/std
    if os.path.exists('mean_std.json'):
        ms = json.load(open('mean_std.json'))
        mean, std = ms['mean'], ms['std']
    else:
        mean, std = [0.485,0.456,0.406], [0.229,0.224,0.225]

    # transforms
    train_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ColorJitter(0.1,0.1,0.1,0.05),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])
    val_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])

    # split 80/20
    tr_idx, va_idx = train_test_split(train_df.index, test_size=0.2, random_state=42,
                                      stratify=train_df['label'])
    tr_df = train_df.loc[tr_idx].reset_index(drop=True)
    va_df = train_df.loc[va_idx].reset_index(drop=True)

    # dataloader
    WORKERS = min(4, cpu_count())
    PIN = (device == 'cuda')
    train_dl = DataLoader(BirdDataset(tr_df, args.img_dir, train_tf, class2id),
                          batch_size=args.batch, shuffle=True,
                          num_workers=WORKERS, pin_memory=PIN,
                          prefetch_factor=4 if WORKERS>0 else None,
                          persistent_workers=bool(WORKERS))
    val_dl = DataLoader(BirdDataset(va_df, args.img_dir, val_tf, class2id),
                        batch_size=args.batch, shuffle=False,
                        num_workers=WORKERS, pin_memory=PIN,
                        prefetch_factor=4 if WORKERS>0 else None,
                        persistent_workers=bool(WORKERS))

    # model / optim
    model = build_resnet18_scratch(num_classes).to(device)
    criterion = nn.CrossEntropyLoss(label_smoothing=0.05)
    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    scaler = GradScaler(enabled=(device=='cuda'))

    def train_one_epoch():
        model.train(); loss_sum = 0.0
        for xb, yb in train_dl:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad(set_to_none=True)
            with autocast(device_type='cuda', enabled=(device=='cuda')):
                logits = model(xb)
                loss = criterion(logits, yb)
            scaler.scale(loss).backward()
            scaler.step(optimizer); scaler.update()
            loss_sum += loss.item() * xb.size(0)
        return loss_sum / len(train_dl.dataset)

    @torch.no_grad()
    def evaluate():
        model.eval(); preds, gts = [], []
        for xb, yb in val_dl:
            xb = xb.to(device)
            logits = model(xb)
            p = logits.argmax(1).cpu().numpy()
            preds.extend(p); gts.extend(yb.numpy())
        return accuracy_score(gts, preds), f1_score(gts, preds, average='macro')

    best_acc, bad, patience = 0.0, 0, 3
    for ep in range(1, args.epochs+1):
        t0 = time.time()
        tr_loss = train_one_epoch()
        scheduler.step()
        val_acc, val_f1 = evaluate()
        print(f"Epoch {ep:02d} | train_loss={tr_loss:.4f} | val_acc={val_acc:.4f} | "
              f"val_f1={val_f1:.4f} | {time.time()-t0:.1f}s")
        if val_acc > best_acc:
            best_acc = val_acc; bad = 0
            torch.save(model.state_dict(), 'weights.pth')
        else:
            bad += 1
            if bad >= patience:
                print("Early stopping!"); break

    print("✅ saved weights.pth")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--img_dir", default="ALL_IMAGES")
    ap.add_argument("--train_csv", default="CUB/train.csv")
    ap.add_argument("--epochs", type=int, default=15)
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--lr", type=float, default=1e-3)
    args = ap.parse_args()
    main(args)
