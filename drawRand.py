# This program was created by Adam Lei
# It will create a dictionary from a file and
# create a random number to select a character from the
# dictionary 
import random

class Character:
    def __init__(self, name, series):
        self.name = name
        self.series = series
    def printChar(self):
        print(self.name + " from " + self.series)

def printAll(subjectList):
    for i in subjectList:
        subjectList[i].printChar()

random.seed()
# Create an empty dictionary to populate
subjectList = {}
charF = open("test.txt", "r")
# First line in file should be number of characters to put in the dictionary
numChar = int(charF.readline())

for i in range(numChar):
    line = charF.readline()
    charEle = line.split(" ")
    if (len(charEle) != 2):
        raise Exception('Error in text file formatting')
    charEle[0] = charEle[0].replace("_", " ")
    charEle[1] = charEle[1].replace("_", " ")
    subjectList[i] = Character(charEle[0], charEle[1])
    
#printAll(subjectList)
subjectList[random.randint(0, numChar - 1)].printChar()
