#faça um programa que leia um velor de 10 numeros reais e modtre-os na ordem inversa.

listaNumerosReais = []
print ('Informe os 10 numeros reais')
for i in range(10):
 	listaNumerosReais.append(float(input('Numero '+ str(i+1) + ':\n')))
listaNumerosReais.reverse()
print (listaNumerosReais)