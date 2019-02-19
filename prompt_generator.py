#Reed's Prompt Generator v1.0
#Generate a prompt for writing a story
import random
import time

def scene(data):
    action = ("runs from","hides from","is chased by","is dancing with","is about to be eaten by","got sat on by","is chasing","is hunted by","is partying with","is meeting up with","is trying to find")
    situation = ("and tries to get laid","while shrinking","while growing","and tries to get unshrunk","during sex")
    location =  ("at a taco truck","at a friends' house","at an ice cream shop","at a burger place","in the forest","at the beach","at the mall","at the park","at a campout","at a family get-together","at the amusement park","at the carnival")
    act = str()
    sit = str()
    loc = str()

    act = action[random.randint(0,10)]
    sit = situation[random.randint(0,4)]
    loc = location[random.randint(0,11)]

    data = (act,sit,loc)
    return data

def char(actor):
    letters = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z")
    vowels = ("a","e","i","o","u","y",)
    creatures = ("dog","cat","horse","dragon","fox","tiger","donkey","rhino","elephant","lion","cheetah","lizard","raccoon","mouse","gazelle","giraffe","zebra")
    gender = ("male","female")

    species = str()
    name = str()
    length = int()
    count = int()
    glyph = str()
    sag = str()
    finalName = str()

    length = random.randint(2,3)
    while length != count:
        glyph = letters[random.randint(0,19)]
        name = name + glyph
        glyph = vowels[random.randint(0,5)]
        name = name + glyph
        species = creatures[random.randint(0,16)]
        sag = gender[random.randint(0,1)]
        count = count + 1
    #finalName is generated species first, then the, then name.
    finalName = " " + species + finalName
    finalName = " the " + sag + finalName
    finalName = name + finalName

    actor = finalName
    return actor

def exe():#does the cross function work and prints everything
    c1 = str()
    c2 = str()
    c1 = char(c1)
    c2 = char(c2)
    info = str()
    info = scene(info)
    fin = str()

    fin = c1 +" "+ info[0] +" "+ c2 +" "+ info[1] +" "+ info[2]
    print(fin)
    file = open("prompt.txt","w")
    file.write(fin)
    file.close
    


def main():#runs exe() in a loop. Export prompts to a file
    choice = str()
    while choice != "no":
        exe()
        choice = input("\nContinue?\nType no to quit and reset the text file\n")
        if choice == "no":
            file = open("prompt.txt","w")
            file.write("")
            file.close
            break
        else:
            print("Generating a new prompt")
            time.sleep(2)
            print("Please Wait\n")
            time.sleep(2)

    
main()
