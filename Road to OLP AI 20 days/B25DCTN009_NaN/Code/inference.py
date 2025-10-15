# inference.py
import os, json, argparse
import pandas as pd
from PIL import Image

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, models

def build_resnet18_scratch(num_classes: int):
    m = models.resnet18(weights=None)
    m.fc = nn.Linear(m.fc.in_features, num_classes)
    return m

class TestSet(Dataset):
    def __init__(self, df, img_dir, tf):
        self.df = df.reset_index(drop=True)
        self.dir = img_dir
        self.tf = tf
    def __len__(self): return len(self.df)
    def __getitem__(self, i):
        name = self.df.iloc[i]['image']
        img = Image.open(os.path.join(self.dir, name)).convert('RGB')
        return self.tf(img), name

@torch.no_grad()
def main(args):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # mapping (tên lớp -> id số); cần id số để nộp
    class2id = json.load(open('class2id.json'))
    num_classes = len(class2id)

    # mean/std dùng cùng với train
    if os.path.exists('mean_std.json'):
        ms = json.load(open('mean_std.json'))
        mean, std = ms['mean'], ms['std']
    else:
        mean, std = [0.485,0.456,0.406], [0.229,0.224,0.225]

    tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])

    df_test = pd.read_csv(args.test_csv)
    dl = DataLoader(TestSet(df_test, args.img_dir, tf),
                    batch_size=args.batch, shuffle=False, num_workers=2)

    model = build_resnet18_scratch(num_classes).to(device)
    model.load_state_dict(torch.load(args.weights, map_location=device))
    model.eval()

    names, preds = [], []
    for xb, name in dl:
        xb = xb.to(device)
        out = model(xb)
        pred = out.argmax(1).cpu().numpy().tolist()
        names.extend(name); preds.extend(pred)

    # prediction.csv: image,label (label là id số)
    pd.DataFrame({"image": names, "label": preds}).to_csv(args.out, index=False)
    print(f"✅ saved {args.out} ({len(names)} rows)")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--img_dir", default="ALL_IMAGES")
    ap.add_argument("--test_csv", default="CUB/test.csv")
    ap.add_argument("--weights", default="weights.pth")
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--out", default="prediction.csv")
    args = ap.parse_args()
    main(args)
