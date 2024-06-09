
# Write a R script using function to store student details(usn,name, 6 subjects marks ) using 
# Vectors
# i) Find out their total marks and average. ii) Check whether they are pass or fail in the all subjects using logical & relational operator. 
# Lists
# Dataframes
# Matrices
# Arrays
# Factors




# Function to calculate total marks and average
calculate_marks <- function(marks) {
  total <- sum(marks)
  average <- mean(marks)
  return(list(total = total, average = average))
}

# Function to check pass/fail status
check_pass_fail <- function(marks, pass_threshold = 40) {
  pass_status <- all(marks >= pass_threshold)
  return(pass_status)
}

# Vectors
usn <- c("CS001", "CS002", "CS003", "CS004")
names <- c("Alice", "Bob", "Charlie", "David")
subject1_marks <- c(75, 80, 65, 70)
subject2_marks <- c(85, 90, 75, 80)
subject3_marks <- c(80, 75, 85, 90)
subject4_marks <- c(70, 85, 80, 75)
subject5_marks <- c(90, 95, 80, 85)
subject6_marks <- c(85, 80, 90, 95)

# Calculate total marks and average for each student
total_marks <- subject1_marks + subject2_marks + subject3_marks + 
               subject4_marks + subject5_marks + subject6_marks
average_marks <- total_marks / 6

# Check pass/fail status for each student
pass_fail_status <- check_pass_fail(cbind(subject1_marks, subject2_marks, 
                                          subject3_marks, subject4_marks, 
                                          subject5_marks, subject6_marks))

# Display results
cat("Using Vectors:\n")
for (i in 1:length(usn)) {
  cat("Student:", names[i], "- USN:", usn[i], "\n")
  cat("Total Marks:", total_marks[i], "\n")
  cat("Average Marks:", average_marks[i], "\n")
  cat("Pass/Fail:", ifelse(pass_fail_status[i], "Pass", "Fail"), "\n")
}

# Lists
student_list <- list(usn = usn, names = names, 
                     subject_marks = list(subject1_marks, subject2_marks, 
                                          subject3_marks, subject4_marks, 
                                          subject5_marks, subject6_marks))

# Calculate total marks and average for each student
total_marks <- sapply(student_list$subject_marks, sum)
average_marks <- sapply(student_list$subject_marks, mean)

# Check pass/fail status for each student
pass_fail_status <- sapply(student_list$subject_marks, check_pass_fail)

# Display results
cat("\nUsing Lists:\n")
for (i in 1:length(student_list$usn)) {
  cat("Student:", student_list$names[i], "- USN:", student_list$usn[i], "\n")
  cat("Total Marks:", total_marks[i], "\n")
  cat("Average Marks:", average_marks[i], "\n")
  cat("Pass/Fail:", ifelse(pass_fail_status[i], "Pass", "Fail"), "\n")
}

# Dataframe
student_df <- data.frame(USN = usn, Name = names, 
                         Subject1 = subject1_marks, Subject2 = subject2_marks, 
                         Subject3 = subject3_marks, Subject4 = subject4_marks, 
                         Subject5 = subject5_marks, Subject6 = subject6_marks)

# Calculate total marks and average for each student
student_df$total_marks <- rowSums(student_df[, -c(1:2)])
student_df$average_marks <- rowMeans(student_df[, -c(1:2)])

# Check pass/fail status for each student
student_df$pass_fail_status <- apply(student_df[, -c(1:3)], 1, check_pass_fail)

# Display results
cat("\nUsing Dataframes:\n")
print(student_df)

# Matrices
student_matrix <- matrix(c(usn, names, subject1_marks, subject2_marks, subject3_marks, subject4_marks, subject5_marks, 
                            subject6_marks), nrow = 4, byrow = FALSE)