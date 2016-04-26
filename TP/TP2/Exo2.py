#max et sa position de 20 entiers
max=int(input('entrez le nombre a1 : \n'))
pos=1
for i in range(2,21):
    print('entrez le nombre a',i,' : ',sep="",end="")
    a=int(input('\n'))
    if a>max:
        max=a
        pos=i
print()
print('le max est :',max)
print('la position est :', pos)
input()
