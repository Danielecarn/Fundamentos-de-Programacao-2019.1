'''Equipe: Anderson Luis Feitosa Ribeiro
		   Daniele Carnaúba Gonçalves
		   João Victor Alves de OLiveira'''

def xor_ab(a,b):
	if a==b:
		return "0"
	else:
		return "1"
def inverter(c):
	if c== "0":
		return "1"
	else:
		return "0"
def binToGray(bin):
	gray = ""
	gray += bin[0]
	for i in range(1,len(bin)):
		gray += xor_ab(bin[i-1],bin[i])
	return gray
def grayToBin(gray):
	binario = ""
	binario += gray[0]
	for i in range(1,len(gray)):
		if gray[i] == "0":
			binario += binario[i-1]
		else:
			binario += inverter(binario[i-1])
	return binario

while True:
	z=int(input("Digite a oção desejada para conversão\n1-Binário pra Gray\n2-Gray pra Binário\n3-Sair\n"))

	if z==1:
		numerobin = input("Numero binário: ")
		convertido = binToGray(numerobin)
		print("O numero inserido foi: ",numerobin," em binário e ",convertido," em gray")
	elif z==2:
		numerogray = input("Numero gray: ")
		convertido2 = grayToBin(numerogray)
		print("O numero inserido foi: ",numerogray," em gray e ",convertido2," em binario")
	if z==3:
		break
