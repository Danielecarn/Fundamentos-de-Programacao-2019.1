def criar_matriz(matriz):
	arq=open(matriz,'r')
	matriz=[]
	for linha in arq.readlines():
		lista=linha.strip().split('\t')
		matriz.append(lista)
	return(matriz)

def multmatriz(a,b,matriz):
	arq= open(matriz,'w')
	matrizc=[]
	
	for l in range(len(a)): #len da matriz a percorre as linhas
		matrizc.append([])
		for c in range(len(b[0])): #índice percorre as colunas
			total=0
			matrizc[l].append(0)
			for n in range(len(a[0])):
				total+= int(a[l][n])*int(b[n][c])
			print("total",total)
			matrizc[l][c] =total
	arq.write(str(matrizc))
	arq.close()
	return(matrizc)
	
		

matriz1=criar_matriz('a.txt')
print(matriz1)

matriz2=criar_matriz('b.txt')
print(matriz2)

matrizc=multmatriz(matriz1,matriz2,'c.txt')
print(matrizc)
