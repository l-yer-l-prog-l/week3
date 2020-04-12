n1 = float(input())
n2 = float(input())
n3 = float(input())
if n1 == n2 == n3:
    import math
    B = math.sqrt(3)
    C = n1 ** 2
    A = B * C
    result = A / 4
    print(result)
else:
    import math
    p = n1 + n2 + n3
    pdel = p / 2
    p1 = pdel - n1
    p2 = pdel - n2
    p3 = pdel - n3
    per = p1 * p2 * p3
    sqrt = math.sqrt(pdel * per)
    print(sqrt)
