#Reed's Prompt Generator v1.1
#Changelog
#Updated character generator with code from new character generator for more detailed characters
#scene() has been given more story possibilities 
import random
import time

def scene(data):#creates the action, situation, and location for the prompt
    action = ("runs from","hides from","is chased by","is dancing with","is about to be eaten by","got sat on by","is chasing","is hunted by","is partying with","is meeting up with","is trying to find","is on a date with","is getting coffee with","is at the bar waiting for","is hanging out with")
    situation = ("and tries to get laid","while shrinking","while growing","and tries to get unshrunk","during sex","after waking up shrunk","after getting rapidly shrunk","when they get in a fight","after sex","while trying to climb out of some food")
    location =  ("at a taco truck","at a friends' house","at an ice cream shop","at a burger place","in the forest","at the beach","at the mall","at the park","at a campout","at a family get-together","at the amusement park","at the carnival","at a bar","at their apartment","after they both wake up in a dollhouse")
    act = str()
    sit = str()
    loc = str()

    act = action[random.randint(0,14)]
    sit = situation[random.randint(0,9)]
    loc = location[random.randint(0,14)]

    data = (act,sit,loc)
    return data

def char(actor):#generates the character. Will run twice in exe() to give two characters total

    letters = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z")
    vowels = ("a","e","i","o","u","y",)
    creatures = ("dog","cat","horse","dragon","fox","tiger","donkey","rhino","elephant","deer","lion","cheetah","lizard","raccoon","mouse","gazelle","giraffe","zebra","cougar","bunny")
    gender = ("male","female")
    boobsize = ("small","medium","large","massive")
    dicksize = ("small","medium","large","massive")
    emotions = ("happy","sad","angry","jealous","dominating","submissive","horny","hungry","tired","exhausted","excited")
    nsfw = ("yes","no")

    species = str()
    name = str()
    length = int()
    count = int()
    glyph = str()
    sag = str()
    finalName = str()
    feet = int()
    inches = int()
    height = int()
    breasts = str()
    dick = str()
    attitude = str()
    part = str()
    dirty = str()

    length = random.randint(2,3)
    dirty = nsfw[random.randint(0,1)]
    while length != count:
        glyph = letters[random.randint(0,18)]
        name = name + glyph
        glyph = vowels[random.randint(0,5)]
        name = name + glyph
        species = creatures[random.randint(0,19)]
        sag = gender[random.randint(0,1)]
        feet = random.randint(0,8)
        inches = random.randint(0,11)
        attitude = emotions[random.randint(0,10)]
        if dirty == "yes":
            if sag == "female":
                breasts = boobsize[random.randint(0,3)]
                part = " " + "with" + " " + breasts + " " + "boobs"
            else:
                dick = dicksize[random.randint(0,3)]
                part = " " + "with a" + " " + dick + " " + "dick"
        else:
            1+1

        height = " at " + str(feet) + " foot " + str(inches) + " inches"
        count = count + 1
    
        

    finalName = " " + species + finalName
    finalName = " the " + attitude + " " + sag + finalName
    finalName = name + finalName
    if dirty == "yes":
        actor = finalName + part + height
    else:
        actor = finalName + height

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
        choice = input("\nIf you wish to keep this prompt, exit python or turn off the script\nType no to quit and reset the text file\nOtherwise, press enter to create a new prompt\n")
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
