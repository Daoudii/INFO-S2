#max et sa position d'une suite d'entiers qui se termine par 0
a=int(input('entrez le nombre a1 : \n'))
max=a
pos=1
i=2
while a!=0:
    print('entrez le nombre a',i,' : ',sep="",end="")
    #le parametre end pour personnaliser l'action apres la fonction print (retour a la ligne est le parametre par defaut)
    #le parametre sep pour personnaliser le caractere entre les parametre de print (espace est le parametre par defaut)
    a=int(input('\n'))
    if a>max:
        max=a
        pos=i
    i=i+1
print()
print('le max est :', max)
print('la position est :', pos)
input()
