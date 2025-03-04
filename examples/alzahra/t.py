# Get user input for t-shirt and jeans prices
tshirt_price = float(input("Enter the price of the T-shirt: "))
jeans_price = float(input("Enter the price of the Jeans: "))

# Calculate total bill
total_bill = tshirt_price + jeans_price

# Calculate discount (20% of total bill)
discount = 0.20 * total_bill

# Calculate final amount to be paid
final_bill = total_bill - discount

# Print the results
print("Total Bill:", total_bill)
print("Discount (20%):", discount)
print("Final Bill to be Paid:", final_bill)
