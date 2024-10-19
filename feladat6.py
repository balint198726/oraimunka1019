def beolvas():
    oldal = float(input("Add meg a háromszög oldalát!"))
def hat():
    #6.	A program azt dönti el, hogy lehet-e háromszöget szerkezteni a felhasználótól beolvasott adatok alpján. akkor lehet hááromszöget szerkezsteni, ha: A háromszög bármely oldalának hossza kisebb a másik két oldal hosszának összegénél. Azaz: a<b+c és b<a+c és c<a+b és c<a+b. Ügyelj arra, hogy a,b,c értékei 0-nál nagyobbnak pozitív valós számnak kell lennie, ha ez nem teljesül, térj vissza hibaüzenettel: „HIBA: Nem megfelelő bemenő adatok!”!
    a = beolvas()
    b = beolvas()
    c = beolvas()

    if a>0 and b>0 and c>0:
        # jó
        if a<c+b and c<a+b and b<a+c:
            print("A háromszög megszerkeszthető")
        else:
            print("A háromszög nem megszerkeszthető")
    else:
        print("HIBA: A szám nem megfelelő")
