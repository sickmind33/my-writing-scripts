#Script for creating simple characters
import random
letters = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z")
vowels = ("a","e","i","o","u","y",)
creatures = ("dog","cat","horse","dragon","fox","tiger","donkey","rhino","elephant","deer","lion","cheetah","lizard","raccoon","mouse","gazelle","giraffe","zebra")
gender = ("male","female")
boobsize = ("small","medium","large","massive")
dicksize = ("small","medium","large","massive")
emotions = ("happy","sad","angry","jealous","dominating","submissive","horny","hungry","tired","exhausted","excited")

species = str()
name = str()
length = int()
count = int()
glyph = str()
sag = str()
finalName = str()
feet = int()
inches = int()
height = str()
breasts = str()
dick = str()
attitude = str()

length = random.randint(2,3)
while length != count:
    glyph = letters[random.randint(0,18)]
    name = name + glyph
    glyph = vowels[random.randint(0,5)]
    name = name + glyph
    species = creatures[random.randint(0,17)]
    sag = gender[random.randint(0,1)]
    feet = random.randint(0,8)
    if feet == 0:
        inches = random.randint(1,11)
    else:
        inches = random.randint(0,11)
    attitude = emotions[random.randint(0,10)]
    if sag == "female":
        breasts = boobsize[random.randint(0,3)]
    else:
        dick = dicksize[random.randint(0,3)]
    count = count + 1
    

finalName = " " + species + finalName
finalName = " the " + sag + finalName
finalName = name + finalName

print(finalName)
print("Attitude:",attitude)
if sag == "female":
    print("breast size:",breasts)
else:
    print("penis size:",dick)
print(feet,"feet and",inches,"inches tall")
