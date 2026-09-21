import random
tema = ('casa', 'mesa', 'mato', 'quadro', 'rampa', 'arvore', 'bola', 'carro', 'dama', 'estado', 'faca', 'gaiola', 'homem', 'imperio', 'jaula', 'kiwi', 'lapis', 'mulher', 'navio', 'osmose', 'padaria', 'queijo', 'ratoeira', 'sabonete', 'trovoada', 'uva', 'vitoria', 'xadrez', 'zoologico', 'amor', 'brasil', 'camelo', 'desejo', 'escola', 'futebol', 'grilo', 'hotel', 'igreja', 'janeiro', 'luva', 'madeira', 'novela', 'ovario', 'patinete', 'quilometro', 'rato', 'sistema', 'trabalho', 'universo', 'verme', 'xerox')
tema_escolhido = []
tema_escondido = []
boneco = {'cabeça': ' ', 'tronco1': ' ', 'tronco2': ' ', 'braço_direito': ' ', 'braço_esquerdo': ' ', 'perna_direita': ' ', 'perna_esquerda': ' '}
tentativas_erradas = []

def jogar_novamente():
	while True:
		print('''[1] - JOGAR NOVAMENTE''')
		opção = int(input('-: '))
		if opção == 1:
			break

def add_hifen():
	for c in range(0, len(tema_escolhido)):
		tema_escondido.append('-')

def add_letra():
	for posição, caractere in enumerate(tema_escolhido):
		if caractere == letra:
			tema_escondido[posição] = letra

def add_tema():
	rand = random.randint(0, len(tema) - 1)
	for palavra in tema[rand]:
		tema_escolhido.append(palavra)
				
def add_boneco():
	if len(tentativas_erradas) == 1:
		boneco['cabeça'] = 0
	elif len(tentativas_erradas) == 2:
		boneco['tronco1'] = '|'
	elif len(tentativas_erradas) == 3:
		boneco['tronco2'] = '|'
	elif len(tentativas_erradas) == 4:
		boneco['braço_direito'] = '/'
	elif len(tentativas_erradas) == 5:
		boneco['braço_esquerdo'] = '\\'
	elif len(tentativas_erradas) == 6:
		boneco['perna_direita'] = '/'
	elif len(tentativas_erradas) == 7:
		boneco['perna_esquerda'] = '\\'
	print('=' * 30)
	print('  |--------| ')
	print('  |        !')
	print(f'  |        {boneco['cabeça']}')
	print(f'  |       {boneco['braço_direito']}{boneco['tronco1']}{boneco['braço_esquerdo']}')
	print(f'  |        {boneco['tronco2']}')
	print(f' /|\\      {boneco['perna_direita']} {boneco['perna_esquerda']}')
	print('/ | \\')
	print('=' * 30)
 	
def resetar_jogo():
	boneco.update({'cabeça': ' ', 'tronco1': ' ', 'tronco2': ' ', 'braço_direito': ' ', 'braço_esquerdo': ' ', 'perna_direita': ' ', 'perna_esquerda': ' '})
	tentativas_erradas.clear()
	tema_escolhido.clear()
	tema_escondido.clear()
	add_tema()
	add_hifen()
	jogar_novamente()
						
add_tema()
add_hifen()
while True:		
	add_boneco()	
	print(*tema_escondido,'        ', *tentativas_erradas)
	letra = input('Digite uma letra: ').strip().lower()
	add_letra()	
	if letra not in tema_escolhido and letra not in tentativas_erradas and len(letra) == 1 and letra.isalpha():
		tentativas_erradas.append(letra) 
		
	if len(tentativas_erradas) == 7:
		add_boneco()
		print(*tema_escolhido,'        ', *tentativas_erradas)
		print('\033[31mVocê perdeu!!\033[0m')
		resetar_jogo()
			
	if tema_escondido.count('-') == 0:
		add_boneco()
		print(*tema_escondido, '        ', *tentativas_erradas)
		print('\033[32mParabéns Você Acertou!!!\033[0m')
		resetar_jogo()