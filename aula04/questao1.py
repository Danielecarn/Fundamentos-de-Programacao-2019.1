for i in range(1,1001):
	cont=0
	for j in range(1,i):
		cont=0
		if i%j==0:
			cont+=1
	if cont<=2:
		if i%10 ==3 or i%10 ==7:
			print(i)