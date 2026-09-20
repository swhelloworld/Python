import random
tema = ['casa', 'mesa', 'mato', 'quadro', 'rampa', 'arvore', 'bola', 'carro', 'dama', 'estado', 'faca', 'gaiola', 'homem', 'imperio', 'jaula', 'kiwi', 'lapis', 'mulher', 'navio', 'osmose', 'padaria']
tema_escolhido = []
tema_escondido = []
boneco = {'cabeça': ' ', 'tronco1': ' ', 'tronco2': ' ', 'braço_direito': ' ', 'braço_esquerdo': ' ', 'perna_direita': ' ', 'perna_esquerda': ' '}
tentativas = []

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
	for c, d in enumerate(tema_escolhido):
		if d == letra:
			tema_escondido[c] = letra

def add_tema():
	rand = random.randint(0, len(tema) - 1)
	for z in tema[rand]:
		tema_escolhido.append(z)
				
def bonec():
	if len(tentativas) == 1:
		boneco['cabeça'] = 0
	if len(tentativas) == 2:
		boneco['tronco1'] = '|'
	if len(tentativas) == 3:
		boneco['tronco2'] = '|'
	if len(tentativas) == 4:
		boneco['braço_direito'] = '/'
	if len(tentativas) == 5:
		boneco['braço_esquerdo'] = '\\'
	if len(tentativas) == 6:
		boneco['perna_direita'] = '/'
	if len(tentativas) == 7:
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
 	
def derrota():
	print('\033[31mVocê perdeu!!\033[0m')
	boneco.update({'cabeça': ' ', 'tronco1': ' ', 'tronco2': ' ', 'braço_direito': ' ', 'braço_esquerdo': ' ', 'perna_direita': ' ', 'perna_esquerda': ' '})
	tentativas.clear()
	tema_escolhido.clear()
	tema_escondido.clear()
	add_tema()
	add_hifen()
	jogar_novamente()
	
def vitoria():
	print('\033[32mParabéns Você Acertou!!!\033[0m')
	boneco.update({'cabeça': ' ', 'tronco1': ' ', 'tronco2': ' ', 'braço_direito': ' ', 'braço_esquerdo': ' ', 'perna_direita': ' ', 'perna_esquerda': ' '})
	tentativas.clear()
	tema_escolhido.clear()
	tema_escondido.clear()
	add_tema()
	add_hifen()
	jogar_novamente()
							
add_tema()
add_hifen()
while True:		
	bonec()	
	print(*tema_escondido)	
	letra = input('Digite uma letra: ').strip().lower()
	add_letra()	
	if letra not in tema_escolhido:
		tentativas.append('1') 
	if len(tentativas) == 7:
		bonec()
		print(*tema_escolhido)
		derrota()	
	if tema_escondido.count('-') == 0:
		bonec()
		print(*tema_escondido)
		vitoria()