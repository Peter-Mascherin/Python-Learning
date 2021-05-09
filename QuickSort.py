#QuickSort by Peter Mascherin
import random

def partition(array,low,high):
    num = (low-1)
    pivot = array[high]

    for i in range(low,high):

        if(array[i] <= pivot):

            num = num + 1
            array[num], array[i] = array[i],array[num]
    
    array[num+1],array[high] = array[high],array[num+1]
    return (num + 1)


def sortMethod(array,low,high):
    if(len(array) == 1):
        return array
    if(low<high):

        pick = partition(array,low,high)

        sortMethod(array,low,pick-1)
        sortMethod(array,pick+1,high)


numset = [100,573,42,432,451,123,6412,53,1,0]
n = len(numset)
sortMethod(numset,0,n-1)
print("Array number set sorted is: ")
for i in range(n):
    print("%d" % numset[i])