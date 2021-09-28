import random

quadratica=[]
l=int(input("linhas da matriz"))


for a in range(l):
	linha=[random.randint(0,10)]*l
	quadratica.append(linha)


soma=0

for i in range(l):

	soma = soma+quadratica[i][i]
			

	print(quadratica[i])
print(soma)