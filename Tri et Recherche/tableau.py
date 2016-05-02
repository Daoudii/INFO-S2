###     ##    ########    ########
##### ####    ###         ###
### ## ###    ########    ########
###    ###    ###         ###
###    ###    ########    ########
##################################
#Fonction et procedures pour les tableaux
def remplissage(n):
    "remplissage d'un tableau"
    t=[0]*(n) #Initialisation du tableau
    for i in range(0,n): #boucle de remplissage
        print('entrez le nombre n°',i,sep="")
        t[i]=int(input(''))
    return t
