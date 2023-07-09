# """1. While loop problems"""

# #a
# a = 0
# while a < 11:
#   print(a ** 2)
#   a += 1

# #b
# a = 11
# while a > 0:
#   print(a)
#   a -= 1

# #c
# sum = 0
# while True:
#   num = int(input("input zero(0) to break: "))
#   if num == 0:
#     break
#   sum += num
# print("End")

# #d
# numbers = []

# print("Enter numbers to compare (press 0 to finish):")

# while True:
#   try:
#     num = float(input("Enter a number: "))

#     if num == 0:
#       break

#     numbers.append(num)
#   except ValueError:
#         print("Please enter a valid number.")

# if numbers:
#   smallest = min(numbers)
#   largest = max(numbers)

#   print(f"Largest value: {largest}")
#   print(f"Smallest value: {smallest}")
# else:
#   print("No numbers were entered.")

#e
numbers = []

print("Enter numbers to compare (press 0 to finish):")

while True:
  try:
    num = float(input("Enter a number: "))

    if num == 0:
      break

    numbers.append(num)
  except ValueError:
        print("Please enter a valid number.")

if numbers:
  total_sum = sum(numbers)
  count = len(numbers)
  mean = total_sum / count
  print(f"Mean value is: {mean}")
else:
  print("No numbers were entered.")



# """2. For loop problems"""

# #a
# for i in range(-10,0):
#   print(i)

# #b
# num = input("Enter a number: ")

# try:
#   num = int(num)

#   sum_of_numbers = 0

#   for i in range(1, num + 1):
#     sum_of_numbers += i

#   print(f"The sum of numbers from 1 to {num} is: {sum_of_numbers}")
# except ValueError:
#   print("Please enter a valid number.")

# #e
# num = int(input("Enter a number: "))
# factorial = 1

# for i in range(1, num + 1):
#   factorial *= i

# print(f"The factorial of {num} is: {factorial}")



# """3. List/Dictionary problems"""

# #a
# list = [i for i in range(10, 50, 5)]
# print(list)

# #b
# squared_list = [i**2 for i in list]
# print(squared_list)

# #c
# greater_list = [i for i in squared_list if i > 100]
# print(greater_list)

# #d
# dictionary = {"Sedan": 1500,
#               "SUV": 2000,
#               "Pickup": 2500,
#               "Mnivan": 1600,
#               "Van": 2400,
#               "Semi": 13600,
#               "Bicycle": 7,
#               "Motorcycle": 110}
# weight = []
# names = []

# for key, value in dictionary.items():
#   weight.append(value)
#   names.append(key)
  
# b_weight = [i for i in weight if int(i) < 5000]
# l_weight = [i for i in weight if int(i) > 2000]

# print(b_weight)
# print(l_weight)

# #e
# upper_names = [i.upper() for i in names]

# print(upper_names)
