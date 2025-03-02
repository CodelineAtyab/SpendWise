import time
count_time = float(input("Enter the number of seconds for the countdown:"))


while count_time  > 0:
    
    print(count_time) 
    time.sleep(1)
    count_time -= 1 
if count_time == 0:
       print("times up!!")
                
else:
    print("invalid input")
     
       


 

 