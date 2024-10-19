def beolvas(szoveg):
    szam = int(input(szoveg))
    return szam
def harom():
    a1 = beolvas("Kérem adja meg a számtani sorozat első elemét:")
    n = beolvas("Kérem adja meg a számtani sorozat elemszámát: ")
    d = beolvas("Kérem adja meg a számtani sorozat differenciáját: ")

    an = a1 + (n-1)*d
    sn = ((a1+an)*n)/2

    print(" a1="+str(a1)+" n="+str(n)+" d="+str(d)+" Sn="+str(int(sn)))
    if d > 0:
        print("A számtani sorozat monoton növekvő, és alulról korlátos.")
    elif d<0:
        print("A számtani sorozat monoton csökkenő, és felülről korlátos")
    else:
        print("A számtani sorozat nemnövekvő, nemcsökkenő, azaz állandó")
