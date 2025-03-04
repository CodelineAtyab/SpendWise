import time

def countdown():
    seconds = input("Enter the number of seconds for the countdown: ")
    if seconds.isdigit() and int(seconds) > 0:
        seconds = int(seconds) 
    else:
        print("Please enter a valid positive number.")
        return
    for second in range(seconds, 0, -1):
        print(second)
        time.sleep(1) 
    print("Time's up!")
countdown()
