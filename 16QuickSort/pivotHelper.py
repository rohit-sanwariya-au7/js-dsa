def pivotHelper(array):
    pivotIndex=0
    start=0
    for i in range(1,len(array)):
        if array[start]>array[i]:
            pivotIndex+=1
            array[pivotIndex],array[i]=array[i],array[pivotIndex]
            print(array)
    array[pivotIndex],array[0]=array[0],array[pivotIndex]
    return (array)
    
print(pivotHelper([4,8,7,2,2,2,3,5,1]))