par = 0
primo = 0 
for i in range(0,10):
	n = int(input("Digite um número inteiro: "))
	e = 1
	count = 0


	if n == 2:
		par += n
		primo+= n
	elif n%2 ==0:
		par += n
	else:
		for i in range(n):
			e +=1
			if n%e ==0:
				count+=1
		if count<=1:
			primo+=n
print("Soma de pares: ",par,"Soma de primos: ",primo)