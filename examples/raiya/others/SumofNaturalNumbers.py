
num=int(input("Enter a number: "))
if num<=0:
    print("Please enter a positive number")

elif num == "abcdefghijklmnopqrstuvwxyz":
    print("Please enter a valid number")
    exit()

else:
    sum=0
    for i in range(1,num+1):
        sum+=i
    print("The sum of the first",num,"natural numbers is",sum)

        