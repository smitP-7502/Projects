from Make_Playlist import Playlist


def Search_Play():
    i = 0
    List = []

    while i == 0:
        c = 0
        Search = input("Enter the song name : ")
        temp = Search.capitalize()

        f = open("Text Files/Music.txt")
        print("----------------------------: Song Found :----------------------------")
        for line in f:
            if ((line.split())[1].capitalize()).removesuffix("\n").__contains__(temp):
                print(line, end="")
                c += 1
        print("------------------------------------------  ----------------------------")
        f.close()
        if c != 0:
            List = Playlist()
        else:
            print("No song found!!!!!")

        str = input("Do you wand add other songs??(y/n):")

        if str == 'n':
            i = 1
        else:
            pass

    return List

# Search_Play()
