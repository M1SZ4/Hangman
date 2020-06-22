import random

print("H A N G M A N")
while True:
    menu_choose = input('Type "play" to play the game, "exit" to quit: ')

    if menu_choose == "play":
        word_list = ['python', 'java', 'kotlin', 'javascript']
        random_word = random.choice(word_list)
        guess = "-" * len(random_word)
        mistakes = 0
        typed_letters = []

        while mistakes < 8:
            print()
            print(guess)
            guess_letter = input("Input a letter: ")
            if len(guess_letter) == 1:
                if 'a' <= guess_letter <= 'z':
                    if guess_letter not in typed_letters:

                        if guess_letter not in random_word:
                            print("No such letter in the word")
                            mistakes += 1

                        else:
                            i = 0
                            for letter in random_word:
                                if letter == guess_letter:
                                    guess = guess[:i] + letter + guess[i + 1:]
                                i = i + 1

                        typed_letters.append(guess_letter)

                        if "-" not in guess:
                            print("You guessed the word!")
                            print("You survived!")
                            break
                    else:
                        print("You already typed this letter")
                else:
                    print("It is not an ASCII lowercase letter")
            else:
                print("You should input a single letter")

        else:
            print("You are hanged!")

    elif menu_choose == "exit":
        exit()