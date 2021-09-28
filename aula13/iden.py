iden=[]
l=int(input("linhas da matriz"))


for a in range(l):
	linha=[0]*l
	iden.append(linha)

for i in range(l):
	for j in range(l):
		if i==j:
			iden[i][j]=1
	print(iden[i])