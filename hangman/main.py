import random
from hangman_art import stages, logo
from hangman_words import word_list
from clearout import clear

print(f"Welcome to \n{logo}")

chosen_word = random.choice(word_list)

lives = 6

#Testing code
print(f"ooho, the solution is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
print(display)

end_of_game = False
while not end_of_game:
    guess = input("guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already guessed the letter {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter} \n Guessed letter: {guess}")

        if guess == letter:
            display[position] = letter
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        
        print(f"you've guessed {guess}, that's not in the word. \n You lose a life")
        print(stages[lives])

        if lives == 0:
            end_of_game = True
            print('You lose')
            print(f"ooho, the solution is {chosen_word}")
        elif lives == 1:
            print(f"Be careful!! You have {lives} live remaining")
        elif lives < 3:
            print(f"Be careful!! You have {lives} lives remaining")
        else:
            print(f"you have {lives} lives remaining")


    if '_' not in display:
        end_of_game = True
        print('You win')