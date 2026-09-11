dominios = ['.com', '.net', '.org']
alfabeto = [' ', 'A', 'Á', 'Â', 'B', 'C', 'D', 'E', 'É', 'Ê', 'F', 'G', 'H', 'I', 'Í', 'J', 'K', 'L', 'M', 'N', 'O', 'Ó', 'Ô', 'Õ', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'â', 'ã', 'é', 'ê', 'í', 'ó', 'ô', 'õ', 'ú', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '@', '-', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

cadastro = []
login = []
try:
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            login.append(dados)
except FileNotFoundError:
    pass

pera = []
uva = []
banana = 0
while True:
	print('-' * 30)
	print('\033[38;5;202mBEM-VINDO À TELA INICIAL\033[0m')
	print('-' * 30)
	print('''\033[38;5;226m[1] - Log In\033[0m
\033[38;5;227m[2] - Se Cadastrar\033[0m
\033[38;5;228m[3] - Sair\033[0m''')
	opcao = int(input('-: '))
	if opcao != 1 and opcao != 2 and opcao != 3:
		print('\033[31mResposta inválida!\033[0m')
	elif opcao == 3:
		print('Volte Sempre!')
		break
	elif opcao == 2:
		print('-' * 30)
		print('\033[38;5;202mBEM VINDO À TELA DE CADASTRO!\033[0m')
		print('-' * 30)
		while True:
			nome = input('\033[38;5;226mDigite o seu primeiro nome: \033[0m').strip()
			if not all(caracte in alfabeto[0:71] for caracte in nome):
				print('\033[38;5;196mNúmeros e caracteres especiais são inválidos.\033[0m')
				print('-' * 30)
			elif len(nome) > 20:
				print('\033[38;5;196mNome muito longo.\033[0m')
				print('-' * 30)
			elif len(nome) < 2:
				print('\033[38;5;196mNome muito curto.\033[0m')
				print('-' * 30)
			else:
				print('\033[38;5;46mPrimeiro nome cadastrado com sucesso.\033[0m')
				break
				
		while True:
			print('-' * 30)
			sobrenome = input('\033[38;5;226mDigite o seu sobrenome: \033[0m').strip()
			if not all(x in alfabeto[0:71] for x in sobrenome):
				print('\033[38;5;196mNúmeros e caracteres especiais são inválidos.\033[0m')
			elif len(sobrenome) > 30:
				print('\033[38;5;196mSobrenome muito longo.\033[0m')
			elif len(sobrenome) < 2:
				print('\033[38;5;196mSobrenome muito curto.\033[0m')
			else:
				print('\033[38;5;46mSobrenome cadastrado com sucesso.\033[0m')
				break
				
		while True:
			print('-' * 30)
			shrek = ' '
			email = input('\033[38;5;226mDigite o seu email: \033[0m').strip()
			qtd = len(email)
			index = email.find('@')
			for m, n in enumerate(login):
				if email == login[m][2] and len(login) >= 1:
					shrek = 's'
			if shrek == 's':
				print('\033[38;5;196mEmail já cadastrado.\033[0m')
			elif not all(car in alfabeto[44:73] for car in email[index:]):
				print('\033[38;5;196mTipo de caractere inválido.\033[0m')			
			elif not all(u in alfabeto[44:] for u in email[:index]):
				print('\033[38;5;196mTipo de caractere inválido.\033[0m')
			elif '@' not in email:
				print('\033[38;5;196mEmail inválido, precisa conter @.\033[0m')	
			elif not any(dominio in email[qtd-4: qtd] for dominio in dominios):
				print('\033[38;5;196mSeu domínio está incorreto, informe domínios como: .com .org ou .net !\033[0m')
			elif len(email[:index]) < 4 and email.count('@') < 2:
				print('\033[38;5;196mCaracteres insuficientes. \033[0m')	
			elif email.count('@') > 1:
				print('\033[38;5;196mSomente um @ é permitido\033[0m')
			elif len(email[:index]) > 15:
				print('\033[38;5;196mEmail muito longo.\033[0m')
			elif len(email[index:]) > 15:
				print('\033[38;5;196mEmail muito longo.\033[0m')
			elif len(email[index:len(email) - 4]) < 6:
				print('\033[38;5;196mCaracteres insuficientes\033[0m')
			elif email[index:].find('.') != len(email[index:]) - 4:
				print('\033[38;5;196mTipo de email inválido.\033[0m')
			elif not all(k in alfabeto[44:69] for k in email[0]):
				print('\033[38;5;196mPrimeiro caractere precisa ser letra\033[0m')
			else:
				print('\033[38;5;46mEmail cadastrado com sucesso.\033[0m')
				break
			
		while True:
			print('-' * 30)
			senha = input('\033[38;5;226mDigite sua senha: \033[0m')
			if senha == senha.upper():
				print('\033[38;5;196mPrecisa de pelo menos um caractere minúsculo.\033[0m')
			elif senha == senha.lower():
				print('\033[38;5;196mPrecisa de pelo menos um caractere maiúsculo.\033[0m')
			elif len(senha) < 8:
				print('\033[38;5;196mSenha precisa de no mínimo 8 caracteres.\033[0m')
			elif len(senha) > 30:
				print('\033[38;5;196mSenha muito longa.\033[0m')
			elif not all(a in caracteres for a in senha):
				print('\033[38;5;196mTipo de caractere não permitido em senhas.\033[0m')		
			elif not any(b in caracteres[53:84] for b in senha):
				print('\033[38;5;196mPrecisa de caracteres especiais como (! @ # $ )\033[0m')
			elif not any(c in caracteres[84:] for c in senha):
				print('\033[38;5;196mPrecisa de pelo menos um número\033[0m')
			else:
				print('\033[38;5;46mConta cadastrada com sucesso.\033[0m')
				cadastro.append(nome.lower().capitalize())
				cadastro.append(sobrenome)
				cadastro.append(email)
				cadastro.append(senha)
				login.append(cadastro[:])
				with open("usuarios.txt", "a") as arquivo: arquivo.write(",".join(cadastro) + "\n")
				cadastro.clear()				
				break
				
	elif opcao == 1:
		print('-' * 30)
		print('\033[38;5;202mBEM-VINDO À TELA DE LOG IN\033[0m')
		print('-' * 30)
		while True:
			email_login = input('\033[38;5;226mDigite seu email: \033[0m')
			for k, o in enumerate(login):
				if email_login == login[k][2]:
					pera.append('s')
				if email_login == o[2]:
					banana = k			
			if 's' in pera:
				pera.clear()
				print('\033[38;5;46mEmail correto!\033[0m')
				break
			else:
				print('\033[38;5;196mEmail incorreto.\033[0m')
				print('-' * 30)	
				
		while True:
			print('-' * 30)
			senha_login = input('\033[38;5;226mDigite sua senha: \033[0m')
			for gu, qu in enumerate(login):
				if senha_login == login[banana][3]:
					uva.append('s')
			if 's' in uva:
				uva.clear()
				print('\033[38;5;46mSenha correta.\033[0m')
				print(f'\033[38;5;46mLogin efetuado com sucesso!\033[0m')
				print('-' * 30)
				print(f'\033[38;5;203mSeja Bem-Vindo(a)\033[0m \033[38;5;14m{login[banana][0]}.\033[0m')
				break
			else:
				print('\033[38;5;196mSenha incorreta.\033[0m')
		while True:
			print('\033[38;5;202mESCOLHA UM JOGO PARA JOGAR:\033[0m')
			print('-' * 30)
			print('\033[38;5;226m[1] - Jogo Da Advinhação.\033[0m')
			print('\033[38;5;227m[0] - Sair Da Conta.\033[0m')
			escolha = int(input('-:  '))
			if escolha == 1:
				import random
				rand = random.randint(0, 100)
				cont = 0
				print('-' * 30)
				print('\033[38;5;226mJOGO DA ADVINHAÇÃO.\033[0m')
				print('-' * 30)
				while True:
					cont = cont + 1
					a = int(input('\033[35mAdvinhe um número de 0 a 100: \033[0m'))
					if a > 100 or a < 0:
						print('\033[31mNúmero inválido, digite um número de 0 a 100.\033[0m')
						print('-' * 30)
					if a == rand:
						print(f'\033[32mParabéns {login[banana][0]} você acertou!\033[0m')
						print(f'\033[32mForam necessarias {cont} tentativas para você acertar.\033[0m')
						print('-' * 30)
						break
					if a != rand and a <= 100 and a >= 0:
						print('\033[31mVocê errou, continue tentando!\033[0m')
					for b in range (0, 6):
						if a == rand - b or a == rand + b and a <= 100:
							if a >= 0:
								print('\033[34mVocê está PERTISSIMO!!!!\033[0m')
								print('-' * 30)
					for c in range(0, 20):
						if a == (rand - 6) - c or a == (rand + 6) + c and a <= 100:
							if a >= 0:
								print ('\033[32mVocê está PERTO!!\033[0m')
								print('-' * 30)
					for d in range(0, 20):
						if a == (rand - 26) - d or a == (rand + 26) + d and a <= 100:
							if a >= 0:
								print('\033[38;5;208mVocê está quase chegando perto!\033[0m')
								print('-' * 30)
					for e in range (0, 20):
						if a == (rand - 46) - e or a == (rand + 46) + e and a <= 100:
							if a >= 0:
								print('\033[33mVocê está longe!\033[0m')
								print('-' * 30)
					for f in range (0, 40):
						if a == (rand-66) - f or a == (rand+66) + f and a <= 100:
							if a >= 0:
								print('\033[31mVocê está MUITO longe!\033[0m')
								print('-' * 30)
			if escolha == 0:
				import time
				banana = ''
				print('Saindo da conta...')
				time.sleep(2)
				print('Isso pode demorar alguns segundos.')
				time.sleep(4)
				break	