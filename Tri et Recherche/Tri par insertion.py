###     ##    ########    ########
##### ####    ###         ###
### ## ###    ########    ########
###    ###    ###         ###
###    ###    ########    ########
##################################
#Tri par insertion
from tableau import remplissage
n=int(input('entrez le nbr de cases : '))
t=remplissage(n)
for j in range(1,n):
    i=j
#    while t[i]<t[i-1] and i>0:
#        c=t[i]
#        t[i]=t[i-1]
#        t[i-1]=c
#        i=i-1
    x=t[j]
    while i>0 and x<t[i-1]:
        t[i]=t[i-1]
        i=i-1
    t[i]=x
print(t)
input()
