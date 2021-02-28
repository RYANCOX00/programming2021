# A program that will seek and output a user command while defining this as a function
# Author: Ryan Cox


def options ():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    command = input("Type one letter (a/v/q): ").strip() #requesting an input and striping white space. 
    return command #returning the users command out of the function. 

command = options() #defining command as options. This triggers the function to run. 
#command as the return value of the function now also exists outside the functions scope. They are defined seperately

print("you chose {}".format(command)) #outputting the users command