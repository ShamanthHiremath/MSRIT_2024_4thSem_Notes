import matplotlib.pyplot as plt
import math

# Define the functions
log_n = lambda x: math.log(x, 2)
n = lambda x: x
n_log_n = lambda x: x * math.log(x, 2)
n_2 = lambda x: x * x
n_3 = lambda x: x * x * x
exp_n = lambda x: 2 ** x
factorial = lambda x: math.factorial(x)

# Define the x-points
xpts = [x for x in range(100, 20000, 2000)]
xpts2 = [x for x in range(0, 100, 10)]  # Smaller range for exp_n and factorial

xpts.insert(0, 1)
# xpts2.insert(0, 1)

# Plot the functions
plt.plot(xpts, [log_n(x) for x in xpts], label="log_n")
plt.plot(xpts, [n(x) for x in xpts], label="n")
plt.plot(xpts, [n_log_n(x) for x in xpts], label="n log n")
plt.plot(xpts, [n_2(x) for x in xpts], label="n^2")
plt.plot(xpts, [n_3(x) for x in xpts], label="n^3")
plt.plot(xpts2, [exp_n(x) for x in xpts2], label="2^n")
plt.plot(xpts2, [factorial(x) for x in xpts2], label="n!")

# Set y-axis limit for better visualization
plt.ylim([0, 100000])

# Add legend and show plot
plt.xlabel("No of Inputs (n)")
plt.ylabel("Big O(f(n))")
plt.title("Asymptotic Complexity")
plt.legend()
plt.show()
