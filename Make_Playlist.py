def Show_song():
    f = open("Text Files/Music.txt", "r")
    print("----------------------: Song List :----------------------")
    for line in f:
        print(line, end="")
    f.close()
    print("---------------------------------------------------------")


def Playlist():
    num = input("Enter the number with space to make song playlist :")
    Num = num.split()
    Play_List = []

    for i in Num:
        f = open("Text files/Music.txt", "r")
        for line in f:
            List = line.split(" ")
            if i in List:
                Play_List.append(List[1].removesuffix('\n'))
                f.close()
                break
    # print(Play_List)
    return Play_List
