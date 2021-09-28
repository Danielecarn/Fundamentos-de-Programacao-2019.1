import math
infinito = math.inf

grafo = [[0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]] #GRAFO FIXO
pai = []
distancia = []

#Entrada dos pesos das arestas existentes no grafos
grafo[0][1] = int(input("Digite o peso da aresta AB:"))
grafo[1][2] = int(input("Digite o peso da aresta BC:"))
grafo[1][3] = int(input("Digite o peso da aresta BD:"))
grafo[2][4] = int(input("Digite o peso da aresta CE:"))
grafo[3][4] = int(input("Digite o peso da aresta DE:"))


#Entrada do caminho a ser encontrado
caminho = input("Digite o caminho a ser calculado():")

#Teste para saber se o caminho existe ou não
loop = 0
while loop == 0:
	if caminho == 'AB' or caminho == 'AD' or caminho == 'AC' or caminho == 'AE' or caminho == 'BC' or caminho == 'BD' or caminho == 'BE' or caminho == 'CE' or caminho == 'DE' or caminho == 'ab' or caminho == 'ad' or caminho == 'ac' or caminho == 'ae' or caminho == 'bc' or caminho == 'bd' or caminho == 'be' or caminho == 'ce' or caminho == 'de':
		loop = 1
	else:
		caminho = input("Caminho inválido. Digite um novo caminho a ser calculado:")

#Dicionário para converter a entrada em índices da matriz(grafo)
dic = {"A":0,"B":1,"C":2,"D":3,"E":4,"a":0,"b":1,"c":2,"d":3,"e":4,}

#conversão da entrada em índices da matriz(grafo)
caminho = caminho.replace(str(caminho[0]), str(dic[caminho[0]]))
caminho = caminho.replace(str(caminho[1]), str(dic[caminho[1]]))

#INICIALIZA-CM-ÚNICA-FONTE
for i in range(0, 5): 
 	distancia.append(infinito) 
 	pai.append(None)
distancia[int(caminho[0])] = 0
 
#Algoritmo de BELL-FORD
for i in range(0, 4):
	for j in range(0, 5):
		for k in range(0, 5):
			if grafo[j][k] != 0:
				#Relaxamento das arestas
				if distancia[k] > distancia[j] + grafo[j][k]:
					distancia[k] = distancia[j] + grafo[j][k]
					pai[k] = j

#Construir o caminho para ser mostrado
lista = []
aux = int(caminho[1])
while aux != caminho[0]:
	lista.append(aux)
	aux = int(pai[int(aux)])
	if pai[int(aux)] == None:
		break
lista.append(int(aux))	
lista.reverse()

#Conversão dos índices da matriz para letras
for i in range(0, len(lista)):
	if lista[i] == 0:
		lista[i] = 'A'
	if lista[i] == 1:
		lista[i] = 'B'
	if lista[i] == 2:
		lista[i] = 'C'
	if lista[i] == 3:
		lista[i] = 'D'
	if lista[i] == 4:
		lista[i] = 'E'

print("Caminho desejado: ",lista)