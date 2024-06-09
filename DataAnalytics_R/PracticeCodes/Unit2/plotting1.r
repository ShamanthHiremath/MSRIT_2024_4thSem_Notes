library(dplyr)
library(tidyr)

# Assuming 'df' is your data frame
df %>%
  summarise(across(where(is.numeric), .fns = list(mean = mean, sd = sd)))

# Add two numbers
result <- 5 + 5
cat("Result:", result, "\n")
plot(1:10)