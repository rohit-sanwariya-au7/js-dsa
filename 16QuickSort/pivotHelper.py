def swapHelper(array,pivotIndex,i):
    array[pivotIndex],array[i]=array[i],array[pivotIndex]



def pivotHelper(array):
    pivotIndex=0
    for i in range(1,len(array)):
        if array[0]>array[i]:
            pivotIndex+=1
            print(pivotIndex,i)
            swapHelper(array,pivotIndex,i)
            print(array)
    swapHelper(array,pivotIndex,0)
    return array
print(pivotHelper([4,8,7,2,2,2,3,5,1]))