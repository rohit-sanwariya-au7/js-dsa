def bubble(testlist):
    for i in range(len(testlist)):
        for j in range(len(testlist)):
            if testlist[j]>testlist[j+1]:
                testlist[j],testlist[j+1] = testlist[j+1],testlist[j]
    return testlist
bubble([2,5,1])
