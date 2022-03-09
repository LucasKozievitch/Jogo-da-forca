# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random # vai buscar a palavra de forma randomica no banco de palavras

# Board (tabuleiro)
# board vai criar uma lista, cada objeto dentro de aspas trilpas e a virgula separa cada objeto
# cada vez que errar uma letra, o programa vai pegar o proximo objeto até chegar no boneco enforcado
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
# criando a classe Hangman
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word # vai procurar uma palavra
		self.missed_letters = [] # cria uma lista vazia para as palavras erradas
		self.guessed_letters = [] # cria uma lista vazia para as palavras corretas
		
	# Método para adivinhar a letra
	def guess(self, letter): # recebe como parametro uma letra(letter)
		if letter in self.word and letter not in self.guessed_letters:
		# se a letra dentro da palavra e letra não estiver dentro da lista de palavras certas faça algo	
			self.guessed_letters.append(letter) 
			# se a letra ainda não estiver na lista de palavras corretas, então eu vou adicionar(append)
		elif letter not in self.word and letter not in self.missed_letters:
		# se a letra não estiver dentro da palavra e a letra não estiver dentro da lista de palavras erradas	
			self.missed_letters.append(letter)
			# se a letra não estiver na lista de palavras erradas, então eu vou adicionar(append)
		else: # senão retorna falso ou finaliza e retorna verdadeiro
			return False
		return True
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.hangman_won() or (len(self.missed_letters) == 6)
		# retorna o Hangman para saber se venceu 
		# ou verifica se o comprimento da lista de palavras erradas é igual a 6 e o jogador perdeu 
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '_' not in self.hide_word():
		# se não tem mais nenhum _ então o usuário ganhou	
			return True
		return False
		
	# Método para não mostrar a letra no board
	def hide_word(self):
		rtn = ''
		for letter in self.word:
		# para cada letra dentro da string	
			if letter not in self.guessed_letters:
			# se a letra não estiver dentro da sequencia de letras da palavra	
				rtn += '_'
				# então retorna o _
			else:
				rtn += letter
				# se tem a letra então adiciona ela na sequência
		return rtn
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print (board[len(self.missed_letters)])
		print ('\nPalavra: ' + self.hide_word())
		print ('\nLetras erradas: ',) 
		for letter in self.missed_letters:
			print (letter,) 
		print ()
		print ('Letras corretas: ',)
		for letter in self.guessed_letters:
			print (letter,)
		print ()

# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
		with open("palavras.txt", "rt") as f:
			bank = f.readlines()
		return bank[random.randint(0,len(bank))].strip()

# Método Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over():
		game.print_game_status()
		user_input = input('\nDigite uma letra: ')
		game.guess(user_input)

	# Verifica o status do jogo
	game.print_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

