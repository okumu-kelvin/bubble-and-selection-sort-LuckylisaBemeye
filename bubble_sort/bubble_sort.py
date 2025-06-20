def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Outer loop
        for j in range(n - i - 1):  # Inner loop
            if arr[j] > arr[j + 1]:
               temp = arr[j]
               arr[j] = arr[j + 1]
               arr[j + 1] = temp


numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Sorted array is:", numbers)
