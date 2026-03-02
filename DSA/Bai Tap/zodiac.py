test_case = int(input())
for t in range(test_case):
    day,month = map(int,input().split())
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        print("Bao Binh")
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        print("Song Ngu")
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        print("Bach Duong")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        print("Kim Nguu")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        print("Song Tu")
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        print("Cu Giai")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        print("Su Tu")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        print("Xu Nu")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        print("Thien Binh")
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        print("Bo Cap")
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        print("Nhan Ma")
    else:
        print("Ma Ket")