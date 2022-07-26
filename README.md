# Project
This is CLI based Offline Music Palyer Devloped in PYthon.

# How to run it
First you have to clone or Download the this repo and then simply put all your offline songs in the **Music** Folder which is attach with this repo.
Before running this programme your system must have python interpeter installed in it. [Donwload From Here](https://www.python.org/downloads/)
Then open CMD and write ***pip install pygame*** (You can also install mannualy). 
After Installation You have to run(click) **Main.py** file and Enjoy your songs.

# Build of the project
I devided whole project in the problems and make the modules.

*1) Main.py*

Main.py file which conatain the whole code and this is the final executable programme.
Main.py contains many python file as sub-modules.

*2) Player.py*

This file is manipulate with with music. It contain many functions.
But there is a problem, If the song is ended then we have to write the function to play another music.

*3) Song_Loader.py*

Using this file, the programme will automatically detect the .mp3 file from the Music folder and put it in the Text Files/Music.txt

*4) Search.py*

This file is in in the **Player.py** to make search and play function.

*5) Play_all.py*

This file use for the function in the **Main.py** to play all the avialable songs.

*6) shuffle.py*

This file is playe the song in shuffle mode which is in **Player.py**.

*7) Make_Playlist.py*

This file is used to create the playlist of the music which is in **Main.py**.
