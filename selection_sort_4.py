
#arr = [5,4,6,3,2,8]

def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Get input from user
arr = list(map(int, input("Enter the numbers for selection sort: ").split()))

# Print original array
print("Original array:", arr)


# Print sorted array
print("Sorted array:", selection_sort(arr))
