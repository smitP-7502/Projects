import time
import Make_Playlist
from Song_Loader import load_songs
from Player import Music_Player
import Search


if __name__ == "__main__":
    load_songs()

    while True:
        print("Enter the number")
        print("1. Make Playlist")
        print("2. Search and Play")
        print("3. Play shuffle ")
        print("4. Exit from the Player")
        n = int(input("Enter the number : "))

        if n == 1:
            print("Make Playlist")
            Make_Playlist.Show_song()
            List = Make_Playlist.Playlist()
            Music_Player(List)
        elif n == 2:
            print("Search and play")
            List = Search.Search_Play()
            Music_Player(List)
        elif n == 3:
            print("Play shuffle")
        elif n == 4:
            print("Exit form the Player")
        else:
            exit()


