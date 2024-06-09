# Description: Relational operations in R
vec1 <- c(0, 2)
vec2 <- c(TRUE, FALSE)

# Element-wise relational operations
equal <- vec1 == vec2
cat("Element-wise equality:", equal, "\n")

not_equal <- vec1 != vec2
cat("Element-wise inequality:", not_equal, "\n")

greater_than <- vec1 > vec2
cat("Element-wise greater than:", greater_than, "\n")

less_than <- vec1 < vec2
cat("Element-wise less than:", less_than, "\n")

greater_than_or_equal <- vec1 >= vec2
cat("Element-wise greater than or equal:", greater_than_or_equal, "\n")

less_than_or_equal <- vec1 <= vec2
cat("Element-wise less than or equal:", less_than_or_equal, "\n")

ind <- vec1[0]  | vec2[0]
print(ind)