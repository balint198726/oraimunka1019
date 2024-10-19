import math
def negy():
# 1.	feladat: Proth-számok
# A számelmélet területén a François Proth matematikusról elnevezett Proth-számok a következő alakban felírható egész számok:
# ahol k pozitív egész páratlan szám és n pozitív egész, amire    Ha a feltételek nem teljesülnek térjen vissza hibaüzenettel: „HIBA: Nem megfelelő számok!”
# Írd ki a sorozat első 10 elemét vesszővel elválasztva egy sorba, hogy az utolsó után ne legyen vessző! (Az első néhány Proth-szám:  3, 5, 9, 13, 17, 25, 33, 41, 49, 57, 65, 81, 97, 113, 129, 145, 161, 177, 193, 209, 225, 241, etc.)
# pl1.:Kimenet: Proth-számok:  3, 5, 9, 13, 17, 25, 33, 41, 49, 57
    n = 1
    k =1

    if (k%2 ==1) and (n > 0) and (n>0) and (math.pow(2,n)>k):
        # jó eset
        print("Proth-számok: ", end=" ")
        for n in range(0,10,1):
            proth = (k * math.pow(2,n))+1
            print(str(proth)+", ", end="")
        proth = (k * math.pow(2,10))+1
        print(proth)
    else:
        print("HIBA: nem megfelelő számok")

def negyb():
    print("Proth-számok: ", end="")
    n = 1
    k = 1
    szamlalo = 0
    while szamlalo < 10:
        if (k>0) and (k % 2 == 1) and (n > 0) and (2**n>k):
            szamlalo += 1
            proth = (k * math.pow(2, n)) + 1
            print(str(proth) + ", ", end="")
        else:
            print("HIBA: nem megfelelő számok")
    n += 1
    proth = (k * math.pow(2, 10)) + 1
    print(proth)
