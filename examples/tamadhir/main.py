from crud_utils import add, view, update, delete

def main():
    print("1. Add your information:")   
    print("2. View information:")   
    print("3. Update information:")   
    print("4. Delete information:")   
    print("5. Exit")   

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                amount = float(input("Enter the amount:"))
                crr = input("Enter the currency:")
                email = input("Enter your email:")
                add(amount, crr, email)
            except ValueError:
                print("Invalid input for the amount. Please enter a valid number.")
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

if __name__ == "__main__":
    main()
