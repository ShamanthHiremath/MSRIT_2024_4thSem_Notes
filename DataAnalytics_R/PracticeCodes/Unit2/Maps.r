# Install and load the required packages
install.packages("maps")
library(maps)

# Read dataset
data <- read.csv("worldcities.csv")

# Convert dataset into a dataframe
df <- data.frame(data)

# Plot world map
map(database = "world")

# Mark points on the map
points(x = df$lng[1:500], y = df$lat[1:500], col = "red")
