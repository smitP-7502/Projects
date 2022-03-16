# This take the list and play the song

from pygame import mixer


def Music_Player(List):
    # List = ["Blinding_lights.mp3","Beggin.mp3","Life_goes_on.mp3"]

    print("--------------------------: Functions :--------------------------")
    print(
        "name: show song name\npause: pause music\nunpause : unpause music\nnext: next music\nprevious : previous music\nEnter 1 to 10: volume of music")
    print("-----------------------------------------------------------------")

    LengthOfList = len(List)
    i = 0
    c = 0
    mixer.init()
    while i != LengthOfList:
        global volume

        if c == 0:
            c += 1
            volume = 0.3

        print("\n\n")
        mixer.music.load("Music/" + List[i])
        print("Playing " + List[i].removesuffix(".mp3") + ".....")
        mixer.music.set_volume(volume)
        mixer.music.play()

        while True:
            button = input()

            if button == "next":
                # print("Next")
                mixer.music.stop()
                # mixer.music.unload()
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
                exit()
            elif button == "name":
                print("Playing " + List[i].removesuffix(".mp3") + ".....")
            else:
                print("Invalid Entry.........")


# Music_Player()
