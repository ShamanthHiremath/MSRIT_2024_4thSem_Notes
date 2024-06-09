# Set seed for reproducibility 
set.seed(110) 

# Create example data 
data <- matrix(rnorm(50, 0, 5), nrow = 5, ncol = 5) 

# Column names 
colnames(data) <- paste0("col", 1:5) 
rownames(data) <- paste0("row", 1:5) 

# Draw a heatmap 
heatmap(data)
