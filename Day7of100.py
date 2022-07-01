from random_word import RandomWords


def hangman_game():
    print(logo)
    r = RandomWords()

    chosen_word = ""
    while not chosen_word:
        chosen_word = r.get_random_word(hasDictionaryDef="true", minLength=4, maxLength=8)

    chosen_word_list = list(chosen_word.lower())
    blanks = "_" * len(chosen_word)

    counter = 0
    stages.reverse()
    print(f"Word : {blanks}")
    print(stages[counter])

    end_of_game = False

    while not end_of_game:
        guess = input("Please enter a letter of your guess : ").lower()
        blanks_list = list(blanks)
        found = False
        for index, elem in enumerate(chosen_word_list):
            if guess == elem:
                found = True
                blanks_list[index] = guess
                blanks = "".join(blanks_list)

        if not found:
            counter += 1
            print(counter)

        print(f"Word : {blanks}")

        if counter >= len(stages) - 1:
            end_of_game = True
            print(stages[counter])
            print("You are dead")
            print(f"The right word is : '{chosen_word}'")
        elif "_" not in blanks:
            end_of_game = True
            print(stages[counter])
            print("Congrats, you are avoiding being hanged!")
        else:
            print(stages[counter])

        print("##############################################")

    return 0


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

hangman_game()
