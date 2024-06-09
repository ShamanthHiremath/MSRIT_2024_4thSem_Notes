# Load the dataset
data(mtcars)

my_colors <- c("#FFA500", "#008000", "#1E90FF", "#FF1493")

# Create the box plot with customized aesthetics
bp <- boxplot(disp ~ gear, data = mtcars,
              main = "Displacement by Gear", xlab = "Gear", ylab = "Displacement",
              col = my_colors, border = "black", notch = TRUE, notchwidth = 0.5,
              medcol = "white", whiskcol = "black", boxwex = 0.5, outpch = 19,
              outcol = "black")

# Extract median values for each group
medians <- bp$stats[3, ]

# Print median values
print(medians)