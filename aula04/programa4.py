n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1>n2 and n1>n3:
	if n2>n3:
		print(n3,n2,n1)
	else:
		print(n2,n3,n1)
elif n2>n1 and n2>n3:
	if n1>n3:
		print(n3,n1,n2)
	else:
		print(n1,n3,n2)
else: 
	if n1>n2:	
		print(n2,n1,n3)
	else:
		print(n1,n2,n3)
