import random

#Custom Node class used for hash/linked list data strucutre
class Node:
    #initalizes fields
    def __init__(self,word):
        self.word = word
        self.occ = 1
        self.next = None
        self.nextWord = None
    def setNext(word):
        self.next = Node(word)
    def setNextWord(word):
        self.nextWord = Node(word)
        self.occ += 1

#Hash table
table = {}

#Function used when writing paper
def writePaper():
    
    #Initalizes variables such as result string, counters, and pointers
    result = ""
    count = 0
    first = True
    second = False
    firstWord = ""
    secondWord = ""
    thirdWord = ""
    firstNode = None
    secondNode = None
    thirdNode = None
    randomCount = 0
    
    #while the result list contains less than or equal to 2000 words
    while(count <= 2000):

        
        #If it is first word of sentance
        if first:
            #Pick a random word from table while it isn't a period
            period = True
            while(period):
                firstNode = random.choice(list(table.values()))
                firstWord = firstNode.word
                if firstWord != ".":
                    period = False
            #Capitalize word, put into result, and change variable conditions
            firstWord.capitalize()
            result += firstWord
            result += " "
            first = False
            second = True

        
        #If it is second word of sentance
        elif second:
            #Sort through children of first word and pick one with highest occurance
            secondNode = firstNode.nextWord
            temp = secondNode
            while(temp.next != None):
                if temp.next.occ > secondNode.occ:
                    secondNode = temp.next
                temp = temp.next
            secondWord = secondNode.word
            #Put into result and change variable conditions
            result += secondWord
            result += " "
            second = False

        
        #If it is 3rd or more word of sentance
        else:
            #Find first word from table, then find second from child of first
            firstNode = table.get(firstNode.word)
            temp = secondNode
            secondNode = firstNode.nextWord
            while(secondNode.word != temp.word):
                secondNode = secondNode.next
            thirdNode = secondNode.nextWord
            temp = thirdNode
            #Sort through children of second word and pick one with highest occurance
            r = 0
            while(temp.next != None):
                if temp.next.occ > thirdNode.occ:
                    thirdNode = temp.next
                temp = temp.next
                r += 1
            #Occasionally selects random child of second word to avoid loops
            if randomCount >= random.randint(4,6):
                r = random.randint(0,r)
                c = 0
                thirdNode = secondNode.nextWord
                while(c < r):
                    thirdNode = thirdNode.next
                    c+=1
                randomCount = 0
            #Put into result and change variable conditions
            thirdWord = thirdNode.word
            result += thirdWord
            result += " "
            if thirdWord == ".":
                first = True
            else:
                firstNode = secondNode
                secondNode = thirdNode
            randomCount += 1

            
        count += 1
    #Open, write, and close file
    file = open("Readme.txt", "w")
    file.write(result)
    print(result)
    file.close()
    

#Function used with populating table
def populateTable(theList):
    #Initalize variables
    global table
    parentInt = 0
    #For length of story
    for index in range(len(theList) - 2):
        #Create first node and if in table get prevous else put into table
        parentNode = Node(theList[parentInt])
        if parentNode.word in table:
            parentNode = table.get(parentNode.word)
            parentNode.occ += 1
        else:
            table[parentNode.word] = parentNode
        #Create child, if already connected to parent increment occurance else insert node
        childNode = Node(theList[parentInt+1])
        if parentNode.nextWord == None:
            parentNode.nextWord = childNode
        else:
            parentNode = parentNode.nextWord
            double = False
            while parentNode.next != None:
                if parentNode.word == childNode.word:
                    parentNode.occ += 1
                    double = True
                    childNode = parentNode
                    break
                parentNode = parentNode.next
            if not(double):
                parentNode.next = childNode
        #Create subChild, if already connected to child increment occurance else insert node
        subChildNode = Node(theList[parentInt+2])
        if childNode.nextWord == None:
            childNode.nextWord = subChildNode
        else:
            childNode = childNode.nextWord
            double = False
            while childNode.next != None:
                if childNode.word == subChildNode.word:
                    childNode.occ += 1
                    double = True
                    break
                childNode = childNode.next
            if not(double):
                childNode.next = subChildNode
        parentInt += 1

