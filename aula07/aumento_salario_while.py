at=int(input("Insira o ano atual: "))

s=1000.00
p=1.5/100
s=s+(p*s)
i=2007

while i<=at:
	p=2*p
	s=s+(p*s)
	i+=1

print("Salário Atual:%.2f"%s)
