import time

i = 0

while True:
    print("Hello\n")
    time.sleep(i)
    i = i + 1
    if i > 3:
        break
print("End of loop")

