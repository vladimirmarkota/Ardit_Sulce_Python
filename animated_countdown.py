import time
import os
import winsound

def clear_screen():
    os.system("cls")

def beep():
    winsound.Beep(1000, 500)

my_time = int(input("Enter your time: "))

for x in range(my_time, 0, -1):
    clear_screen()
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = (x // 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

beep()
print("Time's up")
