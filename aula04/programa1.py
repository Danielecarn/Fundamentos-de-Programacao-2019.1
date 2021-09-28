tlp = 2
avp = 3
exfp = 5

tl= float(input("Digite a nota de Trabalho no Laboratório: "))
av = float(input("Digite a nota de Avaliação Semestral: "))
exf = float(input("Digite a nota do Exame Final: "))

m = ((tl*tlp)+(av*avp)+(exf*exfp))/10

print("Média Ponderada: ",m)

if m>=8 and m<=10:
	print("Conceito A")
elif m>=7:
	print("Conceito B")
elif m>=6:
	print("Conceito C")
elif m>=5:
	print("Conceito D")
elif m<5 and m>=0:
	print("Conceito E")