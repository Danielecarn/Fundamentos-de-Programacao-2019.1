codigo=[]
qtd=[]
for i in range(10):
  m=int(input("Códigos: "))
  codigo.append(m)
for j in range(10):
  n=int(input("Quantidade dos produtos: "))
  qtd.append(n)
while True:
  c=int(input("Digite o código: "))
  cont=0
  for a in range(10): 
    if codigo[a]!=c and c!=0:
      cont+=1
    elif codigo[a]==c and qtd[a]!=0:
      print("Pedido atendido com sucesso")
      qtd[a]-=1
    elif codigo[a]==c and qtd[a]==0:
      print("Sem estoque!")
  if cont==10:
    print("Código inexistente")
  elif c==0:
    for y in range(10):
      print("Código: ",codigo[y],"Quantidade: ",qtd[y])
    break
    