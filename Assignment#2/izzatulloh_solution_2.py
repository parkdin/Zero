# """1. if/elif/else problems"""

# #a

# def lastDigit(m):
#   last_digit = m % 10
#   return last_digit

# last_digit = lastDigit(123)
# print(f"last digit is: {last_digit}")


# #b

# def kgs_to_pounds(kgs):
#   pound = kgs * 2.2046
#   return pound

# def pounds_to_kgs(pound):
#   kilograms = pound / 2.2046
#   return kilograms

# choice = int(input("Enter '0' for kgs to pound and '1' for pound to kgs: "))

# if choice == 0:
#   kilograms = float(input("Enter weight in kilograms:"))
#   pound = kgs_to_pounds(kilograms)
#   print(f"{kilograms}kilograms is {pound} pounds.")

# elif choice == 1:
#   pound  = float(input("Enter weight in pounds: "))
#   kilograms = pounds_to_kgs(pound)
#   print(f"{pound}pounds is {kilograms} kilograms")

# else:
#   print("Invalid choice. Enter 0 or 1")


# #c

# def celsius_to_fahrenheit(celsius):
#   fahrenheit = celsius * 1.8 + 32
#   return fahrenheit

# def fahrenheit_to_celsius(fahrenheit):
#   celsius = (fahrenheit - 32) * 5/9
#   return celsius

# choice = int(input("Enter '0' Celsius to Fahrenheit or '1' to Fahrenheit to Celsius: "))

# if choice == 0:
#   celsius = float(input("Enter Celsius: "))
#   fahrenheit = celsius_to_fahrenheit(celsius)
#   print(f"{celsius} in degrees in Celsius is {fahrenheit} degrees in Fahrenheit.")

# elif choice == 1:
#   fahrenheit = float(input("Enter Fahrenheit: "))
#   celsius = fahrenheit_to_celsius(fahrenheit)
#   print(f"{fahrenheit} degrees in Fahrenheit is equal to {celsius} degrees in Celsius.")

# else:
#   print("Wrong input. Enter 0 or 1!")


# #d


# #e

# def largest_number(m, n):
#   if m > n:
#     return m
#   else:
#     return n

# while True:
#   try:
#     m = int(input("Enter first number to compare: "))
#     n = int(input("Enter second number to compare: "))

#     if m == 0:
#       break
#     if n == 0:
#       break

#   except ValueError:
#         print("Please enter a valid number.")

# largest_num = largest_number(m, n)

# print(f"Largest number is: {largest_num}")


#f

def exam_score(m):
  if m >= 95:
    return "A+"
  elif m >= 85:
    return "A"
  elif m >= 80:
    return "B+"
  elif m >= 70:
    return "B"
  elif m >= 60:
    return "C+"
  elif m >= 50:
    return "C"
  elif m >= 40:
    return "D+"
  elif m >= 30:
    return "D"
  elif m >= 20:
    return "E+"
  elif m >= 10:
    return "E"
  else:
    return "F"

student_score = exam_score(100)
print(f"Your exam score is {student_score}")