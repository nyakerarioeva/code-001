import time

def countdown(s):
    while s:
        mins,secs = divmod(s, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print (timer, end="\r")
        time.sleep(1)
        s -=1
    print("Happy Monday")
s = input("Enter the time in seconds: ")
countdown(int(s))