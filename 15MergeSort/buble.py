def swap(x,y):
    print(x,y)
    x,y=y,x
    print(x,y)
    
def buble(testlist):
    for i in range(len(testlist),0,-1):
        for j in range(0,i-1,1):
            if testlist[j+1]<=testlist[j]:
                testlist[j+1],testlist[j]  = testlist[j],testlist[j+1] 
    return testlist

print(buble([1,5,3,2]))