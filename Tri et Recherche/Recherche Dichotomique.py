###     ##    ########    ########
##### ####    ###         ###
### ## ###    ########    ########
###    ###    ###         ###
###    ###    ########    ########
##################################
#Recherche Dichotomique
from tableau import remplissage
n=int(input('entrez le nbr de cases : '))
t=remplissage(n)
t.sort()
print(t)
x=int(input('entrez x a chercher : '))
inf=0
sup=n-1
m=(inf+sup)//2
while t[m]!=x and inf<=sup:
    if t[m]>x:
        sup=m-1
    else:
        inf=m+1
    m=(inf+sup)//2
if t[m]==x:
    print('trouvé a',m)
else:
    print('pas trouvé')
input()
