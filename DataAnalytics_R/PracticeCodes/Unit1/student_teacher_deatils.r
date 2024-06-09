#Write a R script to store student details(usn,name, 6 subjects marks ) using variables. 
# Find out their total marks and average. 
# Check whether they are pass or fail in the all subjects using logical & relational operator. 


# Student details
# Define the student variables
usn <- "1RV20CS001"
name <- "John Doe"
marks <- c(85, 78, 92, 88, 76, 81)  # Marks for 6 subjects
# Calculate total marks and average
total_marks <- sum(marks)
average_marks <- total_marks / length(marks)
# Check pass or fail in all subjects (assuming pass mark is 40)
# pass_status <- all(marks >= 40)
pass_status <- TRUE
for (mark in marks){
	if (mark < 40) {
	pass_status <- FALSE
    break
	}
}
# Display student details and results
cat("Student Details:\n")
cat("USN:", usn, "\n")
cat("Name:", name, "\n")
cat("Total Marks:", total_marks, "\n")
cat("Average Marks:", average_marks, "\n")
cat("Pass Status:", ifelse(pass_status, "Pass", "Fail"), "\n")


# Write a R script to store faculty details(name, fid,salary, no. of papers published, no of books written, no of patents published, no. of consultancy works ,no of funded projects)using variables. 
# Give weightage for their contributions(eg. For each papers published 5 points)
# Find out the faculty total points for their contributions.
# If they score >75 display that “Appraisal is good” else “not satisfactory”

# Faculty details
# Define the faculty variables
faculty_name <- "Dr. Jane Smith"
fid <- "F001"
salary <- 95000
num_papers <- 15
num_books <- 3
num_patents <- 2
num_consultancy <- 4
num_funded_projects <- 5
# Define the weightage points
points_paper <- 5
points_book <- 10
points_patent <- 8
points_consultancy <- 6
points_funded_project <- 12

# Calculate the total points for contributions
total_points <- (num_papers * points_paper) + 
                (num_books * points_book) + 
                (num_patents * points_patent) + 
                (num_consultancy * points_consultancy) + 
                (num_funded_projects * points_funded_project)

# Evaluate faculty appraisal
appraisal_status <- ifelse(total_points > 75, "Appraisal is good", "Not satisfactory")

# Display faculty details and appraisal status
cat("Faculty Details:\n")
cat("Name:", faculty_name, "\n")
cat("FID:", fid, "\n")
cat("Salary:", salary, "\n")
cat("Total Points for Contributions:", total_points, "\n")
cat("Appraisal Status:", appraisal_status, "\n")
