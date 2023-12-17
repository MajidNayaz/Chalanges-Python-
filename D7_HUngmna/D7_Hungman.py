#this program choses a random word and say to you that how many characters doese it have and your task is 
#to guess the characters if it was true it will help a man other wise you kill the man 

import random
import hungman_logo
import hungman_words

random_word = random.choice(hungman_words.dictionary)

display = []

for char in random_word:
    display += '_'



lives = 0

print(hungman_logo.hungman_logo)

print(f"{' '.join(display)}")

end_game = False

while end_game == False:

    print(hungman_logo.stages[lives])

    guess = input("Guess the character \n").lower()
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter 
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_game = True
        print("You Win!")
    
    if guess not in random_word:
        lives += 1
        print(f"{guess} is not in the word and you have losed one live")
        if lives == 7:
            end_game = True
            print("You lose!")