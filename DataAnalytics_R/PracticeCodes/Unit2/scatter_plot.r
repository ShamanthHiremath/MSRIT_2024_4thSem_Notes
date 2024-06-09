# Load the dataset
data(airquality)

# Create the scatter plot
plot(airquality$Ozone, airquality$Month, 
     main = "Ozone Concentration by Month", 
     xlab = "Ozone Concentration (ppb)", 
     ylab = "Month of Observation", 
     pch = 19)
