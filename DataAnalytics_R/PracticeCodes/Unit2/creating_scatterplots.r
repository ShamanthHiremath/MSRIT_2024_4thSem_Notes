# Get the input values.
input <- mtcars[, c('wt', 'mpg')]
print(head(input))

# Plot the chart for cars with
# weight between 1.5 to 4 and
# mileage between 10 and 25.
plot(x = input$wt, y = input$mpg,
     xlab = "Weight",
     ylab = "Mileage",
     xlim = c(1.5, 4),
     ylim = c(10, 25),     
     main = "Weight vs Mileage")
