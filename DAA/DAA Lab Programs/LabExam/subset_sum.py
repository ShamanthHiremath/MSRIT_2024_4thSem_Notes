ansarr = []
ans = []

def copy_arr (arr):
    ans.append(arr.copy())
        
def subset_sum(arr, index, target, dp):
    if target == 0:
        # copy_arr(ansarr)
        ans.append(ansarr[:])
        return True
    
    if index >= len(arr):
        return False

    if dp[index][target] != -1:
        return dp[index][target]
    
    include = False
    # Include the current element
    if arr[index] <= target:
        ansarr.append(arr[index])
        include = subset_sum(arr, index + 1, target - arr[index], dp)
        ansarr.pop()
        
    # Exculde the current element
    exclude = subset_sum(arr, index + 1, target, dp)

    result = include or exclude
    
    dp[index][target] = result
    
    return dp[index][target]

arr = list(map(int, input("Enter the list of numbers (separated by spaces): ").split()))
target = int(input("Enter the target sum: "))

dp = [[-1 for _ in range(target + 1)] for _ in range(len(arr))]

if subset_sum(arr, 0, target, dp):
    print(f"A subset with sum {target} exists.\nSubsets are the following")
    print(ans)
else:
    print(f"No subset with sum {target} exists.")