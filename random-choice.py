# random-choice - A program that randomly makes your choice for you.



# TODO: make a condition on subjects that one th ing can only happen once (per day?) (still deciding if I wan to implement this).
# TODO: Make it loop
# TODO: save the things in file so that you can add functionality to delete, add, etc in the program.
# TODO: .lower the first letter in input in case (e.g. Music to music)

import random

# Genre variables
subjects = ["Physics", "Chinese", "Programming", "Computer Science", "Read descriptive fiction", "Read How To Influence Friends", "Read War and Peace", "Accounting", "Filipino reading", "Calculus", "Sell steam stickers", "Exercise", "Meditate", "Ate Kate's AMA"]
music = ["Classical", "70s", "Jazz", "Pop chill", "90s", "LOTR ambience", "Hobbit ambience", "HP ambience", "80s", "Movies", "Accousting songs playlist", "Sad pop playlsit", "60s"]

# TODO: find a better name for this.
input_dictionary = {"subjects": subjects, "music": music}

while True:
    # Asks input from the user
    user_input = str.lower(input("What genre do you want randomized (subjects, music) (stop)?: "))

    # Option to stop the program.
    if user_input == "stop":
        break
    else:
        # Shuffles list inputted (for more randomness?).
        random.shuffle(input_dictionary[user_input])

        # Randomly picks an item from the list and prints it out.
        randomized_choice = random.choice(input_dictionary[user_input])
        print(randomized_choice)

# Do you really need an else statement or can you just put an if statement? 

# FULL MENTAL FOCUS
# Mental Exhaustion
# cmd + k then cmd + i
# TODO: don't forget to check the images in the moving wallpaper in mac
# ctrl + g: search up line number.
# Make a question input putter for question when