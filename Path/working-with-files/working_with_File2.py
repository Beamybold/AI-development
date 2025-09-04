
1.#Setting up (ie working inside a folder)

from pathlib import Path

workspace = Path("Ade_files")
workspace.mkdir(exist_ok=True)
file_path = workspace / "my_work.py"
file_path

"""Create a file: There are 2 ways of creating file
w (write): To create the file if it doesn't and overwrites it if it does
x (exclusive create): This creates the file only if it doesn't exist and report error if it does. (Safer if you don't want to overwrte by mistake)   """

#create or overwrite using 'w'
f = open(file_path, "w", encoding="utf-8")
f.write("#Print(Hello World!)\n")
f.close()

#safe create using x

# f = open(file_path / "my_work.py", "x", encoding="utf-8") #This wasn't created but return error because it is already existing
# f = open (workspace / "new_Doc.py", "x", encoding="utf-8")
# f.write("#Print(Hello World!)\n")
# f.close()

#Open a file to prepares it for reading or writing: 
#open for writing again to overwrite
f = open(file_path, "w", encoding="utf-8")
f.write("I have gone past Hello World.\n")
f.close()

#To write in new content use "a" to append
f = open(file_path, "a", encoding="utf-8")
f.write("Add this to my write up\n")
f.close


#write to  a file: To put texts into the file. write() doesn't add newlines automatically except you add \n.
f=open(file_path, "w", encoding="utf-8")
f.write("Shopping List:\n")
f.write("-Rice\n")
f.write("-Sphag\n")
f.close()

#append to a file; It adds to the end without deleting what is already there.
f = open(file_path, "a", encoding="utf-8")
f.write("-Chips\n")
f.write("-Sweet\n")
f.close()

""" #Read from a file:
            read() - whole file as one string
            read(n) - f n characters
            readline() - one line
            readlines() - list ofall lines"""

#reading the whole file using "read"
f = open(file_path, "r", encoding="utf-8")
content = f.read()
f.close()
print(content)

#read line-by-line
f = open(file_path, "r", encoding="utf-8")
# cont = f.readline()
# print(cont)
print("First line:", f.readline().rstrip().upper())
print("Second line:", f.readline().lstrip())
f.close()

#Read as a list of lines
f = open(file_path, "r", encoding="utf-8")
lines = f.readlines()
f.close()
print("Lines list:", [line.rstrip() for line in lines])

#iterate over lines (memory-friendly)
f = open(file_path, "r", encoding="utf-8")
for line in f:
    print("->", line.rstrip())
f.close()

""" #close the file: 
        close files opened with open(...)
        it flushes(saves) any buffered data to disk
        it releases the OS handle so other programs can use the file
        it avoids weird bugs (especially on windows)
        
BETTER WAY OF DOING THE ABOVE
 close file

use with open(...) as f: (best practice)
The "with" statement automatically closes the file even if an error happens."""
with open(file_path, "w", encoding="utf-8") as f:
    f.write("My Todo List:\n")
    f.write(" <-Revise Python file handling\n")
    f.write(" <-Practice error handling within a function")
    f.write(" <-Practice JSON & CSV\n")

#Append safely
with open(file_path, "a", encoding="utf-8") as f:
    f.write(" <-Build a small project\n")

""" "b" - binary(combine e.g 'rb') like images and videos
    "t" - text(default)
    "r+" - read and write (no truncate). It update in place

WHEN THINGS GO WRONG:When files don't exist or when we don't have the permission to read them. 
    Python will throw us error but we can gracefully handle them; like this
"""
from pathlib import Path

workspace = Path("Ade_files")
workspace.mkdir(exist_ok=True)
#Try to read an unexisting filetry:
try:
    with open(workspace / "new_file.txt", "r") as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
    print("Let's create it first!")
#Now create the file
with open(workspace / "new_file.txt", "w") as f:
    f.write("Now created" ) 
print("Done")

#To check if file exist before using them
from pathlib import Path

workspace = Path("Ade_files")
file_path = workspace / "my_work.py"

if file_path.exists(): #To check if the file exists
    print(f"Found the file: {file_path.name}")
    #Get some infomation about the file
    file_size = file_path.stat().st_size
    print(f"File size: {file_size} bytes")

#To read and show the content
    with open(file_path, "r", encoding="utf-8" ) as f:
        content = f.read()
        print(f"Content preview: {content[:50]}....") #First 50 characters

else:
        print(f"File{file_path.name} doesn't exist.")
        print("You might want to create it first!")

#If "my_work.py" exists it prints for "if" output and print ""


#working with Json files: JSON files are great for storing structued data like dicts and lists ie like a way of saving python data to a file

import json
from pathlib import Path
workspace = Path("Ade_files")
#Ceate some student data (A mini database)
students_data = {
    "Name": "Omofoloarin",
    "Age": 17,
    "Courses": ["Python", "Data Science", "Web Development"],
    "Grade": {"Python": "A", "Data Science": "B+", "Web Development": "A-"},
    "is_graduated": False
}

#Save the
json_file = workspace / "student_data.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(students_data, f, indent=2) # indent=2 makes it pretty and readable
    print("Student data saved to JSON file")
#Now to read
with open(json_file, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print("\nData read from JSON file:")
print(f"Student name: {loaded_data['Name']}")
print(f"Age: {loaded_data['Age']}")
print(f"Courses: {', '.join(loaded_data['Courses'])}")
print(f"Python grade: {loaded_data['Grade']['Python']}")


#working with CSV files-Spreadsheet(data in rows and columns) like data




