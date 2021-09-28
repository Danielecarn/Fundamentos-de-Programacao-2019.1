produto=[]
qtd=[]
salario=545
for i in range(10):
  m=int(input("Valor do %d° produto: "%(i+1)))
  produto.append(m)
for j in range(10):
  q=int(input("Quantidade do %d° produto: "%(j+1)))
  qtd.append(q)
total=0
for a in range(10):
  print("Qtd vendida do ° produto: ",qtd[a])
  print("Valor unit do ° produto: ",produto[a])
  
  t=produto[a]*qtd[a]
  print("Valor total: ",t)
  total+=t

print(total)
comissao=(total*5)/100
salario+=comissao

print("Comissâo: ",comissao,"salario: ",salario)

maior=0
posicao=0
for x in range(10):
  if qtd[x]>maior:
    maior=qtd[x]
    posicao=x+1

print("Produto mais vendido: ",posicao,"Quantidade: ",maior)