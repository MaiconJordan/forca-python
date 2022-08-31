# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>JOGO DA FORCA<<<<<<<<<<

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
class Forca:
    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letra_errada = []
        self.letra_certa = []

    # Método para adivinhar a letra
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letra_certa
            self.letra_certa.append(letra)
        elif letra not in self.palavra and palavra not in self.letra_errada
            self.letra_errada.append(letra)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def fim_jogo(self):
        return self.forca_venceu() or (len(self.letra_errada) == 6)

    # Método para verificar se o jogador venceu
    def forca_venceu(self):
        if '_' not in self.hide_palavra:
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_palavra(self):
        rtn = ''
        for letra in self.palavra
            if letra not in self.letra_certa:
                rtn += '_'
            else:
                rtn += letra
            return rtn


    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):



# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
