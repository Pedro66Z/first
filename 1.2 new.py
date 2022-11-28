nevek = []
k = input("adj meg keresztnevet\t")
t = input("2 lehetőséged maradt\t")
l = input("1 lehetőséged maradt\t")


if k == str:
    print("")
if t == str:
    print("")
if l == str:
    print("")
    
if k != "":
        nevek.append(k)
if t != "":
        nevek.append(t)
if l != "":
        nevek.append(l)
        
print("nincs több lehetőséged!")
print("megadott nevek:",nevek)