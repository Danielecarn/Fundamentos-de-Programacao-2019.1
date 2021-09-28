n=int(input("Digite um número inteiro positivo:"))
if n==0:
	print("Fatorial de:",n,"é",1)
else:
	while n<0:
		n=int(input("Negativos Não!\nDigite um número inteiro positivo:"))
	fatorial=1
	for i in range(n):
		fatorial=n*fatorial
		n=n-1
	print("Fatorial de:",i+1,"é",fatorial)