def binarySearch(arr,l, r, x):
    if r>=1:
        mid = l+(r-l)//2
        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1
    

arr = [12,33,24,10,4,5,0]
arr.sort()
print(arr)
x = 5

result = binarySearch(arr, 0, len(arr)-1, x)

if result==-1:
    print(f"{x} is not found")
    
else:
    print("Element present at index ",result)