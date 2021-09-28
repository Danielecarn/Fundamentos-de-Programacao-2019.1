n=[0]*10

for i in range(0,10):
	n[i]=float(input("Digite a %d° nota: "% (i+1)))

for a in range(0,len(n)):
  if n[a]>= 4 and n[a]<7:
    print("Ficou de AF na posição",a+1," com a nota ",n[a])

m=sum(n)/len(n)

print("Média da turma",m)

