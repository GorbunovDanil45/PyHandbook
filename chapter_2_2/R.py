a, b, c = int(input()), int(input()), int(input())

hypot = max(a, b, c)
cath_1 = min(a, b, c)
cath_2 = (a + b + c) - hypot - cath_1

if cath_1 ** 2 + cath_2 ** 2 == hypot ** 2:
    print("100%")
elif cath_1 ** 2 + cath_2 ** 2 < hypot ** 2:
    print("велика")
else:
    print("крайне мала")
