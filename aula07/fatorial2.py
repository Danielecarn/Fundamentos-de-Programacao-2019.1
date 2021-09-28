while True:
	n=int(input("Digite um número inteiro positivo:"))
	a=n
	fatorial=1
	for i in range(a):
		fatorial=a*fatorial
		a=a-1
	if n<=0:
		print("FIM")
		break
	print("Fatorial de:",i+1,"é",fatorial)