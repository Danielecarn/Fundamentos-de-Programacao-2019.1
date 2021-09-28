at=int(input("Insira o ano atual: "))
totaldeanos = at - 2006
s=1000.00
p=1.5/100
s=s+(p*s)

for i in range(0,totaldeanos):
	p=2*p
	s=s+(p*s)

print("Salário Atual:%.2f"%s)
