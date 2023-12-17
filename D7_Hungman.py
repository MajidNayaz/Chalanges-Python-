#this program choses a random word and say to you that how many characters doese it have and your task is 
#to guess the characters if it was true it will help a man other wise you kill the man 

import random

dictionary = ["door", "computer", "mouse", "afghanistan", "university"]
random_word = random.choice(dictionary)

display = []

for char in random_word:
    display += '_'

stages = ['''
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

lives = 0

print(f"{' '.join(display)}")

end_game = False

while end_game == False:

    print(stages[lives])

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
        if lives == 7:
            end_game = True
            print("You lose!")