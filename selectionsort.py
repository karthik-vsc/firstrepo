#time complexity: O(n^2)
def insertionsort(lis):
    for i in range(len(lis)):
        min_ind=i
        for j in range(i+1,len(lis)):
            # '>' for descending order
            if lis[j]<lis[min_ind]:
                min_ind=j
        #shorthand for swapping
        lis[i],lis[min_ind]=lis[min_ind],lis[i]
    return lis
lis=list(map(int,input("Enter elements of list:").split())) 
print("Sorted list:",insertionsort(lis))