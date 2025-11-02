from datetime import datetime

class Rainfall:
    def __init__(self, name, time_be, time_en, rain):
        self.name = name
        self.time_be = time_be
        self.time_en = time_en
        self.rain = rain

    @staticmethod
    def hieu_gio(t1, t2):
        fmt = "%H:%M"
        a = datetime.strptime(t1.strip(), fmt)
        b = datetime.strptime(t2.strip(), fmt)
        if b < a:
            b = b.replace(day=b.day + 1)
        return (b - a).total_seconds() / 3600

    def tinh_tb(self):
        return self.rain / self.hieu_gio(self.time_be, self.time_en)

def solve():
    test_cases = int(input())
    st = {}
    rf = {}
    idx = []
    for cases in range(test_cases):
        place = input().strip()
        t1 = input().strip()
        t2 = input().strip()
        rain = float(input())
        if place not in st:
            st[place] = 0
            rf[place] = 0
            idx.append(place)
        st[place] += Rainfall.hieu_gio(t1, t2)
        rf[place] += rain
    res = 1
    for name in idx:
        tb = rf[name] / st[name] if st[name] != 0 else 0
        print(f"T0{res} {name} {tb:.2f}")
        res += 1

solve()
