# Description: Logical operations in R
vec1 <- c(0, 2)
vec2 <- c(TRUE, FALSE)

# Logical AND
logical_and <- vec1 & vec2
cat("Logical AND of vec1 and vec2 is:", logical_and, "\n")

# Logical OR
logical_or <- vec1 | vec2
cat("Logical OR of vec1 and vec2 is:", logical_or, "\n")

# Logical NOT on vec1
logical_not_vec1 <- !vec1
cat("Logical NOT of vec1 is:", logical_not_vec1, "\n")

# Logical NOT on vec2
logical_not_vec2 <- !vec2
cat("Logical NOT of vec2 is:", logical_not_vec2, "\n")