
#code for Linear search
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Return the index if found
    return -1  # Return -1 if not found

# Example usage
arr = [10, 25, 30, 45, 50]
target = 30

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

#code for Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  
        
        
        if arr[mid] == target:
            return mid  
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return -1  
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")
