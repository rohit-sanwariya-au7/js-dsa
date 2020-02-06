def selectionSort(listtest):
    for x in range(len(listtest)):
        min=x
        for y in range(x+1,len(listtest)):
            if(listtest[min]>listtest[y]):
                min=y
        listtest[x],listtest[min]=listtest[min],listtest[x]
    return listtest

print(selectionSort([1,4,3,2]))

