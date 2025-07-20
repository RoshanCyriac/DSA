def ternary_search(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        
        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif key < arr[mid1]:
            high = mid1 - 1
        elif key > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    
    return -1  # Not found

arr = [1, 3, 5, 7, 9]
print(ternary_search(arr, 9))  # Output: 4
