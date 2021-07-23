import json

"""
JSON can be consider as a communication concept between any language. For example,
It can be create or modified data using the Python and store in a file. Then we can re-load 
that data using the java and do required things 
"""

data = {"Malitha": {
    "Address": "No:12, Kandy Road, Pilamathalawa",
    "Telephone": 1544545454,
    "Email": "maitha@gmail.com"},
    "Nike": {
        "Address": "No:25/A, Kandy Road, Pilamathalawa",
        "Telephone": 564654646,
        "Email": ""}
}

json_str = json.dumps(data)  # Dump as string
# print(json_str)

file = open("dump.json", "w")
json.dump(data, file)
file.close()

read_file = open("dump.json", "r")
load_data = json.loads(read_file.read())   # Load data again as a dictionary and do your changes
print("Loaded data : \n")
print(load_data)
