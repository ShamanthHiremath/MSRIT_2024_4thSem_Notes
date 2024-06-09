data(airquality) 
boxplot(airquality$Wind, 
        main = "Average wind speed at La Guardia Airport", 
        xlab = "Miles per hour", 
        ylab = "Wind", 
        col = "orange", 
        border = "brown", 
        horizontal = TRUE, 
        notch = TRUE)

# Multiple Box plots, each representing 
# an Air Quality Parameter 
boxplot(airquality[, 0:4], 
		main ='Box Plots for Air Quality Parameters') 

