#odd or even calculator

def bmi_calculator():
    w = float(input("Please enter your weight in kg, e.g. 85: "))
    h = float(input("Please enter your height in m, e.g 1.75: "))
    bmi = round(w/h**2)

    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif 18.5 <= bmi <25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif 25 <= bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif 30 <= bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")
    return 0

def leapyear_calculator():
    year = int(input("Please enter the year YYYY: "))
    leap = False
    if not year % 4:
        if not year % 100 and not year % 400:
            leap = True
            print("A leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Not a leap year.")
    return 0

def pizza_calculator():
    size = input("size? (S,M,L) : ").upper()
    add_pepperoni = input("pepperoni? (Y/N) : ").upper()
    extra_cheese = input("extra cheese? (Y/N) : ").upper()

    bill = 0

    if size == "S":
        bill = 15
    elif size == "M":
        bill = 20
    elif size == "L":
        bill = 25
    else:
        print("You need to insert the size first")

    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        elif size == "M" or size == "L":
            bill += 3

    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}")

    return 0

def count_true(name, n_true=None):
    n_true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
    return n_true

def count_love(name, n_love=None):
    n_love = name.count("l") + name.count("o") + name.count("v") + name.count("e")
    return n_love

def love_calculator():
    name1 = input("Your name : ").lower()
    name2 = input("Your partner name : ").lower()

    my_true = count_true(name1) + count_true(name2)
    my_love = count_love(name1) + count_love(name2)

    score = int(str(my_true) + str(my_love))

    if score <= 10 or score >= 90:
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif 40 <= score <=50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}, cool.")

    return 0


love_calculator()
#pizza_calculator()
#leapyear_calculator()
#bmi_calculator()