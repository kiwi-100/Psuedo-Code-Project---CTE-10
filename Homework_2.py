# keeps a running total of numbers entered by the user

sum = 0

while True:
    n = int(input("Enter a number (negative to quit): "))
    
    if n < 0:
        break
    else:
        sum += n

print("Running total:", sum)