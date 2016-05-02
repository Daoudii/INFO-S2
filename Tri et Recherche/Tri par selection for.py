###     ##    ########    ########
##### ####    ###         ###
### ## ###    ########    ########
###    ###    ###         ###
###    ###    ########    ########
##################################
#Tri par selection for
from tableau import remplissage
n=int(input('entrez le nbr de cases : '))
t=remplissage(n)
for j in range(0,n-1):
    min=j
    for i in range(j+1,n):
        if t[i]<t[min]:
            min=i
    c=t[j]
    t[j]=t[min]
    t[min]=c
print(t)
input()
