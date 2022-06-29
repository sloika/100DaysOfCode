import numpy as np
import time
import random
import string

def height_avg():
    #get the input
    heights = input("Please insert the list of heights separated by a single space").split()
    #change it to int
    int_heights = [int(x) for x in heights]
    #get to np array
    arr_heights = np.array(int_heights)
    avg = np.sum(arr_heights)/len(arr_heights)
    print(f"Avg height of the students is : {avg}")
    print(f"Tallest height is : {np.amax(arr_heights)}")

    return 0

def fizzbuzz():
    limit = int(input("Please specify the end number for fizbuzz calculation : "))
    arr = np.arange(1,limit+1)

    start = time.perf_counter()

    for n in arr:
        if not n % 5 and not n % 3:
            print("FizzBuzz!")
        elif not n % 3:
            print("Fizz")
        elif not n % 5:
            print("Buzz")
        else:
            print(n)

    end = time.perf_counter()
    print(f"Execution time : {end-start}")

    return 0

def pass_gen():
    #length = input("How many digits of passwords? ")
    n_letters = int(input("How many letters? "))
    n_symbols = int(input("How many symbols? "))
    n_numbers = int(input("How many numbers? "))

    letters = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(n_letters))
    symbols = ''.join(random.SystemRandom().choice(string.punctuation) for _ in range(n_symbols))
    numbers = ''.join(random.SystemRandom().choice(string.digits) for _ in range(n_numbers))

    chars = letters+symbols+numbers

    pwd = ''.join(random.sample(chars, len(chars)))

    print(f"Here is your new password : {pwd}")

    return pwd


pass_gen()



#fizzbuzz()
#height_avg()

#0.00021635100711137056
#0.00024015000963117927
