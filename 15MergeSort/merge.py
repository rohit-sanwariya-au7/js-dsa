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
print(merge([1,4,5],[2,6,7,8]))
