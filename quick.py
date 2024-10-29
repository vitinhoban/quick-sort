def quicksort(arr):
    
    if len(arr) <= 1:
        return arr
 
    
    pivot = arr[-1]
    left = []
    right = []
    equal = []
 
    
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            equal.append(element)
 
    
    return quicksort(left) + equal + quicksort(right)
 
 
numbers = [3, 6, 8, 10, 1, 2, 1]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)