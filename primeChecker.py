import math


# Main function for primality check.
def primalityCheck(checkPrime, optDivisor):

    # Bypass check if inputted value is 1. 1 is a special value.
    if(checkPrime == 1):
        return print(checkPrime, "is a special number! \n", sep=' ')

    else:

        # Set divisor to half of inputted value for primality check optimization.
        optDivisor = math.ceil(checkPrime / 2)

        # Loop division of inputted number by its half.
        # Immediately returns composite if inputted value has modulo 0 with     divisor.
        # Loop continues until divisor reaches 1
        while (optDivisor > 1):
            if (checkPrime % optDivisor == 0):
                return print(checkPrime, "is a composite number! \n", sep=' ')
            else:
                optDivisor -= 1

    # Return prime if loop finishes completely.
    return print(checkPrime, "is a prime number! \n", sep=' ')


def main():
    # Program continuity. Option to exit shown at end of each primality end.
    while True:

        # Ask for user input. Input is expected to be a positive integer.
        inputVal = input(
            "Enter a positive integer to be checked for primality: ")

        # Initialize divisor to 0.
        divisor = 0

        # Check if inputted value is a positive integer. If positive integer, proceed to check primality.
        # Throw error if input is not a positive integer. Ask for input again.
        try:
            checkInput = int(inputVal)
            assert checkInput > 0
            primalityCheck(checkInput, divisor)
        except:
            print("Inputted value is not a positive integer! \n")
            main()

        # Initialize program continuity checker.
        checkOther = input("Check another number [Y/n]? ")
        if checkOther == "Y" or checkOther == "y" or checkOther == "":
            continue
        else:
            print("Ending program.")
            exit()


# Call main function.
if __name__ == '__main__':
    main()
