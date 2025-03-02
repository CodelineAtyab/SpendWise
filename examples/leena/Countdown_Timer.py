#Countdown Timer
import time

print("Welcome to the Countdown Timer!\n")
time_countdown = input("Enter the number of seconds for the countdown:")
if time_countdown.isdigit() == False:
    print("Please enter a valid number.")
    exit()

for i in range(int(time_countdown), 0, -1):
    print(i)
    time.sleep(1)
print("\nTime's up!")