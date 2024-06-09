# Load mtcars dataset
data(mtcars)

# Create a table of counts for each cylinder type
cyl_counts <- table(mtcars$cyl)

# Create a bar plot using base R
barplot( #cyl_counts,
        mtcars$cyl,
        main="Bar Plot", 
        xlab="Number of Cylinders", 
        ylab="Frequency",
        col="blue",
        border="black",
        horiz = TRUE)

# Optionally, add more customizations such as axis limits, text annotations, etc.

# Horizontal Bar Plot for 
# Ozone concentration in air 
data(airquality)

barplot(airquality$Ozone, 
		main = 'Ozone Concenteration in air', 
		xlab = 'ozone levels') 

