# A program that will seek and output a user command while defining this as a function
# Author: Ryan Cox

records = []


#FUNCTIONS
# Creating a function to request a user command.
def options ():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    command = input("Type one letter (a/v/q): ").strip() #requesting an input and striping white space. 
    return command #returning the users command out of the function. 


# Creating a function to create a list of modules.
def readmodules():
    module = [] # this will be contain contents of modules and grade read in below.
    moduleName = input("Enter a module (leave blank to quit): ").strip()

    while moduleName != "":
        modules = {} #creating a dict for the modules and grades.
        modules["Module name"] = moduleName #"Module name" is the uniform key. The value of that is the module name read in from user.
        modules["Grade"] =int(input("Enter the grade: ")) #grade is the key.  value of grade read in from the user.
        module.append(modules) #appending the "modules" dict to the module list above.  To be added to "student" below.
        moduleName = input("Enter another module (leave blank to quit): ").strip() #looping and reading in another module until input is blank. 

    return modules #returning the contents of the varibale defined above as the output of the function


# Creating a function to add new student records.
def doAdd(): 
    student = {} #single student record.
    student["Name"]=input("Enter student name: ") #creating the key and reading in its value in one go. 
    student["Modules"] = readmodules() #creating the key "module".  Its value is the empty list at readmodules. 
    records.append(student) #Adding this single student record to the master records.


# Creating a function to view student records. 
def doView():
    print(records)


#CODE

command = options() #defining command as options. This triggers the function to run. 
#command as the return value of the function now also exists outside the functions scope. They are defined seperately

while (command != "q"): # when the user doesn't decide to quit, run the loop. "q" to quit
    
    if command == "a": # user typed "a" to add a new student. 
        doAdd()
    
    elif command == "v": # user typed "v" to view the records
        doView()
    
    else:
        print("Please enter either: a, v or q") # everything else will be an incorrect input. 
    command = options() # the loop ends by starting the options function again. i.e. unless already quitted. 