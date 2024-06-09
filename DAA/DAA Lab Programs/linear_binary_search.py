import numpy as np
import time
import matplotlib.pyplot as plt

def linSearch(key, arr, pos, end):
    if pos >= end:
        print("ELEMENT NOT FOUND")
        return
    elif key == arr[pos]:
        print("ELEMENT FOUND AT", pos)
        return
    else:
        linSearch(key, arr, pos + 1, end)
        
def binSearch(arr, key, s, e):
    if(s<=e):
        mid = s + (e - s) // 2
        if(arr[mid] == key):
            print("ELEMENT ", key ," FOUND AT: ", mid)
            return
        elif(arr[mid]>key):
            binSearch(arr, key, s, mid-1)
        else:
            binSearch(arr, key, mid+1, e)
    else:
        print("ELEMENT", key, "NOT FOUND")
        return

def measure_search_time(length):
    arr = np.random.randint(0, 100, size=length)
    elem = np.random.randint(0, 100)
    tik = time.time()
    linSearch(elem, arr, 0, arr.size)
    tok = time.time()
    return tok - tik

# Measure time for different array sizes
array_sizes = [10, 100, 1000, 10000, 100000]
times = []
for size in array_sizes:
    search_time = measure_search_time(size)
    times.append(search_time)

# Plotting
plt.plot(array_sizes, times, marker='o')
plt.xlabel('Array Size')
plt.ylabel('Time Taken (s)')
plt.title('Linear Search Time Complexity')
plt.grid(True)
plt.show()