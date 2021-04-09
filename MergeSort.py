# MergeSort by Peter Mascherin
import random

def printArray(array):
    #loops through array printing each value inside array
    for i in range(len(array)):
        print(array[i],end="  ")
    print() #empty line print

def mergeSort(array):
    #checks if array is bigger then one index
    if(len(array) > 1):
        middle = len(array)//2  #splits the array in half (uses // to assign as int, / is for float)
        left = array[:middle]  #"left" side of the array , everything before the middle point
        
        right = array[middle:]  #"right" side of the array, everything after middle
        
        mergeSort(left) #recursive calls but sends left side of array (recursivley, so second call sends back the left side of the split left that was sent back and so on)
        mergeSort(right)    #recursive calls but sends right side of array (recursivley, so second call sends back the right side of the split left that was sent back and so on)

        l=0 #left control var
        r=0 #right control var
        c=0 #'flag' control var
        
        #the sort algorithm, while l and r are less then the values of left[l] and right[r] respectively, checks which side is bigger (left or right)
        #and assigns the value to array[c] incrementing either l or r on each pass, and always incrementing c
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array[c] = left[l]
                l += 1
            else:
                array[c] = right[r]
                r += 1
            c += 1

        #checks if l is less than the length or left[], if it is assigns left[l] to array[c]
        while l < len(left):
            array[c] = left[l]
            l += 1
            c += 1

        #checks if r is less than the length or right[], if it is assigns right[r] to array[c]   
        while r < len(right):
            array[c] = right[r]
            r += 1
            c += 1



numArray = [] #initialize array
for ggez in range(0,random.randint(10,100)): #meant to assign and random size to array, filled with random values
    numArray.append(random.randint(0,100))
printArray(numArray)
mergeSort(numArray)
printArray(numArray)

