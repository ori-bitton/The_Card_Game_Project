from time import sleep


class Loading:

    def __init__(self, time):
        global str1
        print("Loading", end="")
        str1 = ""
        for i in range(2*time):
            str1 += '.'
        for i in str1:
            print(i, end="")
            sleep(0.5)
        print("\n")