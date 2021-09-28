import math
def encontrarnotas(notas):
	arq=open(notas,'r')
	for linha in arq.readlines():
		lista=linha.strip().split('\t')
		print(lista)
		del(lista[0])
		print(lista)
		#aux_lista=[]
		for i in range(len(lista)):
			lista[i]=int(lista[i])
			#aux_lista.append(int(lista[i]))
		'''for i in range(len(lista)):
			mini=min(int(lista))
			maxi=max(int(lista))'''
		print('Máximo: ',max(lista),'Minimo: ',min(lista))
			#soma+=int(lista[i])
		#print('média: %.2f'%(soma/len(lista))),

		

encontrarnotas('nomenota.txt')
#print('media',media)