import time


countdown_seconds = input("Enter the number of seconds for the countdown: ")


if countdown_seconds.isdigit():
    countdown_seconds = int(countdown_seconds)
    
   
    if countdown_seconds > 0:
        for remaining_time in range(countdown_seconds, 0, -1):
            print(remaining_time)
            time.sleep(1)
            print("p!") 
        print("Time's up!")  
    else:
        print("Please enter a positive number.")
else:
    print("Invalid input! Please enter a valid number.") 