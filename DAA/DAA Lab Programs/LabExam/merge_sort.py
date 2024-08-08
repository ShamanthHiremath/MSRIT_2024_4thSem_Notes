import time
import math
import random
import matplotlib.pyplot as plt

def merge(arr, s, e):
    mid = s + (e - s) // 2
    length1 = mid + 1 - s 
    length2 = e - mid

    left = arr[s:mid+1]
    right = arr[mid+1:e+1]
    # inv_count = 0
    

    i, j, k = 0, 0, s

    while i < length1 and j < length2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            # inv_count += (mid - i + 1)
            
        k += 1

    while i < length1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < length2:
        arr[k] = right[j]
        j += 1
        k += 1
    # return inv_count

def merge_sort(arr, s, e):
    # inv_count = 0
    if s < e:
        mid = s + (e - s) // 2
        
        merge_sort(arr, s, mid)
        merge_sort(arr, mid + 1, e)
        merge(arr, s, e)
        
        # inv_count += merge_sort(arr, s, mid)
        # inv_count += merge_sort(arr, mid + 1, e)
        # inv_count += merge(arr, s, e)
        
    # return inv_count


arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)
    
    
start_time = time.time()
merge_sort(arr, 0, len(arr)-1)
end_time = time.time()
# print(merge_sort(arr, 0, len(arr)-1))

print("The sorted array is:", arr)
print(f"Execution time: {end_time - start_time:.6f} seconds")
# print(f"O({n} * log{n}) = {math.log(n)} is nearly equal to {end_time - start_time:.6f}")
print("The time complexity of Merge Sort is O(nlogn).")



no_of_inputs = [no for no in range(10, 1000, 50)]

arrays = []

for i in no_of_inputs:
    arrays.append([random.randint(0, 1000) for _ in range(i)])

time_series = []

for arr in arrays:
    start_time = time.time()
    merge_sort(arr, 0, len(arr)-1)
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