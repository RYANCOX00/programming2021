# A program to print out a students results that are saved as a dictionary variable. 
# Author: Ryan Cox


#Creating the dict 'grades'.
grades = {
    "Student": "Mary",
    # 'modules' key has a list of values.
    # within the list is 2 seperate dicts (allows for the duplication).
    # courseName and grade are the keys in both dicts.
    "modules":[
            {"courseName": "English",
                "grade": 80},
            {"courseName": "History",
                "grade":99}
                        ] #end of list
                    } #end of overarching dict. 
    

    #printing student name from the key 'Student'
print("Student: {}".format(grades["Student"]))


# creating the temporary dict variable - 'module' in the modules key.
for module in grades["modules"]:
    # It will search the values of keys courseName and grades in the two seperate sub-dicts. 
    print("\t {} \t {}".format(module["courseName"], module["grade"]))
