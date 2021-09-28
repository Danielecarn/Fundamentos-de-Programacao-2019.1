x=[]
for i in range(5):
  m=int(input("Digite o número:"))
  x.append(m)
for a in range(5):
  if x[a]%2 == 0:
    print("Par: ",x[a])
    print("Posição: ",a+1)

print(x)