import random
import time


def Shuffle(Playlist, Played):
    Len_Played = len(Played)
    Len_Playlist = len(Playlist) - 1
    # print(Len_Played, Len_Playlist)
    # print(rand)
    if Len_Playlist - Len_Played + 1 in [0,1]:
        return Playlist

    i = 0

    while i <= (Len_Playlist - Len_Played + 1):
        rand = random.randint(Len_Played, Len_Playlist)
        # print(rand)
        # print(Played)
        # print(Playlist)
        # time.sleep(1)
        num = Playlist[rand]
        # print(num)

        if num not in Played:
            # print("Entered")
            Played.append(Playlist[rand])
            i += 1

        if len(Played) == len(Playlist):
            break
        # i+=1=


    # print(Played)
    return Played

# List = Shuffle(["a","b","c"], ["a"])
# print(List)
