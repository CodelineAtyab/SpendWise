import time

input_seconds = int(input("Enter the number of seconds for the countdown:"))
if input_seconds <= 0:
    print("Please enter a positive number")
else:
    for i in range(input_seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Time's up!")
