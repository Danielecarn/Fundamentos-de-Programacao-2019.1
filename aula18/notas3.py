arquivo = open("notas3.txt","r")

dic={}
aprovados=[]
reprovados=[]

for i in arquivo.readlines():
	lista = i.split("\t")
	nome=lista[0].strip()
	nota=float(lista[1].strip())
	nota2=float(lista[2].strip())
	media =(nota+nota2)/2
	#print(i)
	dic[nome] = media
	if dic[nome]>=7:
		aprovados.append(nome)
	else:
		reprovados.append(nome)
#print(dic)
print(sorted(aprovados))
print(sorted(reprovados))

arquivo.close()