import math
a = float(input())
b = float(input())
c = float(input())
bsquare = b ** 2
ac = a * c
ac4 = 4 * ac
D = bsquare - ac4
a2 = 2 * a
if D > 0:
    origin = math.sqrt(D)
    bplusD = -b + origin
    bminusD = -b - origin
    x1 = bplusD / a2
    x2 = bminusD / a2
    if x1 < x2:
        print("2", x1, x2)
    elif x1 > x2:
        print("2", x2, x1)
    elif x1 == x2:
        print("1", x1)
    else:
        print()
elif D == 0:
    print("1", -b / a2)
else:
    print()
