#Nieme terme de la suite de Fibonacci
n=int(input('entrez n : '))
f0=0
f1=1
if n==0:
    f=f0
elif n==1:
    f=f1
else:
    for i in range(2,n+1):
        f=f0+f1
        f0=f1
        f1=f
print('fn=',f,sep="")
input()
