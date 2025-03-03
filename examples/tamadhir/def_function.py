cus_info = {}

def add(id, expense, currency, email):
    cus_info[id] = {'expense': expense, 'currency': currency, 'email': email}
    print("Added Successfully!")
    print("")

def view():
    if cus_info:
        for id, info in cus_info.items():
            print(f"ID: {id}, Expense: {info['expense']} {info['currency']}, Email: {info['email']}")
    else:
        print("No information available.")
    print("")

def main():
    print("1. Add your information:")   
    print("2. View information:")   
    print("3. Exit")   

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            id = int(input("Enter your ID:"))
            amount = float(input("Enter the amount:"))
            crr = input("Enter the currency:")
            email = input("Enter your email:")
            add(id, amount, crr, email)
        elif choice == "2":
            view()
        elif choice == "3":
            break
        else: 
            print("Invalid choice: Please try again")


main()
