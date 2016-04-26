#Calcul du PGCD par l'algorithme d'Euclide
a=int(input('entrez a : '))
b=int(input('entrez b : '))
if b==0:
    if a==0:
        print('Erreur')
    else:
        print('PGCD=',a,sep="")
else:
    while b!=0:
        r=a%b
        a=b
        b=r
    print('PGCD=',a,sep="")
input()
