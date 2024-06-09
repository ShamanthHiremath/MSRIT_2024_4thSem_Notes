# Loading ggplot2 package
library(ggplot2)

# Creating scatterplot with fitted values.
# An additional function stat_smooth
# is used for linear regression.
new_graph <- ggplot(mtcars, aes(x = log(mpg), y = log(drat))) +  # Transforming variables with logarithm
    geom_point(aes(color = factor(gear))) +  # Coloring points by gear
    stat_smooth(method = "lm",  # Adding linear regression line
                col = "#C42126",  # Setting color of the line
                se = FALSE,  # Not plotting standard error ribbon
                size = 1)  # Setting size of the line

# Adding title with dynamic name
new_graph + labs(title = "Relation between Mile per hours and drat",
                 subtitle = "Relationship break down by gear class",
                 caption = "Authors own computation")
