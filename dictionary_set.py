# doctionary


# info= { 
#     "key": "value",
#     "name":"shradha",
#     "learning":"coding",
#     "age":22,
#     "is_adult":True ,
#     "marks" : 94.4
# }

# print(type(info))
# print(info["learning"])  

student = {
"name": "rahul kumar",
"subject":{
    "phy":97,
    "chem":92,
    "math":95,
}

}

# print(len(list(student.values())))
# print(student.items())
# print(student["name1"]) # this line give erorr
print(student.get("name2")) # this line give me   -> none

