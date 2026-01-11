# marks =[ 12, 34, 45, 56, 67, 98, 96]
# marks.append(67)
# marks.sort( reverse =True)
# print((marks))

# list =[ 2,1,3]
# print(list.append(4)) # this append method is not creatinh any new  list   same for short
# print(list.sort())
# print(list)


# write the  program  to check if a list contain  a pailbdrome of elements (Hint: use copy() method)

# list = [1,2,3,2,1]

# list2 = list.copy()
# list2.reverse()

# if list == list2 :
#     print("it is palamdro")
# else:
#     print("not a palamdro")    


grade=("A", "A", "D", "D", "A" ,"B" ,"B", "C","D" ,"C", "B")
print(grade.count("A"))
print(type(grade))


grade1=["A", "A", "D", "D", "A" ,"B" ,"B", "C","D" ,"C", "B"]
grade1.sort()
print(grade1)