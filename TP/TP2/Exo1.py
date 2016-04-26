#Somme des entiers impaires inferieurs a N
n=int(input('Entrez un entier n : '))
#initialisation de s et de i
s=0
i=1
for i in range(1,n):
    if i%2!=0:
        s=s+i
print('la somme s=',s)
input()
