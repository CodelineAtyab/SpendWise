user_input = int(input("Enter a number:"))
sum=0
for num in range(user_input+1):
    sum += num
print("The sum of the the first",user_input,"natural numbers is ",sum)