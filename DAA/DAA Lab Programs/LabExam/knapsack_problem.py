def knapsack(weight, value, n, maxWeight):
    # Initialize a 2D list for DP (n x (maxWeight+1))
    dp = [[0] * (maxWeight + 1) for i in range(n)]

    # Base case: Fill the first row (considering only the first item)
    for w in range(weight[0], maxWeight + 1):
        dp[0][w] = value[0]

    # Build DP table
    for i in range(1, n):
        for w in range(maxWeight + 1):
            # Max value obtained either including (the weight of the current item can fit in the knapsack) or excluding (or not fit)
            if weight[i] <= w:
                dp[i][w] = max(dp[i-1][w], value[i] + dp[i-1][w - weight[i]])
            else:
                dp[i][w] = dp[i-1][w]

    # The result is found in the bottom-right cell of the DP table
    return dp[n-1][maxWeight]

def inputWeightsValues():
    n = int(input("Enter the no of items: "))
    weights = []
    for i in range(n):
        wt = int(input(f"Weight {i+1}: "))
        weights.append(wt)

    values = []
    for i in range(n):
        val = int(input(f"Value {i+1}: "))
        values.append(val)

    return weights, values

# Example usage:
# Input example
# weight = [1, 2, 3]
# value = [6, 10, 12]
# n = len(weight)
maxWeight = 5

weights , values = inputWeightsValues()
n = len(weights)

max_value = knapsack(weights, values, n, maxWeight)
print(f"Maximum value that can be stolen: {max_value}")