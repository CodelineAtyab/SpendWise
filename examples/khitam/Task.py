seconds = int(input("Enter the number of seconds for the countdown: ")) 
if seconds.isdigit():
    seconds = int(seconds)
    if seconds > 0:
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
        print("p!")
        print("Time's up!")
    else:
        print("Please enter a positive number.")
else:
    print("Invalid input! Please enter a valid number.")