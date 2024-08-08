import random
import matplotlib.pyplot as plt
import time
import math

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

def partition(arr, low, high):
    pivot = arr[low]
    i = low

    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[i] = arr[i], arr[low]
    return i

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




no_of_inputs = [no for no in range(10, 1000, 50)]

arrays = []

for i in no_of_inputs:
    arrays.append([random.randint(0, 1000) for _ in range(i)])

time_series = []

for arr in arrays:
    start_time = time.time()
    quick_sort(arr, 0, len(arr)-1)
    end_time = time.time()
    time_series.append((end_time - start_time)*1000000)
    print(f"Execution time for {len(arr)} inputs: {end_time - start_time:.6f} seconds")

n_log_n = [n * math.log(n) for n in no_of_inputs]
plt.plot(no_of_inputs, time_series, label="Merge Sort")
plt.plot(no_of_inputs, n_log_n, label="O(nlogn)")
plt.xlabel("No of Inputs")
plt.ylabel("Time taken")
plt.title("TIME COMPLEXITY OF MERGE SORT")
plt.legend()
plt.show()
