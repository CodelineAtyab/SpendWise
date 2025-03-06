from datetime import datetime
expenses = {}
def add_expense(email, description, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if email not in expenses:
        expenses[email] = []
    expenses[email].append({"description": description, "amount": amount, "timestamp": timestamp})
    return f"Expense added for {email}: {description} - OMR{amount} at {timestamp}"
def view_expenses(email):
    if email in expenses and expenses[email]:
        return [(index + 1, exp["description"], exp["amount"], exp["timestamp"]) for index, exp in enumerate(expenses[email])]
    return []
def update_expense(email, index, new_description, new_amount):
    if email in expenses and 0 <= index < len(expenses[email]):
        expenses[email][index]["description"] = new_description or expenses[email][index]["description"]
        expenses[email][index]["amount"] = new_amount if new_amount else expenses[email][index]["amount"]
        expenses[email][index]["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return "Expense updated successfully."
    return "Invalid selection."
def delete_expense(email, index):
    if email in expenses and 0 <= index < len(expenses[email]):
        removed = expenses[email].pop(index)
        if not expenses[email]:
            del expenses[email]  
        return f"Deleted expense: {removed['description']} - OMR{removed['amount']} (Added on: {removed['timestamp']})"
    return "Invalid selection."