def quicksort(lis):
    if len(lis)<=1:
        return lis
    else:
        pivot=lis.pop()
    items_greater=[]
    items_smaller=[]
    for data in lis:
        if data<pivot:
            items_smaller.append(data)
        if data>pivot:
            items_greater.append(data)
    return quicksort(items_smaller)+[pivot]+quicksort(items_greater)
print(quicksort([10,1,6,4,17,14]))