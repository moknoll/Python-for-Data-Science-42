import sys

if len(sys.argv) == 1:
    pass

elif len(sys.argv) > 2:
    raise AssertionError("more than one argument is provided")

else:
    try:
        number = int(sys.argv[1])

        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except ValueError:
        # raise AssertionError("argument is not an integer")
        print("AssertionError: argument is not an integer")