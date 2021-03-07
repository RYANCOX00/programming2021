# A program that will seek and output a user command while defining this as a function
# Author: Ryan Cox

records = []

def options ():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    command = input("Type one letter (a/v/q): ").strip() #requesting an input and striping white space. 
    return command #returning the users command out of the function. 

def doAdd(): #defining a function to print, to be used later in adding.
    print("in adding")

def doView():#defining a function to print, to be used later in viewing. 
    print("in viewing")

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