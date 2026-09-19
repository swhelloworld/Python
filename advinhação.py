import random
rand = random.randint(0, 100)
cont = 0
print('-' * 30)
print('\033[38;5;208mJOGO DA ADVINHAÇÃO.\033[0m')
print('-' * 30)
while True:
	cont = cont + 1
	a = int(input('\033[35mAdvinhe um número de 0 a 100: \033[0m'))
	if a > 100 or a < 0:
		print('\033[31mNúmero inválido, digite um número de 0 a 100.\033[0m')
		print('-' * 30)
	if a == rand:
		print('\033[32mVocê acertou!\033[0m')
		break
	if a != rand and a <= 100 and a >= 0:
		print('\033[31mVocê errou, continue tentando!\033[0m')
	for b in range (0, 5):
		if a == rand - b or a == rand + b and a <= 100:
			if a >= 0:
				print('\033[34mVocê está PERTISSIMO!!!!\033[0m')
			print('-' * 30)
	for c in range(0, 20):
		if a == (rand - 5) - c or a == (rand + 5) + c and a <= 100:
			if a >= 0:
				print ('\033[32mVocê está PERTO!!\033[0m')
				print('-' * 30)
	for d in range(0, 20):
		if a == (rand - 25) - d or a == (rand + 25) + d and a <= 100:
			if a >= 0:
				print('\033[36mVocê está quase chegando perto!\033[0m')
			print('-' * 30)
	for e in range (0, 20):
		if a == (rand - 45) - e or a == (rand + 45) + e and a <= 100:
			if a >= 0:
				print('\033[33mVocê está longe!\033[0m')
			print('-' * 30)
	for f in range (0, 40):
		if a == (rand-65) - f or a == (rand+65) + f and a <= 100:
			if a >= 0:
				print('\033[31mVocê está MUITO longe!\033[0m')
				print('-' * 30)
print(f'\033[32mForam necessárias {cont} tentativas para você acertar.\033[0m')