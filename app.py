import random


def main():
    num = random.randrange(0, 100)
    inputnum = enternum()

    while inputnum != num:
        if num > inputnum:
            print("Too small!")
            inputnum = int(input("Please enter a number again: "))
        elif num < inputnum:
            print("Too big!")
            inputnum = int(input("Please enter a number again: "))
    print("good!")


def enternum():
    num1 = int(input("Please enter a number between 0 to 100: "))
    #let user to select range in the future.
    return num1

main()