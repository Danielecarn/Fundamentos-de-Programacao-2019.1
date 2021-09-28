import random 

lista=['banana','maca','laranja','joao','jé','sabiaguaba']
aux=[]
palavra=random.choice(lista)

for i in range(len(palavra)):
	aux.append(0)
	aux[i]=palavra[i]

print(palavra)
print(aux.sort())
while True:
	chute=input('Chute a palavra embaralhada: ')
	if chute==palavra:
		print('que cagado vc em, ',palavra)