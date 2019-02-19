import math
import time

def cost():
        cont = str()
        while cont != "no":
                client = input("Who will this be written for?\n")
                wordcount = int(input("How many words did the client request?\n"))
                baseprice = 0.02
                finalprice = int()
                finalprice = wordcount * baseprice
                print("\nClient: ",client,"\nWordcount: ",wordcount,"\nPrice: $",format(finalprice,".2f"))
                
                wordcount = str(wordcount)
                
                file = open("costqueue.txt", "a+")
                file.write(client)
                file.write("\n")
                file.write(wordcount)
                file.write(" Words")
                file.write("\n")
                file.write("$ ")
                file.write(format(finalprice, ".2f"))
                file.write("\n")
                file.write("----------\n")
                file.close()
                
                cont = input("Continue? ")
	



def main():
        time.sleep(1)
        print("Hello Reed\n")
        time.sleep(1)
        cost()
        print("\nHave a nice day Reed!")
        time.sleep(2)

main()
