import time                                     # 1
import os                                       # 2
import winsound                                 # 3

def clear_screen():                             # 4
    os.system("cls")                            # 5

def beep():                                     # 6
    winsound.Beep(900, 600)                     # 7  # frekvencija 900 Hz, trajanje 600 ms

def format_hms(seconds_total):                  # 8
    hours = seconds_total // 3600               # 9
    minutes = (seconds_total % 3600) // 60      # 10
    seconds = seconds_total % 60                # 11
    return f"{hours:02}:{minutes:02}:{seconds:02}"  # 12

def progress_bar(elapsed, total, length=40):    # 13
    if total == 0:                              # 14
        filled = length                         # 15
    else:                                       # 16
        filled = int((elapsed / total) * length)# 17
    bar = "█" * filled + "-" * (length - filled)# 18
    percent = int((elapsed / total) * 100) if total != 0 else 100  # 19
    return f"[{bar}] {percent:3d}%"             # 20

def main():                                     # 21
    try:                                        # 22
        my_time = int(input("Enter seconds: "))# 23
        if my_time < 0:                         # 24
            raise ValueError("Negative time")   # 25
    except ValueError:                          # 26
        print("Please enter a non-negative integer.") # 27
        return                                  # 28

    start = 0                                   # 29
    for elapsed in range(start, my_time + 1):   # 30
        remaining = my_time - elapsed           # 31

        clear_screen()                          # 32

        # ispis vremena
        print(format_hms(remaining))            # 33

        # ispis progress bara
        print(progress_bar(elapsed, my_time))  # 34

        # kratka pauza (da se vidi svaki korak)
        time.sleep(1)                           # 35

    beep()                                      # 36
    print("Time's up!")                         # 37

if __name__ == "__main__":                      # 38
    main()                                     # 39
