###     ##    ########    ########
##### ####    ###         ###
### ## ###    ########    ########
###    ###    ###         ###
###    ###    ########    ########
##################################
#Tri a bulles
from tableau import remplissage
n=int(input('entrez le nbr de cases : '))
t=remplissage(n)
d=0
while d==0:
    d=1
    for i in range(0,n-1):
        if t[i]>t[i+1]:
            c=t[i]
            t[i]=t[i+1]
            t[i+1]=c
            d=0
print(t)
input()
