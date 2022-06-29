import random

def who_pays():
    names_string = input("Give me all the names on the table, separated by comma : \n")
    names = names_string.split(", ")

    print(f"{random.choice(names)} is going to buy us the meal today!")


def rock_paper_scissor():
    my_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors : "))
    python_choice = random.randint(0, 2)

    result = str(my_choice) + str(python_choice)

    win_lose_dict = {  # 0 = human win, 1 comp win, 2 draw
        "00": 2,
        "01": 1,
        "02": 0,
        "10": 1,
        "11": 2,
        "12": 1,
        "20": 1,
        "21": 0,
        "22": 2
    }

    if my_choice == 0:
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif my_choice == 1:
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif my_choice == 2:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
    else:
        print("You have to choose boi")

    print("And the python choose")

    if python_choice == 0:
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif python_choice == 1:
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif python_choice == 2:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

    if result in win_lose_dict:
        if win_lose_dict[result] == 0:
            print("You win! :)")
        elif win_lose_dict[result] == 1:
            print("Python win! :(")
        else:
            print("Draw... :|")

    return 0
'''
#reminder on list access
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[0][1]) #kale
'''
#rock_paper_scissor()
#who_pays()