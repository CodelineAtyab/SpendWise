import datetime

cus_info = {}

def add(expense, currency, email):
    sys_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if email in cus_info:
        cus_info[email].append({'expense': expense, 'currency': currency, 'email': email, 'time': sys_time})
    else:
        cus_info[email] = [{'expense': expense, 'currency': currency, 'email': email, 'time': sys_time}]
    print("Added Successfully!")
    print("")

def view():
    if cus_info:
        for email, info_list in cus_info.items():
            for info in info_list:
                print(f"Expense: {info['expense']} {info['currency']}, Email: {info['email']}, Time: {info['time']}")
    else:
        print("No information available.")
    print("")

def update(email):
    if email in cus_info:
        print(f"Current records for {email}: {cus_info[email]}")
    
        record_index = int(input(f"Enter the record number to update (1 to {len(cus_info[email])}): ")) - 1
        if 0 <= record_index < len(cus_info[email]):
                new_expense = float(input("Enter the new amount: "))
                new_currency = input("Enter the new currency: ")
                sys_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cus_info[email][record_index] = {
                    'expense': new_expense,
                    'currency': new_currency,
                    'email': email,
                    'time': sys_time
                }
                print(f"Information updated for {email}, record {record_index + 1}.")
        else:
                print("Invalid record number!")
        
        print("Email not found!")
    print("")

def delete(email):
    if email in cus_info:
        print(f"Current records for {email}: {cus_info[email]}")
        record_index = int(input(f"Enter the record number to delete (1 to {len(cus_info[email])}): ")) - 1
        if 0 <= record_index < len(cus_info[email]):
                confirmation = input(f"Are you sure you want to delete record {record_index + 1}? (yes/no): ").lower()
                if confirmation == "yes":
                    del cus_info[email][record_index]
                    print(f"Record {record_index + 1} for {email} deleted successfully.")
                else:
                    print("Deletion canceled.")
        else:
                print("Invalid record number!")
    else:
        print("Email not found!")
    print("")
 