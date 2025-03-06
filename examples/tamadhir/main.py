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
            amount = float(input("Enter the amount:"))
            crr = input("Enter the currency:")
            email = input("Enter your email:")
            add(amount, crr, email)    
        elif choice == "2":
            view()
        elif choice == "3":
            email = input("Enter the email of the customer you want to update: ")
            update(email)  
        elif choice == "4":
            email = input("Enter the email of the customer you want to delete: ")
            delete(email)  
        elif choice == "5":
            break
        else:
            print("Invalid choice: Please try again")

if __name__ == "__main__":
    main()
