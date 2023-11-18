#Task 1:4

#The issue in the code is that the recursive calls to merge_sort(left) and merge_sort(right) are not actually modifying the original left and right arrays. In the code, the modified lists are not being returned or assigned, so the changes are lost.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the sublists
    left = merge_sort(left)
    right = merge_sort(right)
    
    i = j = k = 0
    
    # Merge the sorted sublists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr  # Return the sorted array

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(f"The sorted array is: {arr}")


#Now, the modified left and right lists are assigned back to the original variables, ensuring that the sorting is applied to the correct sublists. This should produce the correct output for the merge sort algorithm.