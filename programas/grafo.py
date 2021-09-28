totalvertice=[]
adcvertice=1
vertice=1
while adcvertice!=0:
	v=input('Digite o %d° vértice:'%vertice)
	totalvertice.append(v)
	adcvertice=int(input('Deseja adicionar mais vértices? Sim:1 Não:0'))
	print(totalvertice)
	vertice+=1
print(totalvertice)