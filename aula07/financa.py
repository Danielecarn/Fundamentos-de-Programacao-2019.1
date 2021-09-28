v=float(input("Insira o valor total para viagem: "))
valorinicial=float(input("Insira o valor do dépósito inicial: "))
mensal=float(input("Insira o valor da quantia que será depositada mensalmente: "))
rendimento=0.5/100

cont=0

while valorinicial<v:
	valorinicial=valorinicial+(rendimento*valorinicial)
	valorinicial+=mensal
	cont =cont+1	

print("Você já tem money suficiente!",
"\nNúmero de meses pra juntar dinheiro suficiente",
cont,"\nValor final depois desses meses %.2f"%valorinicial)
