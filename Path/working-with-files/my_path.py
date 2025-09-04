import os
#To get the current working directory (cwd)
print("Current working directory:", os.getcwd())
#ABSOLUTE vs RELATIVE PATH
#Absolute path is the full address of a file (like a complete GPS location) eg for windows = C:\Users\Chris\Desktop\my_path.py    while relative path is a shortcut that starts from the current working directory eg if your working directory is C:\users\Chris\Desktop, then "my_path.py" will point to C:\Users\Chris\Desktop\my_path.py
#Absolute path example
absolute_path = r"C:\Users\ncc009\Desktop\Path\my_path.py"

#Relative path example
relative_path = "my_path.py"

print("Absolute Path:", absolute_path)
print("Relattive Path:", relative_path)

#   JOINING PATHS
import os

folder = "C:/Users/Chris/desktop"
filename = "my_path.py"

path = os.path.join(folder, filename)
print("Full path:", path)

#Checking if a file or folder exists using os.path.exists
import os

path = "my_path.py"

if os.path.exists(path):
    print("Yes, the file exists!")
else:
    print("File not found.")

#Using pathlib (Modern way). Pathlib is a modern library in python which iseasier to use than os.
from pathlib import Path

#Current working directory
print("Current directory:", Path.cwd())

#Create a path object
file = Path("myfile.txt")

#Check if it exists
print("File exists:", file.exists())

#Combine paths
folder = Path("C:/Users/Chris/Desktop")
full_path = folder / "myfile.txt"
print("Full path:", full_path)

#Navigating folders with pathlib
from pathlib import Path

#Get parent folder of current file
print("Parent folder:", Path.cwd().parent)

#List all files in a directory
for file in Path.cwd().iterdir():
    print(file)