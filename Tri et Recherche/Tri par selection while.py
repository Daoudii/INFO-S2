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
j=0
while j<n-1:
    min=j
    i=j+1
    while i<n:
        if t[i]<t[min]:
            min=i
        i=i+1
    c=t[j]
    t[j]=t[min]
    t[min]=c
    j=j+1
print(t)
input()
