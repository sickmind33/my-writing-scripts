#Calculate the cost of a story as the story is being written

import math
import time

def get_txt():
    text = input("What is your file name?\nNote: file must be in same location as script\n")
    return text


def count(txt):
    file = open(txt,"r")
    with file as f:
        words = len(file.read().split())
    file.close
    return words


def output(items):
    file = open("livecost.txt","w")
    total = items * .02
    file.write("Calculated Cost:\n")
    file.write("$")
    file.write(format(total, ".2f"))
    

def main():
    num = int()
    print("Lanching script")
    txt = get_txt()
    while 2 > 1:
        output(count(txt))
        time.sleep(2)
        

main()
