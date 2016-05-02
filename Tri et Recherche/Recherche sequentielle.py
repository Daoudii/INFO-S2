###     ##    ########    ########
##### ####    ###         ###
### ## ###    ########    ########
###    ###    ###         ###
###    ###    ########    ########
##################################
#Recherche sequentielle
from tableau import remplissage
n=int(input('entrez le nbr de cases : '))
t=remplissage(n)
x=float(input('entrez x a chercher : '))
i=0
while t[i]!=x and i<n-1:
    i=i+1
if t[i]==x:
    print('trouvé a', i)
else :
    print('pas trouvé')
input()
