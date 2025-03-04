import datetime

cus_info = {}

def add(expense, currency, email):
    sys_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cus_info[email] = {'expense': expense, 'currency': currency, 'email': email, 'time': sys_time}
    print("Added Successfully!")
    print("")

def view():
    if cus_info:
        for email, info in cus_info.items():
            print(f"Expense: {info['expense']} {info['currency']}, Email: {info['email']}, Time: {info['time']}")
    else:
        print("No information available.")
    print("")

def update():
    email = input("Enter the email of the customer you want to update: ")
    if email in cus_info:
        print(f"Current information: {cus_info[email]}")
        new_expense = float(input("Enter the new amount: "))
        new_currency = input("Enter the new currency: ")
        cus_info[email]['expense'] = new_expense
        cus_info[email]['currency'] = new_currency
        sys_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cus_info[email]['time'] = sys_time
        print(f"Information updated for {email}.")
            
    else:
        print("Email not found!")
    print("")

def delete():
    email = input("Enter the email of the customer you want to delete: ")
    if email in cus_info:
        del cus_info[email]
        print(f"Information for {email} deleted successfully.")
    else:
        print("Email not found!")
    print("")

def main():
    print("1. Add your information:")   
    print("2. View information:")   
    print("3. Update information:")   
    print("4. Delete information:")   
    print("5. Exit")   

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            
            amount = float(input("Enter the amount:"))
            crr = input("Enter the currency:")
            email = input("Enter your email:")
            add(amount, crr, email)
                
           
        elif choice == "2":
            view()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()        
        elif choice == "5":
            break
        else:
            print("Invalid choice: Please try again")

main()
