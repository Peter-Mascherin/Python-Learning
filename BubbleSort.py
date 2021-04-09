#BubbleSort by Peter Mascherin

import random

def bubblesort(array):
     
    loopnum = len(array) #loopnum set to array length
    
    for i in range(loopnum-1):  #loop through all array elements

        for j in range(0,loopnum-i-1): #loop through array minus i since bubble sort sorts elements last to first

            if array[j] > array[j+1]:
                # if element is greater than element infront of it, swap it
                array[j],array[j+1] = array[j+1],array[j]

def printArrayBubble(array):
    #loops through array printing each value inside array
    for i in range(len(array)):
        print(array[i],end="  ")
    print() #empty line print

numArray = [] #initialize array
for ggez in range(0,random.randint(10,100)): #meant to assign and random size to array, filled with random values
    numArray.append(random.randint(0,100))

printArrayBubble(numArray)
bubblesort(numArray)
printArrayBubble(numArray)