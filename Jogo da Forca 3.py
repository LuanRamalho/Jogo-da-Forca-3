#first i have to say, i didn't develope this all by myself. I tried, but with the "display_hangman" function i needed help.
import random
word_list = ["inserir", "teu", "palavras", "em", "esse", "python", "lista", 'árvore', 'maçã', 'futebol',
             'esporte', 'computador', 'agir' , 'ajuda' , 'amor']

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Vamos jogar jogo da forca")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("adivinhe uma letra ou palavra: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("você já tentou", guess, "!")
            elif guess not in word:
                print(guess, "não está na palavra :(")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("o bom,", guess, "está na palavra!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Você já tentou ", guess, "!")
            elif guess != word:
                print(guess, " não é a palavra :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("entrada inválida")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Bom trabalho, você adivinhou a palavra!")
    else:
        print("Sinto muito, mas você ficou sem tentativas. A palavra era " + word + ". Talvez na próxima vez!")




def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

def main():
    word = get_word(word_list)
    play(word)
    while input("Novamente? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()