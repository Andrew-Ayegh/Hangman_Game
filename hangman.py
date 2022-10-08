import random 
import arts 
from words import word_list, animals, countries, cars

#picking a word for the game from the module's list
chosen_word = random.choice(word_list)
print(chosen_word)

# empty spaces in the word 
dash =[]

#life of player
life = 6

#determinant of game end
end_of_game = False

word_length = len(chosen_word)

#printing the number of letters teh word has
for _ in range(word_length):
    dash += "_"

#Body of the Game
while not end_of_game:
    guess = input("guess a letter: ").title()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            dash[position] = letter
    print(dash)
    if"_" not in dash:
        end_of_game = True    
