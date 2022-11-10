import random 
from arts import welcome_message, stages
from words import word_list, animals, countries, cars

print(welcome_message)



end = False
while not end:
    #picking a word for the game from the module's list
    chosen_word = random.choice(word_list)
    # empty spaces in the word 
    dash =[]

    #life of player
    live = 6


    word_length = len(chosen_word)

    #printing the number of letters the word has
    for _ in range(word_length):
        dash += "_"
    
    
    # determinant of game termination
    end_of_game = False

    while not end_of_game:
        if chosen_word in animals:
            print("The word is the name of an ANIMAL\n")
        elif chosen_word in countries:
            print("The word is the name of a COUNTRY \n")
        elif chosen_word in cars:
            print("The word is the name of a CAR-BRAND")
        
        print(stages[live])
        
        print(" ".join(dash))
        guess = input("guess a letter: ").lower()
        
        if guess in dash:
            print(f"you have guessed *{guess}* already ")
            
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                dash[position] = letter
        
        
        # print(" ".join(dash),"\n")
        if guess not in chosen_word:
            live -= 1
            if live == 1:
                print(f"you have {live} live left")
            else:
                print(f"you have {live} lives left")
            
            if live == 0:
                end_of_game = True
                print(chosen_word)
                print("you lose 😥💔")
                print(stages[live])
        
        if"_" not in dash:
            end_of_game = True
            print(f"you win 🌟🌟🌟🌟🌟 \n\nWord is {(''.join(dash)).upper()}")
    
    game_end = input("do you still wish to play again?(yes/no)  ").lower()
    if game_end == "yes":
        pass
    else:
        end = True
        print("See you next time 😉")
        
