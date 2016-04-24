#calculatrice de pascal (+,-,*,/)
a=float(input())
op=input()
b=float(input())
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    if b!=0:
        print(a/b)
    else:
        print('erreur')
input() #pour que le programme ne se ferme pas apres l'execution
#fin du programme
