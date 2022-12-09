from datetime import datetime
import time
import random
'''for i in range(1,11):
    print(i,".","I AM THE BEST", end=" ")
    
for i in "hi!":
    print(i,"-")'''
odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

for i in range(6):
    right_this_minute = datetime.today().minute
    if right_this_minute in odd:
        print("This time is seem odd")
    else:
        print("not an odd minute")
    wait_time = random.randint(1,5)
    time.sleep(wait_time)