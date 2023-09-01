import random

class Hangman:

    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.missed_letters = []
        self.board = [
            '''
            >>>>>>>>>>Hangman<<<<<<<<<<

            +---+
            |   |
                |
                |
                |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
            /|   |
                |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
            /|\\  |
                |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
            /|\\  |
            /    |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
            /|\\  |
            / \\  |
                |
            =========
            '''
        ]

    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)

    def hangman_won(self):
        return set(self.word) == set(self.guessed_letters)

    def hide_word(self):
        hidden_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "_"
        return hidden_word

    def print_game_status(self):
        print(self.board[len(self.missed_letters)])
        print("Palavra: " + self.hide_word())
        print("Letras corretas: " + ", ".join(self.guessed_letters))
        print("Letras erradas: " + ", ".join(self.missed_letters))

def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank) - 1)].strip()

def main():
    game = Hangman(rand_word())

    while not game.hangman_over():
        game.print_game_status()
        letter = input("Adivinhe uma letra: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Por favor, insira uma única letra válida.")
            continue
        if not game.guess(letter):
            print("Letra já adivinhada ou incorreta. Tente novamente.")

    game.print_game_status()
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

if __name__ == "__main__":
    main()
