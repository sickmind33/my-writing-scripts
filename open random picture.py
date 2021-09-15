import os
import random
dir = r"C:\Users\Owner\Pictures\porn\PokemonSnapXXXL"

thenumber = int(input("How many files are in the folder? "))

thenumber = thenumber - 1

files = ( next( os.walk(dir) )[2] )

testfile = files[random.randint(0,thenumber)]

pane = dir + "\\"

pane = pane + testfile

os.startfile(pane)
