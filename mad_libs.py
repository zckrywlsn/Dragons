# A simple madlibs like game.
def poem (list):
    print ("")
    print ("There was an old ",list[0]," who ", list[1]," in a shoe")
    print ("She had so many " ,list[2]," she didn't know what to do.")
    print ("She ",list[3]," them some ",list[4]," without any ",list[5],";")
    print ("And ",list[6]," them all ",list[7]," and put them to bed.")

def getwords ():
    list = []
    list.append(input("Pick a noun: ")) #woman
    list.append(input("Pick a past tens verb: "))   #lived
    list.append(input("Pick a plural noun: ")) #children
    list.append(input("Pick a past tens verb ")) #gave
    list.append(input("Pick a noun: ")) #broth
    list.append(input("Pick a noun: ")) #bread
    list.append(input("Pick a past tens verb: ")) #whipped
    list.append(input("Pick a adjective: ")) #soundly
    return list
poem(getwords())
