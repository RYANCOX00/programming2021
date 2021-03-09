# A program that will save a dict object to a json file. 
# Author: Ryan Cox

import json

file = "records.json"

records = dict(name="John", age=44, student=True, amount=555.5)

def customerData(object):
    with open(file, "wt") as f:
        json.dump(object, f)
    
customerData(records)
print("Record created")