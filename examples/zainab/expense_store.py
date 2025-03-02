import time

# Validate user input to ensure it's a positive number
while True:
    try:
        count_time = float(input("Enter the number of seconds for the countdown: "))
        if count_time <= 0:
            print("Please enter a positive number greater than zero.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Countdown logic
while count_time > 0:
    print(int(count_time))  # Display countdown as integer
    time.sleep(1)  # Wait for 1 second
    count_time -= 1

print("Time's up!!")
