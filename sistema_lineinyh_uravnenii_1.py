a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
e1 = e - b
if a == 0:
	x = e1
elif e1 % a == 0:
    x = e1 / a
else:
    x = e1
f1 = f - d
if c == 0:
	y = f1
elif f1 % c == 0:
    y = f1 / c
else:
    y = f1
print(x, y)