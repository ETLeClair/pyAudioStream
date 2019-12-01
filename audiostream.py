import os
import glob
from playsound import playsound
from random import randint
import eyed3
from pydub import AudioSegment
import sys

#Initialize configs and global vars
song_table = {}
headless_bool = 0

f = open("configs.txt", "r")
configs = {}
for lines in f:
    k, v =   lines.split(":")
    configs[k.strip()] = v.strip()


#build songtable dictionary object
def build():
    global song_table
    global headless_bool

    #Use Glob to get target directory then iterate into dict.

    loc = configs["sound_library"]
    #Check main and child directories for mp3s
    song_list = glob.glob(loc + "**/*.mp3", recursive=True)
    counter = 0 
    for songs in song_list:
        if songs not in song_table.keys():
            song_table[songs] = counter
            counter += 1
    
    print("Song Dictiory Object has been built")
    #Check to see if headless mode is being run
    if headless_bool == 1:
        return(0)
    else:
        menu()

def play():
    global song_table
    
    #Initialize Bool + song/key lists to allow songs to be played
    play_bool = True
    key_list = list(song_table.keys())
    val_list = list(song_table.values())
    print("Starting Local Audio Stream")
    #get length of current soung_table
    st_length = len(song_table)
    
    while play_bool == True:
        #Get key as songs are stored as keys with glob implmentation
        song = key_list[val_list.index(randint(0,st_length-1))]
        #Create stream
        dst = 'Stream.mp3'
        sound = AudioSegment.from_mp3(song)
        sound.export(dst, format="mp3")
        playsound('Stream.mp3')
    menu()
    #Play Local audio stream


def main():
    global headless_bool
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "headless":
            headless_bool = 1
            build()
            play()
        else:
            menu()
    else:
        menu()
    #Check to see if headless param was run


def menu():
    global song_table
    menu_bool = 1
    while menu_bool == 1:
        try:
            print("1: Create new stream \n 2: Rebuild songtable \n 3: Exit")
            inp = input("Choose your option: ")
            val = int(inp)
        except ValueError:
            print("Invalid input")
            continue
        if int(val) == 1:
            play()
            menu_bool = 0
        if int(val) == 2:
            build()
            menu_bool = 0
        if int(val) == 3:
            exit()
main()
    #Displays options on menu.
