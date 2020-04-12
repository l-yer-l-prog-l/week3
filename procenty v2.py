procent = int(input())
rubli = int(input())
kopeiki = int(input())
rubl_v_kopeikah = rubli * 100
summa = rubl_v_kopeikah + kopeiki
one_procent = summa / 100
poditogsumma = one_procent * procent
itog = summa + poditogsumma
result1 = itog // 100
ost_kopeiki = itog - result1
if ost_kopeiki > 10:
    result2 = ost_kopeiki / 10
elif 1 < ost_kopeiki < 10:
    result2 = ost_kopeiki / 100
elif ost_kopeiki < 1:
    result2 = ost_kopeiki / 1000
print(result1, result2)