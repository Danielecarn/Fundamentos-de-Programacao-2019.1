agenda={}

def inserir_contato(agenda):
	nome=input('Digite o nome do contato: ')
	fone=input('Digite o telefone: ')
	agenda[nome]=fone

def busca_contato(agenda):
	nome=input('Digite o nome do contato: ')
	if nome in agenda:
		return agenda[nome]
	else:
		return None
def remove_contato(agenda):
	nome=input('Digite o nome para remover: ')
	if nome in agenda:
		del agenda[nome]
		print('tirei já %s'%nome)
	else:
		print('Nome nao encontrado')

def lista_todos(agenda):
	print('Nome          Telefone')
	for nome in sorted(agenda):
		print('%-11s - %s'%(nome,agenda[nome]))

def salva_agenda(agenda):
	nome_arq=input('Digite o nome do arquivo: ')
	arq=open(nome_arq,'w')
	for nome in agenda:
		arq.write('%s,%s\n'%(nome,agenda[nome]))
	arq.close()
	print('Salvo')

def carrega_agenda(agenda):
	nome_arq=input('Nome do arq: ')
	arq=open(nome_arq,'r')
	for linha in arq:
		lista=linha.split(',')
		nome=lista[0].strip()
		tel=lista[1].strip()
		agenda[nome]=tel
	arq.close()
	print('agenda carregada')

while True:
	print('********** FUPfones **********\n\
	*** Existem: 0 contatos ***\n\
	******************************\n\
	1. Inserir um contato\n\
	2. Consultar telefone\n\
	3. Remover um contato\n\
	4. Listar toda a agenda\n\
	5. Ler contatos de arquivo\n\
	6. Salvar agenda\n\
	7. Finalizar\n\
	Digite a opção desejada:')

	opcao=int(input(''))

	if opcao == 1:
		inserir_contato(agenda)
		
	if opcao == 2:
		print('Consultando um telefone\n')
		telefone=busca_contato(agenda)
		if telefone is not None:
			print('Telefone: %s'%telefone)
		else:
			print('Contato não existe')

	if opcao == 3:
		remove_contato(agenda)

	if opcao == 4:
		lista_todos(agenda)

	if opcao == 5:
		carrega_agenda(agenda)

	if opcao == 6:
		salva_agenda(agenda)
	if opcao ==7:
		break
