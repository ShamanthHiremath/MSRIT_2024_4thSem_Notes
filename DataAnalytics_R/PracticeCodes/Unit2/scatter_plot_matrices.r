# Using base R
# Load the mtcars dataset
data(mtcars)
pairs(mtcars, main="Scatter Plot Matrix")

# Plot the matrices between 4 variables giving 12 plots.
# One variable with 3 others and total 4 variables.
pairs(~wt + mpg + disp + cyl, data = mtcars,
      main = "Scatterplot 4 var Matrix")