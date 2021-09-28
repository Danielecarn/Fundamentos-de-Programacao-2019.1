import random

def escolherpalavra():
    arquivo = open("palavras.txt","r")
    matriz=[]
    for linha in arquivo.readlines():
        totalpalvras = linha.strip()
        matriz.append(totalpalvras)
    escolha = random.choice(matriz)
    print(matriz)
    return(escolha)

escolha = escolherpalavra() 

copia_escolha=list(escolha)
letras_chute=list('-'*len(escolha))

print(copia_escolha)
print(letras_chute)

num_tentativas=0

tentativas=[]


while num_tentativas<6 and escolha!="".join(letras_chute):
	print("".join(letras_chute))
	entrada=input("Insira uma letra: ")
	

	if entrada not in tentativas:
		tentativas.append(entrada)

		if copia_escolha.count(entrada)>0: #TEM A LETRA NA PALAVRA

			for i in range(copia_escolha.count(entrada)):			
				posicao=copia_escolha.index(entrada) #4
				char_posicao=copia_escolha[posicao]#e
				copia_escolha[posicao]='-'
				letras_chute[posicao]=char_posicao
		else:
			num_tentativas+=1
			print("Você perdeu uma tentativa! :(")

if num_tentativas <6:
	print("".join(letras_chute))
	print("Você ganhou um parabéns")
else:
	print("Perdedor")