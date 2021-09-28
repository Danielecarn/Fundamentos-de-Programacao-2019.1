def cadastro_livro(livros):
	arq=open(livros,'a+')
	livro={}
	livro['code']=input('Digite o código do livro: ')
	livro['title']=input('Digite o título do livro: ')
	livro['autor']=input('Digite o autor do livro: ')
	livro['page']=input('Digite a quantidade de páginas do livro: ')
	print(livro)
	arq.write(livro['code'] +','+ livro['title']+','+livro['autor']+','+livro['page'])
	arq.write('\n')
	print('Livro adicionado com sucesso!')
	arq.close()

def mostrar_livro(livros):
	arq=open(livros,'r')
	for linha in arq.readlines():
		lista=linha.strip()
		print(lista)
	arq.close()

def emprestimo(livros):
	cod=input('Pesquise um livro: ')
	arq=open(livros,'a+')
	livro_encontrado=[]
	for linha in arq.readlines():
		lista=linha.strip().split(',')
		print(lista)
		'''if cod == lista[0]:
			print(lista[0])
			livro_encontrado=lista
	if livro_encontrado == []:
		print(livro_encontrado)
		print('Livro não encontrado! :(')'''





escolha=int(input('1 - Cadastro de livros\n2 - Emprestimo de Livros\n3 - Exibir livros'))
if escolha == 1:
	cadastro_livro('livros.txt')
elif escolha == 2:
	emprestimo('livros.txt')
elif escolha == 3:
	mostrar_livro('livros.txt')
