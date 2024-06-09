def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Take input for the array
arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    arr.append(x)

# Perform quick sort
quick_sort(arr, 0, len(arr) - 1)

# Print the sorted array
print("The sorted array is:", arr)
