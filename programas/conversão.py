
""" Conversão entre Decimais, Binários, Octais, Hexadecimais
    Equipe: João Victor Alves de Oliveira
            Anderson Luis Feitosa Ribeiro
            Daniele Carnaúba Gonçalves"""

def DecToBase(num, base, simbolos):
    r = ""
    num2 = num//base
    while num2>0 :
        r += simbolos[num-num2*base]
        num = num2
        num2 = num//base
    r += simbolos[num-num2*base]
    return r[::-1]

def BaseToDec(strNumerica, base, simbolos):
    r = 0
    for i in range(0, len(strNumerica)):
        r += simbolos.index(strNumerica[-i-1])*base**i
    return r

hexaSimb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


print("\nO número desejado para conversão deve ser inserido junto com sua base sem espaços.\n\n"
      "Bases possíveis:\n d = decimal\n b = binário\n o = octal\n h = hexadecimal\n\n Ex: 10d\n\n"
      "Para sair do programa de conversões digite 'exit'\n")
while(True):
    entrada = input("Entre com o número e sua respectiva base: ").upper()
    if entrada[-1] == "D":
        identificador = "D"
        for i in range(0,len(identificador)):
            entrada = entrada.replace(identificador[i],"")
        print("")
        print(entrada,"- Decimal\n")    
        print(DecToBase(int(entrada),2,hexaSimb),"- Binário\n")
        print(DecToBase(int(entrada),8,hexaSimb),"- Octal\n")
        print(DecToBase(int(entrada),16,hexaSimb),"- Hexadecimal\n")

    elif entrada[-1] == "B":
        identificador = "B"
        for i in range(0,len(identificador)):
            entrada = entrada.replace(identificador[i],"")
        print("")
        numbase10 = BaseToDec(entrada,2,hexaSimb)
        print(numbase10,"- Decimal\n")
        print(entrada,"- Binário\n")
        print(DecToBase(numbase10,8,hexaSimb),"- Octal\n")
        print(DecToBase(numbase10,16,hexaSimb),"- Hexadecimal\n")
    elif entrada[-1] == "O":
        identificador = "O"
        for i in range(0,len(identificador)):
            entrada = entrada.replace(identificador[i],"")
        print("")
        numbase10 = BaseToDec(entrada,8,hexaSimb)
        print(numbase10,"- Decimal\n")
        print(DecToBase(numbase10,2,hexaSimb),"- Binário\n")
        print(entrada,"- Octal\n")
        print(DecToBase(numbase10,16,hexaSimb),"- Hexadecimal\n")
    elif entrada[-1] == "H":
        identificador = "H"
        for i in range(0,len(identificador)):
            entrada = entrada.replace(identificador[i],"")
        print("")
        numbase10 = BaseToDec(entrada,16,hexaSimb)
        print(numbase10,"- Decimal\n")
        print(DecToBase(numbase10,2,hexaSimb),"- Binário\n")
        print(DecToBase(numbase10,8,hexaSimb),"- Octal\n")
        print(entrada,"- Hexadecimal\n")
    elif entrada == "EXIT":
        break
    else:
        print("O formato informado é inválido")