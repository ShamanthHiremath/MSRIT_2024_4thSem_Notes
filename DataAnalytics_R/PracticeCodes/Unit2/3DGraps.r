# Define the cone function
cone <- function(x, y) {
  sqrt(x^2 + y^2)
}

# Prepare variables
x <- y <- seq(-1, 1, length = 30)
z <- outer(x, y, cone)

# Plot the 3D surface
persp(x, y, z,
      main = "Perspective Plot of a Cone",
      zlab = "Height",
      theta = 30, phi = 15,
      col = "orange", shade = 0.4)