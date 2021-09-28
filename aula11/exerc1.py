x=[]
par=[]
impar=[]

for i in range(10):
  m=int(input("Insira um numéro: "))
  x.append(m)

print(x)
contpar=0
contimpar=0
for j in range(10):
  if x[j]%2==0:
    par.append(x[j])
    #print("Par: ",x[j])
    contpar+=1
  else:
    impar.append(x[j])
    #print("Impar: ",x[j])
    contimpar+=1

print("pares: ",contpar,"Quantidade de pares: ",par,"impares: ",contimpar,"Quantidade de impares: ",impar)