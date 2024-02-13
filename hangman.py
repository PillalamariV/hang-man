import random as rand
import pictures

words = ["God", "Cow", "Horse", "Apple", "Microsoft", "Jobs", "Books"]
game_word = rand.choice(words).lower()
print(game_word)
board = []
for x in range(len(game_word)):
    board.append("_")

def check(guess_letter):
    count = 0
    if (guess_letter in game_word):
        for x in game_word:
            if (guess_letter == x):
                board[count] = guess_letter
            count += 1
        return True
    else:
        return False

def display_word():
    return ' '.join(board)

def display_art(index):
    if (index >= 1):
        print(pictures.stages[index])

game_play = True
hangman = 0
while (game_play):
    if (hangman == len(pictures.stages) - 1):
        game_play = False
        display_art(hangman)
        print("You lose. The correct answer is " + game_word)
        break
    display_art(hangman)
    player_guess = display_word()
    print(player_guess)
    guess_letter = input("\nEnter a letter: ").lower()
    if (guess_letter in player_guess):
        display_art(hangman)
        print("You already guessed that word.")
    if check(guess_letter) == False:
        hangman += 1
    if (''.join(board) == game_word):
        game_play = False
        display_art(hangman)
        print(display_word())
        print("You win")
