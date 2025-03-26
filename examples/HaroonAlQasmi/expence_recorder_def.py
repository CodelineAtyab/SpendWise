from datetime import datetime
import hashlib
import os
import csv

expenses_file = "expenses.csv"
hash_file = "hashes.csv"
expenses_dictionary = {}
hash_dictionary = {}


def compute_csv_hash(filename):
    try:
        with open(filename, 'rb') as f:
            file_contents = f.read()
        return hashlib.sha256(file_contents).hexdigest()
    except Exception as e:
        print(f"Error computing hash: {e}")
        return None

def load_saved_hash():
    if not os.path.exists(hash_file):
        return None
    try:
        with open(hash_file, 'r', newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row.get("file") == expenses_file:
                    return row.get("hash")
    except Exception as e:
        print(f"Error loading hash: {e}")
    return None
def update_hash_file():
    new_hash = compute_csv_hash(expenses_file)
    if new_hash is None:
        return
    try:
        with open(hash_file, 'w', newline="") as csvfile:
            fieldnames = ["file", "hash"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({"file": expenses_file, "hash": new_hash})
    except Exception as e:
        print(f"Error updating hash: {e}")

def ensure_file_exists():
    if not os.path.exists(expenses_file):
        try:
            with open(expenses_file, 'w', newline="") as csvfile:
                fieldnames = ["customer_contact", "customer_name", "amount","date_time"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
        except Exception as e:
            print(f"Error creating file: {e}")

def add_expense():
    try:
        expence = input("Enter the amount: ")
        customer_name = input("Enter the customer name: ")
        customer_contact = input("Enter the customer contact: ")
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(expenses_file, 'a', newline="") as csvfile:
            fieldnames = ["customer_contact", "customer_name", "amount","date_time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"customer_contact": customer_contact, "customer_name": customer_name, "amount": expence,"date_time":date_time})
        print(f"Expense added with ID: {customer_contact}")
    except Exception as e:
        print(f"Error adding expense: {e}")

def view_expenses():
    try:
        with open(expenses_file, 'r', newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
    except Exception as e:
        print(f"Error viewing expenses: {e}")

def update_expense():
    try:
        customer_contact = input("Enter the customer contact: ")
        updated_expense = input("Enter the updated amount: ")
        updated_customer_name = input("Enter the updated customer name: ")
        updated_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated = False
        with open(expenses_file, 'r', newline="") as csvfile:
            reader = list(csv.DictReader(csvfile))
        for row in reader:
            if row["customer_contact"] == customer_contact:
                row["amount"] = updated_expense
                row["customer_name"] = updated_customer_name
                row["date_time"] = updated_date_time
                updated = True
        if not updated:
            print("Expense not found.")
            return
        with open(expenses_file, 'w', newline="") as csvfile:
            fieldnames = ["customer_contact", "customer_name", "amount","date_time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(reader)
        print(f"Expense updated with ID: {customer_contact}")
    except Exception as e:
        print(f"Error updating expense: {e}")

def remove_expense():
    try:
        customer_contact = input("Enter the customer contact: ")
        removed = False
        with open(expenses_file, 'r', newline="") as csvfile:
            reader = list(csv.DictReader(csvfile))
        new_rows = [row for row in reader if row["customer_contact"] != customer_contact]
        if len(new_rows) != len(reader):
            removed = True
        if not removed:
            print("Expense not found.")
            return
        with open(expenses_file, 'w', newline="") as csvfile:
            fieldnames = ["customer_contact", "customer_name", "amount","date_time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_rows)
        print(f"Expense removed with ID: {customer_contact}")
    except Exception as e:
        print(f"Error removing expense: {e}")
