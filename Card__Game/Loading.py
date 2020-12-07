from time import sleep


class Loading:

    def __init__(self, time):
        print("Loading", end="")
        str1 = ""
        for i in range(2*time):
            str1 += '.'
        for i in str1:
            print(i, end="")
            sleep(0.5)
        print("\n")

    def playing(self, time):
        print("Playing", end="")
        str1 = ""
        for i in range(2 * time):
            str1 += '.'
        for i in str1:
            print(i, end="")
            sleep(0.5)
        print("\n")
