import math


def main():
    # Program continuity. Option to exit shown at end of each primality end.
    while True:

        # Ask for user input. Input is expected to be a positive integer.
        input_val = input(
            "\nEnter a positive integer to be checked for primality: ")

        # Initialize divisor to 0.
        divisor = 0

        # Check if inputted value is a positive integer.
        # If positive integer, proceed to check primality.
        # Throw error if input is not a positive integer. Ask for input again.
        try:
            check_input = int(input_val)
            assert check_input > 0
            primality_check(check_input, divisor)
        except:
            print("Inputted value is not a positive integer! \n")
            main()

        # Initialize program continuity checker.
        check_other = input("Check another number [Y/n]? ")

        if (check_other == "Y" or
            check_other == "y" or
                check_other == ""):
            continue
        else:
            print("Ending program.")
            exit()


# Function for primality check.
def primality_check(check_prime, opt_divisor):

    # Bypass check if inputted value is 1. 1 is a special value.
    if(check_prime == 1):
        return print(check_prime, "is a special number! \n", sep=' ')

    else:
        # Set divisor to half of inputted value for primality check
        # optimization.
        opt_divisor = math.ceil(check_prime / 2)

        # Loop division of inputted number by its half.
        # Immediately returns composite if inputted value has modulo 0 with
        # divisor.
        # Loop continues until divisor reaches 1.
        while (opt_divisor > 1):
            if (check_prime % opt_divisor == 0):
                return print(check_prime, "is a composite number! \n", sep=' ')
            else:
                opt_divisor -= 1

    # Return prime if loop finishes completely.
    return print(check_prime, "is a prime number! \n", sep=' ')


# Call main function.
if __name__ == '__main__':
    main()
