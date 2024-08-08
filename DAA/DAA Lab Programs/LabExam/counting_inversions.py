def merge(arr, s, e):
    mid = s + (e - s) // 2
    length1 = mid + 1 - s 
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





user1 = list(map(int, input("Enter playlist ranking songs of USER 1 with spaces: ").split()))
user2 = list(map(int, input("Enter playlist ranking songs of USER 2 with spaces: ").split()))
n = len(user1)
base_user = [i for i in range(n)]

result1 = merge_sort(user1, 0, n-1)
print("Number of inversions are", result1)
print("The sorted array is:", user1)

result2 = merge_sort(user2, 0, n-1)
print("Number of inversions are", result2)
print("The sorted array is:", user2)


print("The minimum no of inversions required to make the playlist of USER 1 same as USER 2 is", abs(result1 - result2))





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