nota1 = float(input("Digite a 1 nota: "))
nota2 = float(input("Digite a 2 nota: "))

media = (nota1 + nota2)/2

if(media>=7):
    print("Aprovado, média:", media)
elif(media >=4):
    print("Af, média:", media)
else:
    print("Reprovado, média: ", media)