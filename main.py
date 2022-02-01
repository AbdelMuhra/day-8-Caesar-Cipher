# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
from datetime import date

name=input("Name? \n")
def welcome():
  print(f"hello {name} how can i help you today")

welcome()
ask_date = input("would you like to know the date? Y|N \n")
if ask_date == "Y":
  print(date.today())