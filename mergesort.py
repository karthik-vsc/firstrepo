def mergesort(lis):
    if len(lis)>1:
        sublis1=lis[0:len(lis)//2]
        sublis2=lis[len(lis)//2:]
        mergesort(sublis1)
        mergesort(sublis2)
        i,j,k=0,0,0
        while i<len(sublis1) and j<len(sublis2):
            if sublis1[i]>sublis2[j]:
                lis[k]=sublis1[i]
                i+=1
            else:
                lis[k]=sublis2[j]
                j+=1
            k+=1
        while i<len(sublis1):
            lis[k]=sublis1[i]
            i+=1
            k+=1
        while j<len(sublis2):
            lis[k]=sublis2[j]
            j+=1
            k+=1
        return lis
    else:
        return lis
        
print(mergesort([i for i in range(1,101)]))