# DATA STRUCTURES

# Vectors
# Ordered collection of same data type
vec = c(1,2,3,4,5)

# List
# Ordered collection of different objects
arr = c(1,2, "sgjds")
arr2 = c(1,2, 3)
arr3 = list("Area" = 123, "peri" = 20)

print(arr)
print(arr2)
print(arr3)

empId = c(1, 2, 3, 4)
empName = c("Debi", "Sandeep", "Subham", "Shiba")
numberOfEmp = 4
empList = list(empId, empName, numberOfEmp)

print(empList)

# Data Frame
# A data frame is a table or a two-dimensional array-like structure in which each column contains values of one variable and each row contains one set of values from each column.
df = data.frame("Name" = c("Mamata", "Sita", "Gita"), "Marks" = c(69, 100, 20))
print(df)

age <- c(22, 12, 33)
names <- c("x", "y", "z")
lang <- c("py", "cpp", "c")

df2 <- data.frame(age, names, lang)

print(df2)

# create a dataframe such as name age and usn , display it and order it based on the age, populate the dataframe with NA values and also deal with the missing values by using NA.argument() functions

names <- c("Kartik", "Joel", "Mitesh")
age <- c(22, 20, 21)
usn <- c("CS076", "CS075", "Cs085")
df3 <- data.frame(names, age, usn)
print(df3)

# Sort the dataframe based on the age column
newdf <- df3[order(df3$age), ]
print("DataFrame sorted based on age:")
print(newdf)


# df3[order(df3$usn), ]
# df3[order(df3$usn, decreasing = TRUE), ]

# Matrix
mat = matrix(c(1,2,3,4,5,6), nrow=2, ncol=3)
print(mat)

# Arrays
# Arrays are the R data objects which store the data in more than two dimensions
A = array(c(1, 2, 3, 4, 5, 6, 7, 8), 
                dim = c(2, 2, 2)    )                    
print(A)

# Factors
# Factors are the data objects which are used to categorize the data and store it as levels. They can store both strings and integers. They are useful in the columns which have a limited number of unique values.
fac = factor(c("Male", "Female", "Male",
               "Male", "Female", "Male", "Female"))
print(fac)



