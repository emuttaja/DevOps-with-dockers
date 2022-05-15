"""
Something goofy to rustle your jimmies.

"""

def odd(x):
    """ Check if an integer is odd.

    :param x: int, an integer to be examined
    :return: bool, True if x is odd
    """
    if x < 0:
        return odd(x**2)
    elif x == 1:
        return True
    elif x == 0:
        return False
    else:
        return odd(x-2)


def main():
    user_in = ""
    try:
        user_in = int(input("Please provide a number: "))
    except:
        print(f"Please provide a number instead of whatever nonsense that was")
        return
    try:
        if odd(user_in):
            print("Congratulations! The number provided is odd!")
        else:
            print("What a shame. The number provided is even.")
    except RecursionError:
        print("Too many recursions!! Try a smaller number next time.")
        return



if __name__ == "__main__":
    main()
