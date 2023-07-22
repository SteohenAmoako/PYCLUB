"""1#program that ask a user for their name an their date of birth after, output their ages.

name = input("Please input your name: ")     #the input funtion helps the user to type in his name
print ("Your name is " + name)      #the print function print the string You... with the inputed name 

year_Of_Birth = int(input("input your year of birth ")) #the int function there helps the system to identify whether the input is a string or an integer
age = 2023 - year_Of_Birth
print (f"Hello ", {name}, "your age is ",{age})"""



"""2 A PROGRAM TO CALCULATE THE AREA OF A TRIANGLE ALLOWING THE USER TO GIVE THEIR OWN HEIGHT AND WIDTH 

height = float(input("please input the Height of the tirangle "))
base = float(input("please input the Base of the triangle "))
area = 0.5*base*height
print("The area of the triangle is: ",area)"""


"""WRITE A PROGRAM THAT BUILDS A PROFILE ABOUT YOU WITH THE FOLLOWING DETAILS
name,age,height,weight,email,contact,BMI"""

name = input("Input your full name: ")
age = int(input("input your age: "))
height= float(input("Input your height  "))
weight= float(input("Input your clearweight here: "))
email = input("Please input your email here ")
contact = int(input("Input your Contact number here: \n\n"))
BMI = height * weight

print(">>>>Hello ",name, "your age is ", age)
print(">>>>We hope your email ",email,)
print(">>>>Your contact ",contact,"is active")
print(">>>>Your body mass index is ", BMI)


"""Nana = 20
Kuukua = 30
if Nana is Kuukua:
    print(True)
else:
    print(False)"""
    
"""ALMIGHTY FORMULA"""
a = float (input("Input the value for a "))
b = float (input("Input the value for b "))
c = float (input("Input the value for c "))
Almighty_f = (-b + ((b**2-(4*a*c)))**(1/2))/(2*a)
print(Almighty_f)
