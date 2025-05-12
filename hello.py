# Simple Python script for Jenkins demo

# Print a greeting
print("Hello from Python!")
print("This script is running from Jenkins Job C")

# Create a text file in the workspace
with open("output.txt", "w") as file:
    file.write("This file was created by the Python script\n")
    file.write("Jenkins Job C executed successfully!")

print("Created output.txt file in workspace")
