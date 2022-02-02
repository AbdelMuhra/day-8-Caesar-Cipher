# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
name=input("Name?\n")
location = input("Where are you?\n")

def greet_with(name, location):
  print(f"Hello {name}.  what is is like in {location}?")

greet_with(name = name,location = location)
