# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
#name=input("Name?\n")
#location = input("Where are you?\n")

#def greet_with(name, location):
#  print(f"Hello {name}.  what is is like in {location}?")

#greet_with(name = name,location = location)



# Python Program to find the area of triangle


a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# Semi-perimeter
s = (a + b + c) / 2

#area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
