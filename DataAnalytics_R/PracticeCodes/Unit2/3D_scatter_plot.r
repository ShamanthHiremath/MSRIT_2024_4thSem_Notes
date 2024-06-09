# Using scatterplot3d package
library(scatterplot3d)
scatterplot3d(mtcars$wt, mtcars$mpg, mtcars$hp, main="3D Scatter Plot", xlab="Weight", ylab="Miles Per Gallon", zlab="Horsepower")

# Using plotly
library(plotly)
plot_ly(mtcars, x=~wt, y=~mpg, z=~hp, type="scatter3d", mode="markers") %>%
  layout(title="3D Scatter Plot")
