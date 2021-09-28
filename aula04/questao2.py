n=int(input("Número: "))
i=1
while i*(i+1)*(i+2) <= n:
	if i*(i+1)*(i+2) == n:
		print("Número Triangular",i,(i+1),(i+2))
		break
	i+=1	
if i*(i+1)*(i+2) > n:
	print("N")