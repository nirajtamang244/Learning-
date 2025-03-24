#writing a program to ask the user for a number until they enter a valid one.
while True:
    try:
        a = float(input("Enter a numerator:\t"))
        b= float(input("Enter a denominator:\t"))
        x=a/b
    except ValueError:
        print(f"enter a valid number.")
    else:
        print(f"The result is {x}")
        break
    finally:
        print("The computation has been done.")
        