from os import system


class DaysinMonth(object):
    def __init__(self):
        print("Welcome to the day-in-the-month calculator.")

    @staticmethod
    def number_of_days(year: int, month: int):
        """It will take the year and month and return the number of days of the month"""
        leap = 0
        print(f"The year is {year} and month {month}")
        if not year % 4:
            if not year % 100 and not year % 400:
                leap = 1

        month_with_30: [4, 6, 9, 11]

        if month == 2:
            return 28 + leap
        elif month in month_with_30:
            return 30
        else:
            return 31


def add_num(a: float, b: float):
    return a + b


def subtract_num(a: float, b: float):
    return a - b


def divide_num(a: float, b: float):
    return a / b


def multiply_num(a: float, b: float):
    return a * b


operation = {
    "+": add_num,
    "-": subtract_num,
    "/": divide_num,
    "*": multiply_num
}


# days = daysInMonth().number_of_days(2020,2)
# print(f"It has {days} days")

def calculator():
    is_done = False
    num_1 = float(input("Please insert the first number"))

    while not is_done:
        operator = input("Please insert one operator (+ - * /)")
        num_2 = float(input("Please insert the second number"))

        if operator in operation:
            calculation_function = operation[operator]
        else:
            print("Illegal operation, please retry")
            calculator()

        answer = calculation_function(num_1, num_2)

        next_step = input(f"Type 'y' to do another operation to the current answer: {answer},\n"
                          "Type 'n' to make a new calculation, or\n"
                          "Type 'nn' to quit.\n").lower()
        system("clear")
        if next_step == "y":
            num_1 = answer
        elif next_step == "n":
            calculator()
        elif next_step == "nn":
            is_done = True


calculator()
