# # conditional statements  - it return true or false 
# if 
# elif
# else

# age = 24
# if(age >=18):
#     print("can vote") #intentation 
# else:
#     print("connot vote")


# marks=int(input("enter student marks :"))

# if(marks >= 90):
#     print("grade: A")
# elif(marks>= 80):
#     print("grade: B")
# elif(marks>= 70):
#     print("grade: C")
# else:
#     print("grade: D")



    #  nesting
# age=8
# if (age >= 18):   
#     if(age >= 80):
#        print("cannot drive")
#     else:
#         print("can drive")   
# else:
#     print("connot drive")



# num = int(input("enter number : "))

# if(num % 2 == 0):
#     print("enven number")
# else:
#     print(" odd number")    

# a = int(input("enter value of a : "))
# b = int(input("enter value of b : "))
# c = int(input("enter value of c : "))
# d = int(input("enter value of d : "))

# if( a > b and a > c and a > d ):
#     print(a,"a is gretest")
# elif(b > a and b > c and b > d ):
#     print(b,"b is gretest")
# else:
#     print(c,"c is gretest")


# num = int(input("enter num : "))

# if(num%7 == 0):
#     print(num, "is multipul of 7 ")
# else:
#     print(num, "is not a multipul of 7")    

a = int(input("enter value of a : "))
b = int(input("enter value of b : "))
c = int(input("enter value of c : "))
d = int(input("enter value of d : "))

if a > b and a > c and a > d:
    print(a, "is greatest")
elif b > a and b > c and b > d:
    print(b, "is greatest")
elif c > a and c > b and c > d:
    print(c, "is greatest")
else:
    print(d, "is greatest")
