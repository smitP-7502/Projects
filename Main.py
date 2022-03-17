import time
import Make_Playlist
import shuffle
from Random_play import Play_suf
from Song_Loader import load_songs
from Player import Music_Player
from Search import Search_Play
import os


if __name__ == "__main__":
    os.system("cls")
    load_songs()

    while True:
        os.system("cls")
        print("\n\n----------------------: Home Page :----------------------")
        print("1. Make Playlist")
        print("2. Search and Play")
        print("3. Play shuffle ")
        print("4. Exit from the Player")
        print("---------------------------------------------------------")
        n = int(input("Enter the number : "))

        if n == 1:
            os.system("cls")
            # print("Make Playlist")
            print("\n\n")
            Make_Playlist.Show_song()
            List = Make_Playlist.Playlist()
            os.system("cls")
            Music_Player(List)
        elif n == 2:
            os.system("cls")
            # print("Search and play")
            print("\n")
            List = Search_Play()
            os.system("cls")
            Music_Player(List)
        elif n == 3:
            os.system("cls")
            # print("Play shuffle")
            List = Play_suf()
            shuffle.Shuffle(List,[])
            os.system("cls")
            Music_Player(List)
        elif n == 4:
            print("Exit form the Player")
            exit()
        else:
            print("Invalid Entry...")


