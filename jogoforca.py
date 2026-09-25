import random
import sys
temas = ('arrependimento', 'brutalidade', 'carpinteiro', 'dinamarca', 'encanador', 'fertilidade', 'ganancioso', 'computador', 'dispositivo', 'empreendedor', 'fidelidade', 'generosidade', 'humanidade', 'intimidade', 'juventude', 'kiwi', 'longevidade', 'mediocridade', 'necessidade', 'oportunidade', 'procrastinar', 'quantidade', 'relacionamento', 'superficial', 'tecnologia', 'uniforme', 'vascularizado', 'xadrez', 'zoologico', 'ambicioso', 'bochecha', 'complexo', 'dicionario', 'extrovertido', 'felicidade', 'gentileza', 'habilidade', 'importante', 'julgamento', 'linguagem', 'maturidade', 'nacionalidade', 'organismo', 'perspectiva', 'quilometro', 'responsabilidade', 'superestimado', 'transparente', 'universidade', 'vulnerabilidade', 'xenofobia', 'aposentado', 'bibliografia', 'caracteristica', 'desenvolvimento', 'exponencial', 'fragmentado', 'guardanapo', 'hereditario', 'independente', 'jabuticaba', 'lubrificante', 'meteorologia', 'neurotransmissor')
tema_escolhido = []
tema_escondido = []
boneco = {'cabeça': ' ', 'tronco1': ' ', 'tronco2': ' ', 'braço_direito': ' ', 'braço_esquerdo': ' ', 'perna_direita': ' ', 'perna_esquerda': ' '}
tentativas_erradas = []

def jogar_novamente():
	while True:
		print('[1] - Jogar Novamente.\n[2] - Sair. ')
		opcao = int(input('-: '))
		if opcao == 1:
			break
		elif opcao == 2:
			sys.exit()
		else:
			print('\033[1;38;5;9mERRO: Opção inexistente.\033[0m')

def add_hifen():
	for c in range(0, len(tema_escolhido)):
		tema_escondido.append('-')

def add_letra():
	for posição, caractere in enumerate(tema_escolhido):
		if caractere == letra:
			tema_escondido[posição] = letra

def add_tema():
	rand = random.randint(0, len(temas) - 1)
	for palavra in temas[rand]:
		tema_escolhido.append(palavra)
				
def add_boneco():
	if len(tentativas_erradas) == 1:
		boneco['cabeça'] = 'O'
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
	print(*tema_escondido)
	letra = input('Digite uma letra: ').strip().lower()
	add_letra()
		
	if letra not in tema_escolhido and letra not in tentativas_erradas and len(letra) == 1 and letra.isalpha():
		tentativas_erradas.append(letra) 
		
	if len(tentativas_erradas) == 7:
		add_boneco()
		print(*tema_escolhido)
		print('\033[1;31mVocê perdeu!\033[0m')
		resetar_jogo()
			
	if tema_escondido.count('-') == 0:
		add_boneco()
		print(*tema_escondido)
		print('\033[1;32mParabéns, você acertou!\033[0m')
		resetar_jogo()