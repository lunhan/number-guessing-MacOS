import random


def main():
    num = random.randrange(0, 10)
    inputnum = enternum()
    if num > inputnum:
        print("Too small!")
    elif num < inputnum:
        print("Too big!")
    else:
        print("good")
    while inputnum != num:
        newinput = int(input("Please enter a number again: "))
        if num > newinput:
            print("Too small!")
        elif num < newinput:
            print("Too big!")
        else:
            print("good!")
            break #make the progarm stop

def enternum():
    num1 = int(input("Please enter a number: "))
    return num1

main()
