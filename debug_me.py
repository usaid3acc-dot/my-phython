total = 0
count = 0
while count < 3:
    number = int(input("Enter a number: "))
    total = total + number
    count = count + 1
print("Average:", total / count)