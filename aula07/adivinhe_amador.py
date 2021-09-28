import random
na=random.randint(1,10)
nt=0
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