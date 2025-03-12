print("ramadan mubark all ")

import time


num = float(input("Enter the number of seconds for the countdown:"))


def countdown(seconds):
    while seconds > 0:
        print(f"{seconds:.1f}")
        time.sleep(1)
        seconds -= 1

    print("0.0")
    print("Time's up!")

countdown(num)