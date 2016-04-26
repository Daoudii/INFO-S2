#Triangle
#1
#12
#123
#123
#1234
#12345
#123456
n=int(input('entrez n : '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")#le parametre end pour personnaliser l'action apres la fonction print (retour a la ligne est le parametre par defaut)
    print()
input()
