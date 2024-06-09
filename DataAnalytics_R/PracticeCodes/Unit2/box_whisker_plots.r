# Using base R
boxplot(mtcars, main="Box and Whisker Plots", las=2)

# Using ggplot2
library(reshape2)
mtcars_melt <- melt(mtcars)
ggplot(mtcars_melt, aes(x=variable, y=value)) + 
  geom_boxplot() + 
  ggtitle("Box and Whisker Plots") + 
  xlab("Variables") + 
  ylab("Values")
