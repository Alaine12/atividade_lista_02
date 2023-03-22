#Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20
#elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outras
#listas.

lista1 = []
lista2 = []
listaInter = []

for i in range(10):
 print ('lista 1: ')
lista1.append(input('Elemento: ' + str(i+1) + '\n'))

for j in range(10):
 print ('lista 2: ')
lista2.append(input('Elemento: ' + str(i+1) + '\n'))

for m in range(10):
 listaInter.append(lista1[m])
listaInter.append(lista2[m])


print (lista1)
print (lista2)
print (listaInter)
