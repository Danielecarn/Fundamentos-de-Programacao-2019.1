n1 =float(input("Digite a primeira nota: "))
n2 =float(input("Digite a segunda nota: "))

m=(n1+n2)/2

if m>=7:
	print("Aprovado, média: ",m)
elif m>=4 and m<7:
	af =float(input("Digite a nota da Avaliação Final: "))
	m2= (af+m)/2
	if m2>=5:
		print("Aprovado, média: ",m2)
	else: 
		print("Reprovado, média:",m2)
else:
	print("Reprovado, média: ",m)


