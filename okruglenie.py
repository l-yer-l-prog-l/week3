import math
N = float(input())
flr = math.floor(N)
num = N - flr
if num == 0.5:
    c = math.ceil(N)
    print(c)
if num < 0.5:
    a = math.floor(N)
    print(a)
if num > 0.5:
    b = math.ceil(N)
    print(b)
