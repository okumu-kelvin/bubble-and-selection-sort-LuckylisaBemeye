def find_min(arr, start, n):
   
    smallest = arr[start]
    pos = start
    for j in range(start + 1, n):
        if arr[j] < smallest:
            smallest = arr[j]
            pos = j
    return pos

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        pos = find_min(arr, i, n)
        arr[i], arr[pos] = arr[pos], arr[i]

numbers = [64, 25, 12, 22, 11]
print("Original array:", numbers)

selection_sort(numbers)
print("Sorted array:  ", numbers)
