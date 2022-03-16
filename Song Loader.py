# This program detects all the song from the Music folder and write into the Music.txt file

import subprocess as sp
import os


def load_songs():
    # If there is no Text Files exist then create it
    str = sp.getoutput("dir")
    if str.count("Text Files") != 0:
        pass
    else:
        os.system("mkdir \"Text Files\"")

    # creating the temp file to store the output of the cmd
    output = sp.getoutput("dir Music\\")
    f = open("Text Files/Temp.txt", "w")
    f.write(output)
    f.close()

    # Detecting all the mp3 file and written in the Music.txt
    F = open("Text Files/Temp.txt", "r")
    File = open("Text Files/Music.txt", "w")

    i = 0
    for line in F:
        n = line.count(".mp3")
        if n != 0:
            i += 1
            song = line[39::]  # after the index 39 the song name starts
            # song = line.split(" ").pop()
            str = f"{i} {song}"
            File.write(str)

    F.close()
    File.close()
