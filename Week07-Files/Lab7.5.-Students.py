# A program that will input student records and view student records.
# Author: Ryan Cox


import json
records = []
file ="studentReocrds.json"


# FUNCTIONS

# Saving records to json file. 
def doWrite(object): # initiated from doSave below.  Object is the records list above. 
    with open(file, "wt") as f: # opening file to write to. File defined above.
        json.dump(object,f) # Dumping contents of records to the file. 


#Reading in records from json file.
def readDict(): # initiated from doLoad below. This will read in the contents and save its as a new variable records i.e. overwrite above list.
    with open(file, "rt") as f: # opening file as defined above.
        data = json.load(f) # loading from json file 
        return data #returning and overwriting records. 


# Creating a function to request an input from a under from a list of parameters.
def options ():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(l) Load students")
    print("\t(s) Save students")
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


def doSave(): # initiated from the user input "s"
    doWrite(records) #this runs the json function above using the records list as the input object.
    print("Records saved")


def doLoad():  # initiated from user input "l"
    global records  #this will create a new global variable.
    records = readDict() #running the json function above and saving the contents under records (overwritten). 
    print("Records loaded")



#CODE
command = options() #defining command as options. This triggers the function to run. 
#command as the return value of the options function now exists outside the functions scope. They are defined seperately


# The code is now run, feeding from the defined functions. 
while command != "q":  # when "options" is not selected "q".
    
    if command == "a": # user typed "a" to add a new student.
        addName() 

    elif command == "v": # user typed "v" to view the records
        doView()
    
    elif command =="l":
        doLoad()

    elif command =="s":
        doSave()
        
    else:
        print("Please enter either: a, v or q") # everything else will be an incorrect input. 

    command = options()