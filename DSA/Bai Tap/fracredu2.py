import math
a, b, c, d = map(int, input().split())
P_num = a/math.gcd(a, b)
P_den = b/math.gcd(a, b)
Q_num = c/math.gcd(c, d)
Q_den = d/math.gcd(c, d)
R_num = P_num * Q_den + Q_num * P_den
R_den = P_den * Q_den
R_gcd = math.gcd(int(R_num), int(R_den))
R_num //= R_gcd
R_den //= R_gcd
print(f"{int(R_num)}/{int(R_den)}")