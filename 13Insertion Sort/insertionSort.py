def insertSort(array):
    for i in range(1,len(array)):
        current=array[i]
        j=i-1
        print("current and j",current,array[j])
        while(j>=0 and array[j]>current):
            array[j+1]=array[j] #bhen chod jab tak array[j]>array[j+1]
            #swap karo matlab piche se ka ek pakad ke age walon se compare
            #karo har jo bada ho use swa
            j-=1
        array[j+1]=current
        print(array,i)


    return array

insertSort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48])