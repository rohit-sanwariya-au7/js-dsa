def merge(first,second):
    i=0
    j=0
    final=[]
    while(i<len(first) and j<len(second)):
        
        if first[i]<second[j]:
            final.append(first[i])
            i+=1
        else:
            
            final.append(second[j])
            j+=1
    while(i<len(first)):
            final.append(first[i])
            i+=1
    while(j<len(second)):
            final.append(second[j])
            j+=1
 
    return final

def mergesort(testlist):
    if len(testlist)<=1:
        return testlist
    else:
        mid = len(testlist)//2
        left=mergesort(testlist[:mid])
        right=mergesort(testlist[mid:])
        
        return(merge(left,right))
    print(merge(left,right))
print(mergesort([1,2,3,4,5]))