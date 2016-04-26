#Sigma i de 1 a n (Sigma j de 1 a i) de i+j
n=int(input('entrez n : '))
s=0
for i in range(2,n+1): #quand i=1 sigma j de 1 à 1 de i+j =0
    for j in range(1,i+1):
        s=s+i+j
print('la somme est s=',s,sep="")
input()
