# install package dplyr
install.packages("dplyr")

# import library dplyr
library(dplyr)

# create dataframe
df <- data.frame("Age" = c(12, 21, 15, 5, 25), 
                 "Name" = c("Johnny", "Glen", "Alfie", "Jack", "Finch"))

# sort the dataframe on the basis of
# Age column using arrange method
arrange(df, Age)


# create factor data with 5 strings 
factor_data < - as.factor(c("sravan", "sravan", "bobby", "pinkey", "sravan")) 

# display before ordering 
print(factor_data) 

# display after ordering 
print(as.ordered(factor_data)) 