import time
s=int(input("Enter a time: "))
while s:
    mins= s//60
    secs=s%60
    timer=f'{mins:02d}:{secs:02d}'
    print(timer, end='\r')
    time.sleep(1)
    s -= 1

print("Time's up!")