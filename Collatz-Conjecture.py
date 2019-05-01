""""This is my take on the Collatz Conjecture

This can be used to loop over a range of numbers with memoization to find the longest collatz number

This code was inspired by a Numberphile video:
https://www.youtube.com/watch?v=5mFpVDpKX70
"""
import sys

known_length = dict()  # Creates a dict to store calculated values
sys.setrecursionlimit(400)  # Increases the recursive depth to handle bigger numbers


def collatz(a):  # Collatz-Function
    global known_length  # Saves it in the gloabal variable to have it stored during the programm runntime
    if (a == 1):  # Brake condition
        return 0
    if a not in known_length:  # Checks if value is already known
        if (a % 2 == 0):
            known_length[a] = 1 + collatz(
                a // 2)  # 1+ because every collatz series is bigger by one from the next number
            return known_length[a]
        elif (a % 2 != 0):
            known_length[a] = 1 + collatz(3 * a + 1)
            return known_length[a]

    return known_length[a]  # Returns if value is in the dict


def enter_positive_numeric(thing):
    try:
        n = int(input(f"Enter a positive {thing}"))
        if (n <= 0):
            print("You entered a negative value.")
            return enter_positive_numeric(thing)
        return n
    except:
        print("You entered an invalid character. Please enter again")
        return enter_positive_numeric(thing)


while (True):
    start = enter_positive_numeric("Starting value")
    end = enter_positive_numeric("Ending value")
    if (start <= end):
        break
    print("Your starting value was smaller than or equal the ending value")

for i in range(start, end + 1):
    collatz(i)

longest_collatz = max(known_length, key=known_length.get)

print(f"The longest collatz number in your series is {longest_collatz} with length {known_length[longest_collatz]}")
