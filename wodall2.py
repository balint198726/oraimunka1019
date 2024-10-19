def wo():
    n = 1
    db = 0
    print("Wodall számok: ", end="")
    while db<10:
        if n>0:
            wn = n*pow(2,n)-1
            if db !=9:
                print(str(wn)+", ", end="")
            db +=1
        n +=1