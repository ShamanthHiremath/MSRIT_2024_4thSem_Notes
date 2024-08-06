def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0

    # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # There are mid - i inversions, because all elements left to i in the left subarray 
            # are greater than arr[j]
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into Original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
        
    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

# Driver code
arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    arr.append(x)

temp_arr = [0]*n
result = merge_sort_and_count(arr, temp_arr, 0, n-1)
print("Number of inversions are", result)
print("The sorted array is:", arr)




'''
def merge(arr, s, e):
    mid = s + (e - s) // 2
    length1 = mid - s + 1
    length2 = e - mid

    left = arr[s:mid+1]
    right = arr[mid+1:e+1]
    inv_count = 0
    

    i, j, k = 0, 0, s

    while i < length1 and j < length2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inv_count += (mid - i + 1)
            
        k += 1

    while i < length1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < length2:
        arr[k] = right[j]
        j += 1
        k += 1
    return inv_count

def merge_sort(arr, s, e):
    inv_count = 0
    if s < e:
        mid = s + (e - s) // 2
        
        # merge_sort(arr, s, mid)
        # merge_sort(arr, mid + 1, e)
        # merge(arr, s, e)
        
        inv_count += merge_sort(arr, s, mid)
        inv_count += merge_sort(arr, mid + 1, e)
        inv_count += merge(arr, s, e)
        
    return inv_count


arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    arr.append(x)

print(merge_sort(arr, 0, len(arr)-1))

print("The sorted array is:", arr)

'''