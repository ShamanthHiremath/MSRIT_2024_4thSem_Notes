def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while(j>=0 and key < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    arr.append(x)

insertion_sort(arr)

print("The sorted array is:", arr)