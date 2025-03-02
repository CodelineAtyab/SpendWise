given_amount = float(input("Enter the amount: "))

if given_amount > 0:
    with open("expenses.txt", "a") as file:
        file.write(f"{given_amount}\n")
    print("Amount Stored in a file.")

print(f'The amount is {given_amount}')