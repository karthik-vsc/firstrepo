#with swapped variable - optimized version of bubble sort
#with swapped if the list is sorted ahead of total iterations loop will break 
# Time complexity: O(n^2)
def bubblesort(lis):
    for i in range(len(lis)):
        swapped=False
        for j in range(0,len(lis)-1-i):
            # '<' for descending order
            if lis[j]>lis[j+1]:
                temp=lis[j]
                lis[j]=lis[j+1]
                lis[j+1]=temp
                swapped=True
        if not swapped:
            break
    return lis
lis=list(map(int,input("Enter elements of list:").split()))
print("Sorted list:",bubblesort(lis))
