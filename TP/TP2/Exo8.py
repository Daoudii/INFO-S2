#Somme des chiffres d'un entier
n=int(input('entrez n : '))
s=0
while n//10!=0:
    s=s+n%10
    n=n//10
s=s+n
print("s=",s,sep="")    
input()
