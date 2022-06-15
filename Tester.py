import re
import Markov


def removePun(string):
 
    # punctuation marks
    punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''
 
    # traverse the given string and if any punctuation
    # marks occur replace it with null
    for x in string.lower():
        if x in punctuations:
            string = string.replace(x, "")
 
    return string

def getStory(title):
    file = open(title, "r")
    #Skip through title and author
    file.readline()
    file.readline()
    file.readline()
    file.readline()
    #Initialize variables
    result = ""
    temp = ""
    tempNext = ""
    #Loop through text line by line until the end
    while True:
        line = file.readline()
        #If end break
        if not line:
            break
        #If Chapter line then skip
        if "CHAPTER" in line:
            file.readline()
        else:
            index = line.find(".")
            #If line contains period
            if index != -1:
                #Another loop if there is more than 1 period in line
                while True:
                    index = line.find(".")
                    temp += line[:index+1]
                    tempNext = line[index+1:]
                    temp.lower()
                    temp = removePun(temp)
                    result += temp
                    temp = tempNext
                    #If more than 1 period
                    if temp.find(".") != -1:
                        line = temp
                        temp = ""
                    else:
                        break
            #Doesnt contain period
            else:
                temp += line
    #Seperate periods
    result = result.replace(".", " .")
    file.close()
    return result.split()

#Populate hash table
Markov.populateTable(getStory("trainingText1.txt"))
Markov.populateTable(getStory("trainingText2.txt"))

#Writes 2000 word paper
Markov.writePaper()
