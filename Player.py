# This take the list and play the song

from pygame import mixer
from shuffle import Shuffle


def Music_Player(List):
    # List = ["Blinding_lights.mp3","Beggin.mp3","Life_goes_on.mp3"]
    Mainlist = List
    Dublicate = []

    print("\n\n--------------------------: Functions :--------------------------")
    print(
        "name: show song name\npause: pause music\nunpause : unpause music\nnext: next music\nprevious : previous music\nshuffle on or off: enable or disable shuffle\nEnter 1 to 10: volume of music\nqueue: showing the song queue")
    print("-----------------------------------------------------------------")

    LengthOfList = len(List)
    shuffled = 0
    i = 0
    c = 0
    cout = 0
    mixer.init()
    while i != LengthOfList:
        global volume
        global button
        Played = []

        if c == 0:
            c += 1
            volume = 0.3
        else:
            if List[i] in Played:
                pass
            else:
                Played.append(List[i])

        # print(i,List,"\n\n")

        mixer.music.load("Music/" + List[i])
        print("\nPlaying " + List[i].removesuffix(".mp3") + ".....")
        mixer.music.set_volume(volume)
        mixer.music.play()

        while True:
            button = input()

            if button == "next":
                # print("Next")
                mixer.music.stop()
                mixer.music.unload()
                i += 1
                break
            elif button == "previous":
                # print("Previous")
                mixer.music.stop()
                mixer.music.unload()
                i -= 1
                break
            elif button == "pause":
                print("Song is paused")
                mixer.music.pause()
                # mixer.music.get_busy()
            elif button == "unpause":
                # print("unpause")
                mixer.music.unpause()
            elif button.isnumeric():
                # num = int(button.split(" ")[1])
                volume = float(int(button) * 0.1)
                mixer.music.set_volume(volume)
                print(f"Volume set to {button}")
            elif button == "exit":
                print("Exit from the player")
                break
            elif button == "name":
                print("Playing " + List[i].removesuffix(".mp3") + ".....")
            elif button.startswith("shuffle"):
                if button.split(" ")[1] == "on":
                    print("Shuffle is enabled")
                    if cout == 0:
                        List = Shuffle(List, Played)
                        c = 1
                        Dublicate = List
                    else:
                        List = Dublicate
                elif button.split(" ")[1] == "off":
                    print("Shuffle is disabled")
                    List = Mainlist
            elif button == "queue":
                print("\n\n--------------------------: Song Queue :--------------------------")
                for j in List:
                    if str(j) == List[i]:
                        print(f"{j} \t\t<-- Now Playing")
                    else:
                        print(j)
                print("------------------------------------------------------------------")

            else:
                print("Invalid Entry.........")


# Music_Player()
