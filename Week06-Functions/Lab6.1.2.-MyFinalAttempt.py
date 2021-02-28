# A program that will input student records and view student records.
# Author: Ryan Cox

records = []

#FUNCTIONS
# Creating a function to request an input from a under from a list of parameters.
def options ():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    command = input("Type one letter (a/v/q): ").strip() #requesting an input and striping white space. 
    return command #returning the users command out of the function. 

# Creating a function to input modules and grades from a user and add them to a dict. This dict to be used inside the student records dict.
def subDictModule():
    modules = [] # master module list for each student record. Forms the begining of a value of "Modules" on line 35. 
    
    module1 =input("Enter the first module (leave blank to exit): ") # reading in a module from the user. Done outside the loop to allow for exit if selected in error.
               
    while module1 != "": # running a loop until the user indicate exit by leaving the module input blank.  
        moduleRecord ={} # single module dict for each student record. This sub-dict can have multiple modules.
        moduleRecord["Module Name"] = module1  # setting the key for the read in module above as "Module Name", and adding both the key and value to the dict.
        moduleRecord["Grade"] = input("Enter the grade: ") # reading in grade for this module and adding both the key and grade value to the dict. 
        modules.append(moduleRecord) # adding this dict to the master module list above. 
        module1 = input("Enter another module (leave blank to exit): ").strip() # done last within the loop to allow for exit. 
    
    return modules
    

def addName():
    studentRecord = {} # Dict for each student
    studentRecord["Student name"] = input("Enter the students name: ") # Name of student.
    studentRecord["Modules"] = subDictModule() # Module as a opening key. The value is sourced from line 17 -29.
    records.append(studentRecord)


def doView():
    print(records)


#CODE
command = options() #defining command as options. This triggers the function to run. 
#command as the return value of the options function now exists outside the functions scope. They are defined seperately


# The code is now run, feeding from the defined functions. 
while command != "q":  # when "options" is not selected "q".
    
    if command == "a": # user typed "a" to add a new student.
        addName() 

    elif command == "v": # user typed "v" to view the records
        doView()
        
    else:
        print("Please enter either: a, v or q") # everything else will be an incorrect input. 

    command = options()