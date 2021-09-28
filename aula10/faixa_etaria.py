ate15=0
ate30=0
ate45=0
ate60=0
acima60=0

for i in range(0,8):
	n=int(input("Digite altas idades "))
	if n <=15:
		ate15+=1
	elif n>=16 and n<=30:
		ate30+=1
	elif n>=31 and n<=45:
		ate45+=1
	elif n>=46 and n<=60:
		ate60+=1
	elif n>60:
		acima60+=1
m=ate15*100
y=acima60*100
print("Quantidade de pessoas por faixa etária\n1-",ate15,
	"\n2-",ate30,"\n3-",ate45,"\n4-",ate60,"\n5-",acima60)
print("Porcentagem de pessoas da 1 faixa etária em relação ao total ",(m/8),"%")
print("Porcentagem de pessoas da 5 faixa etária em relação ao total ",(y/8),"%")