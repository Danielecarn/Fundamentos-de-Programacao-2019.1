l=int(input('Insira a qtd de linhas'))
c=int(input('Insira a qtd de colunas'))

matriz=[]

for i in range(l):
	matriz.append([])
	for j in range(c):
		matriz[i].append(0)
		m=int(input('Valor da posicao %d'))
		matriz[i][j]=m
print(matriz)