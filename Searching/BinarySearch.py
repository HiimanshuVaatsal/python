def binarySearch(arr,target):
    start=arr[0]
    end=len(arr)-1
    mid=0
    for i in range(len(arr)):
        mid=start+end/2
        if arr[mid]==target:
            return print('same')
        elif arr[mid]>=target:
