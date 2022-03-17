def Play_suf():
    List = []
    f = open("Text Files/Music.txt")

    for line in f:
        List.append(line.split(" ")[1].removesuffix('\n'))

    return List


# list = Play_suf()
# print(list)
