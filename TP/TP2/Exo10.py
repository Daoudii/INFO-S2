#Sigma i de 1 a n de 1/fact(i)
n=int(input('entrez n : '))
s=1
fact=1
for i in range(1,n+1):
    fact=fact*i
    s=s+(1/fact)
print('s=',s,sep="")
input()
