#Entier cubique
print('les entiers cubiques entre 100 et 1000 sont : ')
for i in range(100,1000):
    c=i//100
    d=i%100//10
    u=i%10
    if c**3+d**3+u**3==i:
        print(i)
input()
