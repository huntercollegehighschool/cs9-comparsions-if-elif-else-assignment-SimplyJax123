'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):
'''


month = str(input("Enter a month: "))

if month == "September" or "April" or "June" or "November":
  print("There are 30 Days in this month")
elif month == "January" or "March" or "May" or "July" or "August" or "December":
  print("There are 31 Days in this month")
elif month == "February":
  print("There are 28 or 29 Days in this month")
else:
  print("this is not a month")