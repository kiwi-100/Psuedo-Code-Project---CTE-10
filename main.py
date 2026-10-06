# mega selection menu

import runpy

programs = {
    "1": "Example_1.py",
    "2": "Example_2.py",
    "3": "Example_3.py",
    "4": "Example_4.py",
    "5": "Example_5.py",
    "6": "Example_6.py",
    "7": "Homework_1.py",
    "8": "Homework_2.py",
}

while True:
    print("\n--- Mega Menu ---")
    for key, name, in programs.items():
        print(key + ". " + name)
    print("0. Quit")
    print()

    choice = input("Pick a program: ")
    if choice == "0":
        break
    elif choice in programs:
        print()
        runpy.run_path(programs[choice])
    else:
        print()
        print("Error Code 2. " \
        "User is stupid and can't type or read. " \
        "Or possibly both.")
        input("Press Enter to try again...")
