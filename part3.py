'''
______
PART 3
______
Write a program that asks the user to input one integer. The program will then print two strings, one stating if it's positive, negative, or zero, and another that states whether or not is is divisible by 3. (Hint: to check divisibility by 3, you will find using the modulus(%) operation very helpful.)

3 examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

'''

number1 = int(input("Enter a number: "))

#first string
if number1 > 0:
  print("positive")
elif number1 < 0:
  print("negative")
elif number1 == 0:
  print("zero")

#second string
if number1 % 3 == 0:
  print("divisible by 3")
else:
  print("not divisible by 3")