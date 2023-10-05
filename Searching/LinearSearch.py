def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=[2,3,5,7,4,8]
target=3
result=linearSearch(arr,target)

if result !=-1:
    print(f"Target {target} is in index {result}")
else:
    print(f"Target{target} is not found!")