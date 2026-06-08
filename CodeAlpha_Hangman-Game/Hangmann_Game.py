import random
try:
    with open("highscore.txt", "r") as file:
        data = file.read().split(",")

        high_score_name = data[0]
        high_score = int(data[1])
except:
    high_score = 0
    high_score_name = "No One"


words_easy = ["Tea" , "Pot" , "Milo" , "Dog" , "Cat" , "Bird"]
words_medium = ["Circle" , "Python" , "Intern" , "Mobile" , "Party" , "operator"]
words_difficult = ["Programming" , "Technical skills" , "Refrigerator" , "Agriculture" , "Dev Karan"]
score = 0

stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]



while True:
    print("~~~~~~~~~~~~~~ The HangMan Game ~~~~~~~~~~~~~")
    print(f"High Score: {high_score}({high_score_name})")
    print("Start The Game?")

    choice = input("(Y/N):")
    #Checking input
    if len(choice) != 1 or choice.lower() != "n" and choice.lower() != "y":
        print("Enter Valid Input(Y/N)!")
        continue
    #Start of the game 
    if choice.lower() == "y":
        lives = 6
        correct_guesses = []
        wrong_guesses = []
        print(stages[0])
        

        #Selecting Difficulty
        print("~~~~~~~~~~~~ Select Difficulty ~~~~~~~~~~~~~")
        print("1)Easy\n2)Medium\n3)Difficult")
        try:
            difficulty = int(input("Enter Difficulty Level(1-3):"))
        except ValueError:
            print("Enter Valid Number!(1-3)")
            continue
        if difficulty == 1:
            selected_word = random.choice(words_easy).lower()
            

        elif difficulty == 2:
            selected_word = random.choice(words_medium).lower()
            

        elif difficulty == 3:
            selected_word = random.choice(words_difficult).lower()
        
        else:
            print("Enter Valid value!(1-3)")
            continue
        word_length = len(selected_word)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('Computer has Selected a word!\n')

        display = []
        for char in selected_word:
            if char == " ":
                display.append(" ")
            else:
                display.append("_")
        print(" ".join(display))




        #User Input Loop
        while lives > 0 and "_" in display:
            user_letter = input("Guess Letter:").lower()
            #If the guessed letter is in selected word or guessed word
            if len(user_letter) != 1:
                print("Enter Exactly  One Letter!")
                continue
            if user_letter in correct_guesses:
                print("You have already gussed this letter!\n")
                print("Correctly Guessed letters:",','.join(correct_guesses))
                continue
            if user_letter in selected_word:
                print(f"The Letter:{user_letter} is present in the Selected Word!")
                correct_guesses.append(user_letter)
                for index , letter in enumerate(selected_word):
                    if letter == user_letter:
                        display[index] = letter
                print(" ".join(display))
                print("Correct Guesses:",','.join(correct_guesses))
                print("Wrong Guesses:",','.join(wrong_guesses))
                print(stages[6 - lives])
                print(f"You have {lives} left!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            #Letter Guessed is Wrong
            else:
                if user_letter in wrong_guesses:
                    print("You have already guessed this Letter!")
                    print("Wrong Guessed letters:",','.join(wrong_guesses))
                    continue
                print(f"The Letter:{user_letter} is not present in the Selected Word!")
                wrong_guesses.append(user_letter)
                lives -= 1
                print(" ".join(display))

                print(stages[6 - lives])
                print("Correct Guesses:",','.join(correct_guesses))
                print("Wrong Guesses:",','.join(wrong_guesses))
                print(f"You have {lives} left!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    

        #If you guessed correctly - You Win
        if "_" not in display :
            print("You Won!")
            print(f"The Word Was {''.join(display)}")
            if difficulty == 1:
                score += 1
            elif difficulty == 2:
                score += 2
            elif difficulty == 3:
                score += 3
            if score > high_score:
                user_name = input("Enter your Name: ").title()

                high_score = score
                high_score_name = user_name

                with open("highscore.txt", "w") as file:
                    file.write(f"{high_score_name},{high_score}")

                print("Your Score:",score)
                print("🎉 New High Score!")
            else:
                print("Your Score:",score)
            #You lost
        else:
            print("You Lost!\n")
            print(f"The Word Was {''.join(selected_word)}")

            print(stages[6])
            print("You Died!")
            print("Your Score:",score)
        print("Would You Like To play Again?")
        play_again = input("Y/N:").lower()
        while play_again not in ["y" , "n"]:
            play_again = input("Please enter 'y' or 'n':")
        if play_again.lower() == "n":
            print("Game Exited Successfully!\n")
            break
    else:
        print("Game Exited Successfully!\n")
        break