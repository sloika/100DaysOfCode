import datetime

# Pull individual char
# print("Hello"[0])
# street_name = "Abbey Road"
# print(street_name[4] + street_name[7])

'''
#f-string
a = 12
b = 1.6
isGood = True
print(f"Your score is {a}, your height is {b}m, and your winning is {isGood}")
'''


def bill_splitter():
    print("Welcome to the tip calculator")
    bill = float(input("What was the total bill? $"))
    people = float(input("How many people to split the bill? "))
    tip = float(input("What percentage tip would you like to give? "))
    bill_after_tip = tip / 100 * bill + bill
    bill_per_person = bill_after_tip / people
    return bill_per_person


def number_adder():
    print("Welcome to the number adder. It will add all the digits in the input")
    num = input("Please input the number: ")
    print("It consists of : ")
    total = 0
    minus = False
    for x in num:
        if x == "-":
            minus = True
            continue
        elif minus:
            total += float(x) * -1
            minus = False
            print(total)
        else:
            total += float(x)
            print(x)

    return total


def time_left_till_90(current_age: int):
    # assert isinstance(current_age, object)
    years_left = 90 - current_age
    days_left = years_left * 365
    months_left = years_left * 12
    print(f"You have {years_left} years or {months_left} months or {days_left} days till you are 90 years old")
    return 0


def time_left_till_90_v2():
    # missing the leap years. Need more thinking
    date_entry = input("Enter your birthday in YYYY-MM-DD format")
    year, month, day = map(int, date_entry.split('-'))
    birthdate = datetime.date(year, month, day)
    delta_date = datetime.date.today() - birthdate
    print("You are {0} years, {1} months, {2} days old today".format(delta_date.years, delta_date.months,
                                                                     delta_date.days))
    return 0


# 1991-05-04
time_left_till_90_v2()

# total = number_adder()
# print("Total addition = {0}".format(total))

# per_person = bill_splitter()
# print("Each person should pay: ${0}".format(per_person))

# number_adder()
