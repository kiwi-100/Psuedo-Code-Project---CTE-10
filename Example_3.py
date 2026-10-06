# corresponds colors to numbers

num = int(input("Enter a number: "))
if 0 <= num <= 10:
    print("blue")
elif 10 <= num <= 20:
    print("red")
elif 20 < num <= 30:
    print("green")
else:
    print("Number out of range")
