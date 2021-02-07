# A program to test the different type of variables.
# We will use format to include many pre-defined variables in one sentence.
# Author:  Ryan Cox


# Defining some variables. 
i = 10
fl = 2.5
status = True
message = "Python is awsome"
list =[]


# Inputing a variety of variables into a sentence using the formated function.
# The method is to input the variable name as a string,
# identify the type of variable,
# and finanly identify the value of that variable. 
print ("Variable {} is of type {} and value: {}".format("i", type(i), i))
print ("Variable {} is of type {} and value: {}".format("fl", type(fl), fl))
print ("Variable {} is of type {} and value: {}".format("status", type(status), status))
print ("Variable {0} is of type {1} and value: {2}".format("message", type(message), message))
print ("Variable {} is of type {} and value: {}".format("list", type(list), list))


# As we see under line 26, we can order of the variables within the sentence from those set out in the format function. 
# This would be handy where you have not placed them in order, or where you use the same variable twice in a sentence. 