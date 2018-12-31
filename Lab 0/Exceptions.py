while True:
    try:
         x = int(input("Please enter a number: "))
         break
    except ValueError:
         print("Oops!  Th-4at was no valid number.  Try again...")

