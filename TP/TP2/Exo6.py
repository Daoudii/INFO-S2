#Total de 15 en ajoutant 3 entiers
print('les possibilités d\'avoir un Total de 15 en ajoutant 2 entiers sont : ')
l=1
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i+j+k==15 and i<=j<=k: #la 2ieme condition pour eviter la redandance
                print('la possibilité',l,'est ',i,j,k)
                l=l+1
input()
