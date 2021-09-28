cont=0
n=0
while True:
	i=int(input("Digite a idade:"))
	while i<0:
		i=int(input("Idade inválida\nDigite a idade:"))
	if i==0:
		break
	n+=i
	cont+=1
print("Média das idades:%.2f"%(n/cont))