z <- 3
f <- function(x,y){
    # print("calc =",x^2+y/z)
    x^2+y/z
}
f(2,3)

# Assigning
# c <- c(1,2,3,4,5)
# c(1,2,3,4,5) -> c
# c = c(1,2,3,4,5)

x = as.raw(255)
# print(x)
x
class(x)
typeof(x)

y = 2
class(y)
typeof(y)
print (is.numeric(y))
print (is.double(y))

x = as.character(2810)
y = as.numeric(0)
z = 5L
comp = 4+3i
print (comp)
print (class(comp))

print (x)
print (y)
print (z)
arr <- c(3,5,6,3,6,8)
sort(arr, decreasing = TRUE)
class(arr)
typeof(arr)
order(arr, decreasing = TRUE)
order(-arr)

# Find sum of numbers 4 to 6.
print(sum(4:6))

# Find max of numbers 4 and 6.
print(max(arr))

# Find min of numbers 4 and 6.
print(min(4:6))
