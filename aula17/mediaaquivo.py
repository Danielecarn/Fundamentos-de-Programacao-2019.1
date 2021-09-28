arquivo = open("notas.txt","r")

soma=0
media=0

for i in arquivo.readlines():
	soma+=i

media=soma/len(arquivo.readlines())

print(media)