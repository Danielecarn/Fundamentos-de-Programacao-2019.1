a=[]

l=int(input("ordem da matriz"))

for n in range(l):
	linha=[0]*l
	a.append(linha)

for i in range(l):
	for j in range(l):
		a[i][j]=int(input("Entre com o valor da linha  e da coluna "))

v=[]

for b in range(l):
	m =int(input("Valores do vetor"))
	v.append(m)
	

print(a)
print(v)