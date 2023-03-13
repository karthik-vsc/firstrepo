def binarysearch(lis,low,high,target,method):
    if method=="iterative" or method=="Iterative":
        low,high=0,len(lis)-1
        while low<=high:
            mid=round(low+high/2)
            if target==lis[mid]:
                return mid
            elif target<lis[mid]:
                high=mid-1
            else:
                low=mid+1
        return "Element not found"
    elif method=="recursive" or method=="Recursive":
        mid=(low+high)//2
        if low<=high:
            if target==lis[mid]:
                return mid
            elif target<lis[mid]:
                    return binarysearch(lis,low,mid-1,target,method)
            else:
                return binarysearch(lis,mid+1,high,target,method)
        else:
            return "Element not found"
    else:
        return "Invalid method"
      
lis=list(map(int,input("Enter the elements with space:").split()))
target=int(input("Enter the element to be searched:"))
method=input("Enter the type of method either iterative or recursive:")
low,high=0,len(lis)-1
print(sorted(lis))
print("element position:",binarysearch(sorted(lis),low,high,target,method))