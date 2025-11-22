
def binary(arr , trg):
    low = 0 
    high= len(arr) -1

    while low<= high :
        mid = (low + high)//2 

        if arr[mid]==trg :
            return mid 
        elif arr[mid] < trg :
            low=mid+1

        else :
            high = mid -1 

    return -1



array =[10,20,30,40,50,60,70,80,90]
target = 70

result = binary(array , target)

if result == -1 :
    print("Element not found")
else :
    print("Element found at index ", result)
