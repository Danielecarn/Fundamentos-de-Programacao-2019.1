import random
na=random.randint(1,10)
nt=0
n=int(input("Adivinhe o número!\nEscolha o nível:\n1-Beginner\n2-Hard\n3-Insane\nDigite sua opção:"))
if n==1:
  while True:
    n=int(input("Tente adivinhar o número!"))
    if n<na:
      print("Digite um número maior!")
    elif n>na:
      print("Digite um número menor!")
    nt=nt+1
    if n==na:
      print("Você acertou!\nNúmero de tentativas:",nt)
      break
elif n==2:  
  for i in range(3):
    n=int(input("Tente adivinhar o número!"))
    if n<na:
      print("Digite um número maior!")
    elif n>na:
      print("Digite um número menor!")
    nt=nt+1
    if n==na:
      print("Você acertou!\nNúmero de tentativas:",nt)
      break
elif n==3:
  for i in range(3):
    n=int(input("Tente adivinhar o número!"))
    nt=nt+1
    if n==na:
      print("Você acertou!\nNúmero de tentativas:",nt)
      break
     