data(airquality) 
hist(airquality$Temp, 
     main = "La Guardia Airport's Maximum Temperature (Daily)", 
     xlab = "Temperature (Fahrenheit)", 
     xlim = c(50, 125), 
     col = "yellow", 
     freq = TRUE) 
