import random

szam = random.randint(-5, 5)
print(szam)


if szam > 0:
    print("poz")
if szam % 2 == 0:
    print("pár")
if szam == 2 or szam == 3 or szam == 5:     
    print("prím")