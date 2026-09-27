import random
import time
tabuleiro = {1:' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def mostrar_tabuleiro(tabuleiro):
	print(f'| {tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]} |')
	print(f'| {tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]} |')
	print(f'| {tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]} |\n')
	


def vez_do_jogador(tabuleiro):
	while True:
		try:
			numero = int(input('Sua vez: '))
			time.sleep(1)
		
			if tabuleiro[numero] == ' ':
				tabuleiro[numero] = 'X'
				print(f'\033[1;33mVocê escolheu a posição {numero}\033[0m')
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
		


def main():
	print('\033[1;29mEscolha um dos números para fazer uma jogada.\033[0m')
	print(f'| {1} | {2} | {3} |')
	print(f'| {4} | {5} | {6} |')
	print(f'| {7} | {8} | {9} |')
	while True:
		
		vez_do_jogador(tabuleiro)
		
		if condicao_vitoria(tabuleiro, 'X'):
			print('\033[1;32mParabéns você venceu!\n(o computador é burro!)\033[0m')
			print('')
			break
		
		if ' ' not in tabuleiro.values():
			print('\033[1;244mEmpate\033[0m')
			break
		
		vez_do_computador(tabuleiro)
			
		if condicao_vitoria(tabuleiro, 'O'):
			print('\033[1;31mComputador venceu!\033[0m')
			break
			


if __name__ == '__main__':
	main()