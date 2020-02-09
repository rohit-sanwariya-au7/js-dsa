
def buble(testlist):
    step=0
    for i in range(len(testlist),0,-1):
        step+=1
        
        swap=True
        for j in range(0,i-1,1):
            if testlist[j+1]<=testlist[j]:
                testlist[j+1],testlist[j]  = testlist[j],testlist[j+1] 
                swap=False
        if swap:
            break
    return [testlist,f"step: {step}"]
print(buble([1,5,3,2]))

