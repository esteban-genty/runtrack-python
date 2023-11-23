i = 1
nb = int(input("Entrée un nombre entier :"))
if nb == 0:
    print ("Erreur")
else:
     while i<nb+1:
        print ("Table de multiplication de ",i," : ")
        e=1
        for e in range(11):
            print (e, " x ", i, " = ", e*i)
            e=e+1
        i=i+1