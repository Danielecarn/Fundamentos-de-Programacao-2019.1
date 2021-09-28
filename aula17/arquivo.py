arquivo = open("exemplo.txt", "w")
arquivo1 = open("impar.txt", "w")

for i in range(1,1001):
	if i%2 == 0:
		arquivo.write("{}\n".format(i))
	else:
		arquivo1.write("{}\n".format(i))

arquivo.close()
arquivo1.close()
