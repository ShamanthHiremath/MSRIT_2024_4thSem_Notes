# Create a data frame with student name, USN, and CGPA
student_data <- data.frame(
  name = c("Alice", "Bob", "Charlie", "David"),
  usn = c("CS001", "CS002", NA, "CS004"),  # Leave one value as NA
  cgpa = c(3.8, NA, 3.5, 3.9)  # Leave one value as NA
)

# Display the rows not having NA
print("Rows not having NA:")
print(student_data[complete.cases(student_data), ])

# Halt display of code if NA is encountered
if (anyNA(student_data)) {
  stop("NA values encountered in the data frame.")
}

# Print by excluding every row containing even one NA but keep a record of their original position
rows_without_na <- student_data[complete.cases(student_data), ]
print("Rows without any NA:")
print(rows_without_na)

# Ignore NA and print the data frame
print("Data frame ignoring NA:")
print(na.omit(student_data))
