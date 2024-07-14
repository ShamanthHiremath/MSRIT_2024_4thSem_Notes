def weighted_interval_scheduling(intervals):
    # Sort intervals based on end time
    intervals.sort(key=lambda x: x[1])

    # Initialize dp array with 0s
    n = len(intervals)
    dp = [0] * n

    # Base case
    dp[0] = intervals[0][2]  # Value of the first interval

    # Build dp array
    for i in range(1, n):
        # Option 1: Include current interval
        value_incl = intervals[i][2]  # Value of current interval
        j = find_latest_non_overlapping(intervals, i)
        if j != -1:
            value_incl += dp[j]

        # Option 2: Exclude current interval
        value_excl = dp[i-1]

        # Choose the maximum of including or excluding the current interval
        dp[i] = max(value_incl, value_excl)

    # The result is the maximum value subset
    return dp[n-1]

def find_latest_non_overlapping(intervals, current_index):
    # Find the latest interval that does not overlap with the current interval
    for j in range(current_index - 1, -1, -1):
        if intervals[j][1] <= intervals[current_index][0]:
            return j
    return -1

def input_intervals():
    n = int(input("Enter the number of intervals: "))
    intervals = []
    for i in range(n):
        start_time = int(input(f"Interval {i+1} start time: "))
        end_time = int(input(f"Interval {i+1} end time: "))
        value = int(input(f"Interval {i+1} value: "))
        intervals.append((start_time, end_time, value))
    return intervals

# Example usage:
intervals = input_intervals()
max_value = weighted_interval_scheduling(intervals)
print(f"Maximum value subset of intervals: {max_value}")