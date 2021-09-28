x=[]
positivo=[]
negativo=[]

for i in range(8):
  m=int(input("Digite um numero"))
  x.append(m)
  if m >= 0:
    positivo.append(m)
  else:
    negativo.append(m)
print(x)
print("Positivos",positivo)
print("Negativos: ",negativo)