import time
program_on = True
while program_on:
    user_input=input("Enter number of seconds for the countdown:")
    if user_input.isdigit():
        for num in range(int(user_input)):
            time.sleep(1)
            print(num +1)
        program_on = False
    else:
        print("wrong input")