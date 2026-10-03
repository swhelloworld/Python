import random
import time

def mostrar_tabuleiro(tabuleiro):
	print(f'| {tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]} |')
	print(f'| {tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]} |')
	print(f'| {tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]} |\n')


def vez_do_jogador(tabuleiro, simbolo, texto):
	while True:
		try:
			numero = int(input(f'Vez do jogador {simbolo}: '))
			time.sleep(1)
		
			if tabuleiro[numero] == ' ':
				tabuleiro[numero] = simbolo
				print(f'\033[1;33m{texto} {numero}\033[0m')
				mostrar_tabuleiro(tabuleiro)
				break
			
			else: 
				print('\033[1;31mPosição já ocupada, tente outra!\033[0m')
				mostrar_tabuleiro(tabuleiro)
				
		except (ValueError, KeyError):
			print('\033[1;31mApenas números entre 1 e 9 são permitidos.\033[0m')
			mostrar_tabuleiro(tabuleiro)
			
									
def vez_do_computador(tabuleiro):
	aleatorio = random.randint(1, 9)
	while True:
		if tabuleiro[aleatorio] != ' ':
			aleatorio = random.randint(1, 9)
		elif tabuleiro[aleatorio] == ' ':
			break
			
	print('Vez do computador: ')
	time.sleep(1)
	tabuleiro[aleatorio] = 'O'
	print(f'\033[1;33mComputador escolheu a posição {aleatorio}\033[0m')
	mostrar_tabuleiro(tabuleiro)


def condicao_vitoria(tabuleiro, simbolo):
	if tabuleiro[1] == simbolo and tabuleiro[2] == simbolo and tabuleiro[3] == simbolo:
		return True

	elif tabuleiro[4] == simbolo and tabuleiro[5] == simbolo and tabuleiro[6] == simbolo:
		return True
	
	elif tabuleiro[7] == simbolo and tabuleiro[8] == simbolo and tabuleiro[9] == simbolo:
		return True
	
	elif tabuleiro[1] == simbolo and tabuleiro[4] == simbolo and tabuleiro[7] == simbolo:
		return True
	
	elif tabuleiro[2] == simbolo and tabuleiro[5] == simbolo and tabuleiro[8] == simbolo:
		return True
	
	elif tabuleiro[3] == simbolo and tabuleiro[6] == simbolo and tabuleiro[9] == simbolo:
		return True
	
	elif tabuleiro[1] == simbolo and tabuleiro[5] == simbolo and tabuleiro[9] == simbolo:
		return True
	
	elif tabuleiro[3] == simbolo and tabuleiro[5] == simbolo and tabuleiro[7] == simbolo:
		return True
	
	return False
	
	
def checar_vitoria(tabuleiro, texto, simbolo):
	if condicao_vitoria(tabuleiro, simbolo):
		print(texto)
		return True
		
	if ' ' not in tabuleiro.values():
		print('\033[1;29mO jogo empatou :/ \033[0m\n')
		return True
		
	return False
	
	
def cabecalho(titulo):
	print('-' * 45)
	print(titulo)
	print('-' * 45)
	print('\033[1;33mEscolha um dos números para fazer uma jogada.\033[0m')
	print(f'| 1 | 2 | 3 |')
	print(f'| 4 | 5 | 6 |')
	print(f'| 7 | 8 | 9 |')


def jogador_vs_computador():
	tabuleiro = {1:' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
	cabecalho('Bem - vindo ao modo jogador contra computador')
	
	while True:
		vez_do_jogador(tabuleiro, 'X', 'Você escolheu posição')
		
		if checar_vitoria(tabuleiro, 'X' '\033[1;32mParabéns você venceu!\033[0m\n'):
			break
		
		vez_do_computador(tabuleiro)
			
		if checar_vitoria(tabuleiro, 'O' '\033[1;31mO computador venceu\033[0m\n'):
			break


def jogador_vs_jogador():
	tabuleiro = {1:' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
	cabecalho('Bem - vindo ao modo jogador contra jogador')
	
	while True:
		vez_do_jogador(tabuleiro, 'X', 'Jogador X escolheu posição')
		
		if checar_vitoria(tabuleiro, 'X', '\033[1;32mParabéns jogador X você venceu!\033[0m\n'):
			break
			
		vez_do_jogador(tabuleiro, 'O', 'Jogador O escolheu posição')
		
		if checar_vitoria(tabuleiro, 'O' '\033[1;32mParabéns jogador O você venceu!\033[0m\n'):
			break
			
			
def main():
	while True:
		print('[1] - Jogador vs jogador.\n[2] - Jogar contra computador.\n[3] - Sair')
		escolha = input('-: ')
		
		time.sleep(1)
		if escolha == '1':
			jogador_vs_jogador()
			
		elif escolha == '2':
			jogador_vs_computador()
			
		elif escolha == '3':
			break
			
		else:
			print('\033[1;31mCaractere inválido!\033[0m')
	
	
if __name__ == '__main__':
	main()
