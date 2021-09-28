def mdc(a,b):
	if b==0:
		return a
	else:
		return mdc(b, a%b)

a=int(input("Insira A: "))
b=int(input("Insira B: "))

if a<b:
	aux=b
	b=a
	a=aux

print("o MDC (%d, %d) = %d."%(a,b, mdc(a,b)))