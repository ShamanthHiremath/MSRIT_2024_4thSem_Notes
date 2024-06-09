# Load the dataset
data(mtcars)

# Define the variables for the box plots
variables <- c("mpg", "disp", "hp", "wt")

# Set up the plotting layout
par(mfrow = c(1, length(variables)))

# Create a vector of colors for the legend
colors <- c("skyblue", "orange", "green", "red")

# Create the box plots
for (i in 1:length(variables)) {
  var <- variables[i]
  boxplot(get(var) ~ gear, data = mtcars,
          main = paste("Box Plot of", var),
          xlab = "Gear",
          ylab = var,
          col = colors[i], # Set color for the current variable
          border = "black",
          notch = TRUE,
          notchwidth = 0.5,
          medcol = "white",
          whiskcol = "black",
          boxwex = 0.5,
          outpch = 19,
          outcol = "black")
}

# Add legend
legend("topright", legend = variables, fill = colors, title = "Variables")

# Reset the plotting layout
par(mfrow = c(1, 1))
