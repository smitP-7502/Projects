import time


if __name__ == "__main__":

    while True:
        print("Enter the number")
        print("1. Make Playlist")
        print("2. Search and Play")
        print("3. Play shuffle ")
        print("4. Exit from the Player")
        n = input("Enter the number : ")

        if n == 1:
            print("Make Playlist")
        elif n == 2:
            print("Search and play")
        elif n == 3:
            print("Play shuffle")
        elif n == 4:
            print("Exit form the Player")
        else:
            exit()


