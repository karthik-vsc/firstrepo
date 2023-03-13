def insertionsort(arr):
    #shifting
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

    #swapping
    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j=j-1
    return arr

lis=list(map(int,input("Enter elements in list:").split()))
print(insertionsort(lis))

