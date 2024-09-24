# import math
# import random

# ##2.1
# # Write a program that asks your name and then greets you by your name: Examples:
# # If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
# # If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!.
#
# name = input("Enter your name: ")
# print(f"Hello {name}")
#
# ##2.2
# # Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
#
# radius = float(input("Enter your radius: "))
# area = math.pi * radius**2
# print(f"The area is {area:.2f}")
#
# ##2.3
# # Write a program that asks the user for the length and width of a rectangle.
# # The program then prints out the perimeter and area of the rectangle.
# # The perimeter of a rectangle is the sum of the lengths of each four sides.
#
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
# perimeter = (length + width) * 2
# area = length * width
# print(f"The perimeter is {perimeter:.2f},The area is {area:.2f}")
#
# ##2.4
# # Write a program that asks the user for three integer numbers.
# # The program prints out the sum, product, and average of the numbers.
#
# num1 = float(input("input number1: "))
# num2 = float(input("input number2: "))
# num3 = float(input("input number3: "))
# sum = num1 + num2 + num3
# product = num1 * num2 * num3
# average = sum / 3
# print(f"The sum is {sum:.2f},The product is {product:.2f},The average is {average:.2f}")
#
# ##2.5
# # Write a program that asks the user to enter a mass in medieval units:
# # talents (leiviskä), pounds (naula), and lots (luoti).
# # The program converts the input to full kilograms and grams
# # and outputs the result to the user:
# # One talent is 20 pounds.
# # One pound is 32 lots.
# # One lot is 13,3 grams.
#
# talents = float(input("input talents: "))
# pounds = float(input("input pounds: "))
# lots = float(input("input lots: "))
# total = lots * 13.3 + pounds * 13.3 * 32 + talents * 13.3 * 32 * 20
# kilograms = total // 1000
# grams = total % 1000
# print(f"The weight in modern units: \n{kilograms:.0f} kilograms and {grams:.2f} grams.")
#
# ##2.6
# # Write a program that draws two random combinations of numbers for a combination lock:
# # a 3-digit code where each number is between 0 and 9.
# # a 4-digit code where each number is between 1 and 6.
#
# n1 = random.randint(0, 9)
# n2 = random.randint(0, 9)
# n3 = random.randint(0, 9)
# code1 = n1 , n2 , n3
# print(f'code1 is : {code1}')
# nn1 = random.randint(1, 6)
# nn2 = random.randint(1, 6)
# nn3 = random.randint(1, 6)
# nn4 = random.randint(1, 6)
# code2 = nn1 , nn2 , nn3 , nn4
# print(f'code2 is : {code2}')
#
#
# #3.1
# # Write a program that asks a fisher the length of a zander in centimeters.
# # If the zander does not fulfill the size limit,
# # the program instructs to release the fish back into the lake
# # and notifies the user of how many centimeters below the size limit the caught fish was.
# # A zander must be 42 centimeters or longer to meet the size limit.
#
# length = float(input("The length of a zander in centimeters is: "))
# if length >= 42:
#     print("You can keep the fish.")
# else:
#     print("A zander must be 42 centimeters or longer to meet the size limit.\n"
#            "Please release the fish back into the lake.")
#
#
# ##3.2
# # Write a program that asks the user to enter the cabin class of a cruise ship
# # and then prints out a written description according to the list below.
# # You must use an if/elif/else structure in your solution.
# ##  LUX: upper-deck cabin with a balcony.
# ##  A: above the car deck, equipped with a window.
# ##  B: windowless cabin above the car deck.
# ##  C: windowless cabin below the car deck.
# ##  If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.
#
# cabin_class = input("Please enter the cabin class of a cruise ship:")
# if cabin_class == "LUX":
#     print("LUX: upper-deck cabin with a balcony.")
# elif cabin_class == "A":
#     print("A: above the car deck, equipped with a window.")
# elif cabin_class == "B":
#     print("B: windowless cabin above the car deck.")
# elif cabin_class == "C":
#     print("C: windowless cabin below the car deck.")
# else:
#     print('Invalid cabin class.')
#
#
#
#
# ##3.3
# # Write a program that asks for the biological gender and hemoglobin value (g/l).
# # The program the notifies the user if the hemoglobin value is low, normal or high.
# ##  A normal hemoglobin value for adult females is between 117-155 g/l.
# ##  A normal hemoglobin value for adult males is between 134-167 g/l.
#
# gender = input("Please enter your biological gender(Male/Female): ")
# if gender == "Male":
#     value = float(input("Please enter your hemoglobin value: "))
#     if value > 155:
#         print("Your hemoglobin is high.")
#     elif value < 117:
#         print("Your hemoglobin is low.")
#     else:
#         print("Your hemoglobin is normal.")
# elif gender == "Female":
#     value = float(input("Please enter your hemoglobin value: "))
#     if value > 167:
#         print("Your hemoglobin is high.")
#     elif value < 134:
#         print("Your hemoglobin is low.")
#     else:
#         print("Your hemoglobin is normal.")
# else:
#     print("Input error.")
#
#
# ##3.4
# # Write a program that asks the user to enter a year
# # and notifies the user whether the input year is a leap year.
# # A year is a leap year if it is divisible by four.
# # However, years divisible by 100 are leap years only if they are also divisible by 400.
#
# year = int(input("Enter year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("It is a leap year.")
# else:
#     print("It is not a leap year.")
#
#
#
# ##4.1
# #Write a program that uses a while loop to print out all numbers
# #divisible by three in the range of 1-1000.
#
# number = 1
# while number <= 1000:
#     if number % 3 == 0:
#         print(number)
#     number += 1
#
#
# ##4.2
# #Write a program that converts inches to centimeters until the user inputs a negative value.
# #Then the program ends.
#
# inches = float(input("Enter inches: "))
# while inches > 0:
#     centimeters = inches * 2.54
#     print(f"{inches} inches = {centimeters} centimeters")
#     inches = float(input("Enter inches: "))
# print("program ends")
#
#
# ##4.3
# # Write a program that asks the user to enter numbers until they enter an empty string to quit.
# # Finally, the program prints out the smallest and largest number from the numbers it received.
# # The first way:
# max_number = None
# min_number = None
# number = input("Enter numbers: ")
#
# while number != "":
#     number = float(number)
#     if  max_number is None or max_number < number :
#         max_number = number
#     if min_number is None or min_number > number :
#         min_number = number
#     number = input("Enter numbers: ")
#
# print(f"The max_number is {max_number},the min_number is {min_number}")
#
# #  The second way:
# numbers = []
# number = input("Enter numbers: ")
# while number != "":
#     numbers.append(number)
#     number = input("Enter numbers: ")
#
# print(numbers)
# number_max = max(numbers)
# number_min = min(numbers)
# print(number_max, number_min)
#
#
# ##4.4
# # Write a game where the computer draws a random integer between 1 and 10.
# # The user tries to guess the number until they guess the right number.
# # After each guess the program prints out a text: Too high, Too low or Correct.
# # Notice that the computer must not change the number between guesses.
#
# random_num = random.randint(1, 10)
# while True:
#     guess_num = int(input("Guess a number between 1 and 10: "))
#     if guess_num < random_num:
#         print("Too low!")
#     elif guess_num > random_num:
#         print("Too high!")
#     else:
#         print("Correct!")
#         break
#
#
# ##4.5
# # Write a program that asks the user for a username and password.
# # If either or both are incorrect, the program ask the user to enter the username and password again.
# # This continues until the login information is correct or wrong credentials have been entered five times.
# # If the information is correct, the program prints out Welcome.
# # After five failed attempts the program prints out Access denied.
# # The correct username is python and password rules.
#
# T_username = "python"
# T_password = "rules"
# time = 0
# while time < 5:
#     time += 1
#     username = input("Enter your name: ")
#     password = input("Enter your password: ")
#     if username == T_username and password == T_password :
#         print("Welcome!")
#         break
#     elif ( username != T_username or password != T_password )and time != 5:
#         print("Try Again")
#     else:
#         print("Access denied")
#
#
# ##4.6
# # Implement an algorithm for calculating an approximation for the value of pi (π).
# # Let's assume that A is a unit circle. A unit circle has the radius of one
# # and it is centered at the origin (0,0). Smallest possible square B is drawn around the unit circle
# # so that circle A is completely inside the square.
# # The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1).
# # If a large number of random points are scattered inside the square,
# # the fraction of points that fall inside the circle A correlates with
# # the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4.
# # This can be used as a simple method for calculating an approximation of the value of pi:
# # Let's generate a large number of random points, such as one million, inside square B.
# # Let N be the total number of random points.
# # Each point inside the square is tested for whether it resides inside circle A.
# # Let n be the total number of points that fall inside circle A.
# # Now we have n/N≈π/4, and from that we get π≈4n/N.
# # Write a program that asks the user how many random points to generate,
# # and then calculates the approximate value of pi using the method explained above.
# # At the end, the program prints out the approximation of pi to the user.
# # (Notice that it is easy to test if a point falls inside circle A by testing
# # if it fulfills the inequation x^2+y^2<1.).
#
# point_all = 0
# point_circle = 0
# point_user = int(input("How many points do you want? "))
#
# while point_all < point_user:
#     point_all = point_all + 1
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#     if x ** 2 + y ** 2 <= 1:
#         point_circle = point_circle + 1
#
# pi = 4 * point_circle / point_user
# print(f"The approximation of pi is {pi:.10f}")
#
#
#
# ## 5.1
# # Write a program that asks the user how many dice to roll.
# # The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
#
# times = int(input("How many times would you like to roll? : "))
# sum_of_numbers = 0
# numbers =[]
# for i in range(times):
#     roll = random.randint(1, 6)
#     numbers.append(roll)
#     sum_of_numbers = sum_of_numbers + roll
# print(numbers)
# print(sum_of_numbers)
#
#
# ## 5.2
# # Write a program that asks the user to enter numbers until they input an empty string to quit.
# # At the end, the program prints out the five greatest numbers sorted in descending order.
# # Hint: You can reverse the order of sorted list items by using the sort method
# # with the reverse=True argument.
#
# numbers = []
#
# while True:
#     user_number = input("Enter a number: ")
#     if user_number == "":
#         break
#     numbers.append(int(user_number))
#
# numbers.sort(reverse=True)
# first_five_numbers = numbers[:5]
#
# print(first_five_numbers)
#
# ## 5.3
# # Write a program that asks the user for an integer and tells if the number is a prime number.
# # Prime numbers are number that are only divisible by one or the number itself.
# #   For example, 13 is a prime number as it can only be divided by 1 or 13
# #   so that the result is an integer.
# #   On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
# user_num = int(input("Enter a number: "))
# divided_by = []
#
# if user_num <= 1 :
#     print("Your number is not a prime number.")
#
# elif user_num in { 2,3,5 }:
#     print("Your number is a prime number.")
#
# elif user_num > 5:
#     for i in range(2,user_num,1):
#         if user_num % i == 0 :
#             divided_by.append(i)
#             break
#
#     if len(divided_by) == 0 :
#         print("Your number is a prime number.")
#     else:
#         print("Your number is not a prime number.")
#
#
# ## 5.4
# # Write a program that asks the user to enter the names of five cities one by on
# # (use a for loop for reading the names) and stores them into a list structure.
# # Finally, the program prints out the names of the cities one by one, one city per line,
# # in the same order they were read as input.
# # Use a for loop for asking the names and a for/in loop to iterate through the list.
#
# cities = []
#
# for a in range(5):
#     city = input("Enter a city: ")
#     cities.append(city)
#
# for city in cities:
#     print(city)
#
#
# ## 6.1
# # Write a function that returns a random dice roll between 1 and 6.
# # The function should not have any parameters.
# # Write a main program that rolls the dice until the result is 6.
# # The main program should print out the result of each roll.
#
# def roll():
#     dice = random.randint(1,6)
#     return dice
#                            # result = roll()  # Start by rolling the dice
# while True:                # while result != 6:
#     result = roll()        #     print(result)  # Print the current roll
#     if result == 6 :       #     result = roll()  # Roll the dice again
#         print(result)      # print(result)  # Print the final result when it's 6
#         break
#     print(result)
#
#
# ## 6.2
# # Modify the function above so that it gets the number of sides on the dice as a parameter.
# # With the modified function you can for example roll a 21-sided role-playing dice.
# # The difference to the last exercise is that the dice rolling
# # in the main program continues until the program gets the maximum number on the dice,
# # which is asked from the user at the beginning.
#
# def roll(sides):
#     dice = random.randint(1, sides)
#     return dice
#
# dice_max = int(input("Enter a number: "))
#
# while True:
#     result = roll(dice_max)
#
#     if result == dice_max :
#         print(result)
#         print("You rolled the maximum number! ")
#         break
#     print(result)
#
# ## 6.3
# # Write a function that gets the quantity of gasoline in American gallons and
# # returns the number converted to litres. Write a main program that asks for
# # a volume in gallons from the user and converts the value to liters.
# # The conversion must be done by using the function.
# # Conversions continue until the user inputs a negative value.
#
# def gasoline(gallons):
#     litres = gallons * 3.78541
#     return litres
#
# user_gallons = float(input("Enter number of gasoline in American gallons : "))
#
# while user_gallons >= 0 :
#     user_litres = gasoline(user_gallons)
#     print(f"{user_gallons} gallons = {user_litres:.3f} litres.")
#     user_gallons = float(input("Enter number of gasoline in American gallons : "))
#
# print("Error input.")
#
#
# ## 6.4
# # Write a function that gets a list of integers as a parameter.
# # The function returns the sum of all the numbers in the list.
# # For testing, write a main program where you create a list,
# # call the function, and print out the value it returned.
#
# def f(list_int):
#     all_numbers = 0
#     for i in list_int:
#         all_numbers = all_numbers + i
#     return all_numbers
#
# numbers = [2,4,6,10]
#
# sum_numbers = f(numbers)
# print(f"The sum of {numbers} is {sum_numbers}")
#
#
# ## 6.5
# # Write a function that gets a list of integers as a parameter.
# # The function returns a second list that is otherwise the same as
# # the original list except that all uneven numbers have been removed.
# # For testing, write a main program where you create a list, call the function,
# # and then print out both the original as well as the cut-down list.
#
# def n(list_int):
#     for i in list_int[:]:
#         if i % 2 != 0:
#             list_int.remove(i)
#     return list_int
#
# list_create = [1,1,1,1,2,2,3,4,5,56,6,7,8,9]
# print(list_create)
#
# new_list = n(list_create)
# print(new_list)
#
#
# ## 6.6
# # Write a function that receives two parameters:
# # the diameter of a round pizza in centimeters and the price of the pizza in euros.
# # The function calculates and returns the unit price of the pizza per square meter.
# # The main program asks the user to enter the diameter and price of two pizzas
# # and tells the user which pizza provides better value for money
# # (which of them has a lower unit price).
# # You must use the function you wrote for calculating the unit prices.
#
# def calculate_unit_price(diameter,price):
#     # Calculate the area of the pizza (in square meters) Diameter is in cm, convert to meters
#     pizza_size = (diameter /100 / 2) ** 2 * math.pi
#     # Calculate the price per square meter
#     unit_price = price / pizza_size
#     return unit_price
#
# # Get user input for the first pizza
# diameter1 = float(input("Enter your first diameter(cm): "))
# price1 = float(input("Enter your first price: "))
#
# # Calculate unit price for the first pizza
# unit_price1 = calculate_unit_price(diameter1,price1)
#
# # Get user input for the second pizza
# diameter2 = float(input("Enter your second diameter(cm): "))
# price2 = float(input("Enter your second price: "))
#
# # Calculate unit price for the second pizza
# unit_price2 = calculate_unit_price(diameter2,price2)
#
# # Compare unit prices and print results
# if unit_price1 < unit_price2:
#     print(f"The first pizza is {unit_price1:.2f} euros/square meter.")
#     print(f"The second pizza is {unit_price2:.2f} euros/square meter.")
#     print("The first pizza has a lower unit price.")
# elif unit_price2 < unit_price1:
#     print(f"The first pizza is {unit_price1:.2f} euros/square meter.")
#     print(f"The second pizza is {unit_price2:.2f} euros/square meter.")
#     print("The second pizza has a lower unit price.")
# else:
#     print(f"The first pizza is {unit_price1:.2f} euros/square meter.")
#     print(f"The second pizza is {unit_price2:.2f} euros/square meter.")
#     print("They have the same unit price.")
#


## 7.1
# Write a program that asks the user for a number of a month
# and then prints out the corresponding season (spring, summer, autumn, winter).
# Save the seasons as strings into a tuple in your program.
# We can define each season to last three months,
# December being the first month of winter.

# season = ("","winter","winter","spring","spring","spring","summer",
#           "summer","summer","autumn","autumn","autumn","winter")
#
# month_input = int(input("Enter a number of a month(1-12):"))
# if 12 >= month_input >= 1:
#     print(season[month_input])
# else:
#     print("Invalid input")




## 7.2
# Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name
# or Existing name depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one,
# one below another in any order. Use the set data structure to store the names.

# names = set()
# while True:
#     name_new = input('Please enter a name (or press Enter to finish): ')
#     if name_new == "":
#         break
#     if name_new in names:
#         print("It was entered.")
#     else:
#         names.add(name_new)
#         print("It's a new name.")
# for a in names:
#     print(a)



## 7.3
# Write a program for fetching and storing airport data.
# The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit.
# If the user chooses to enter a new airport,
# the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport
# and prints out the corresponding name. If the user chooses to quit,
# the program execution ends.
# The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport.
# For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
# You can easily find the ICAO codes of different airports online.)

# first way

# chooses = {'EFHK': 'Helsinki-Vantaa Airport',
#            'ZBAA': 'Beijing Capital International Airport',
#            'VHHH': 'Hong Kong International Airport',
#            'KLAX': 'Los Angeles International Airport',
#            'YSSY': 'Sydney Kingsford-Smith International Airport',
#            'LFPG': 'Paris Charles de Gaulle Airport',
#            'CYYZ': 'Toronto Pearson International Airport'}
# while True:
#     print('1:Enter a new airport.\n2:Fetch the information of an existing airport.\n3:Quit.')
#     user = input('Please enter a number ：')
#     if user == '1':
#         code_new = input('Please enter the ICAO code of the airport: ').upper()
#         if code_new in chooses:
#             print(f'The ICAO code "{code_new}" already exists in the database.')
#         else:
#             name_new = input('Please enter the name of the airport: ').strip()
#             if name_new:
#                 chooses[code_new] = name_new
#                 print(f'New airport "{name_new}" with ICAO code "{code_new}" added.')
#             else:
#                 print('Error: Airport name cannot be empty.')
#
#     elif user == '2':
#         if chooses:
#             print("Here is the list of available airports:")
#             for key in chooses.keys():
#                 print(key)
#
#             code = input('Please enter the ICAO code: ').upper()
#             if code in chooses:
#                 print(f'The name of the airport with ICAO code "{code}" is: {chooses[code]}')
#             else:
#                 print(f'Airport not found.')
#         else:
#             print("No airports available in the database.")
#     elif user == '3':
#         print('Quit')
#         break
#     else:
#         print('Error enter.')

# second way

# chooses = {
#     'EFHK': 'Helsinki-Vantaa Airport',
#     'ZBAA': 'Beijing Capital International Airport',
#     'VHHH': 'Hong Kong International Airport',
#     'KLAX': 'Los Angeles International Airport',
#     'YSSY': 'Sydney Kingsford-Smith International Airport',
#     'LFPG': 'Paris Charles de Gaulle Airport',
#     'CYYZ': 'Toronto Pearson International Airport'
# }
#
# def print_airports():
#     # Prints all ICAO codes in columns with five codes per row, left-aligned.
#     if chooses:
#         print("\nHere is the list of available airports:")
#         # 获取所有键
#         keys = list(chooses.keys())
#         num_columns = 5
#         column_width = max(len(key) for key in keys) + 2  # +2 for padding
#         # 打印每行的键
#         for i in range(0, len(keys), num_columns):
#             row_keys = keys[i:i + num_columns]
#             print(''.join(f"{key.ljust(column_width)}" for key in row_keys))
#     else:
#         print("No airports available in the database.")
#
# def add_airport():
#     # Adds a new airport to the database.
#     code_new = input('Please enter the ICAO code of the airport: ').upper()
#     if code_new in chooses:
#         print(f'The ICAO code "{code_new}" already exists in the database.')
#     else:
#         name_new = input('Please enter the name of the airport: ').strip()
#         if name_new:
#             chooses[code_new] = name_new
#             print(f'New airport "{name_new}" with ICAO code "{code_new}" added.')
#         else:
#             print('Error: Airport name cannot be empty.')
#
# def fetch_airport_info():
#     # Fetches and displays information for an existing airport.
#     print_airports()
#     code = input('\nPlease enter the ICAO code: ').upper()
#     if code in chooses:
#         print(f'The name of the airport with ICAO code "{code}" is: {chooses[code]}')
#     else:
#         print(f'Airport with ICAO code "{code}" not found.')
#
#
# while True:
#     print('\n1: Enter a new airport.\n2: Fetch the information of an existing airport.\n3: Quit.')
#     user = input('Please enter a number: ')
#     if user == '1':
#         add_airport()
#     elif user == '2':
#         fetch_airport_info()
#     elif user == '3':
#         print('Quitting the program.')
#         break
#     else:
#         print('Error: Invalid input. Please enter 1, 2, or 3.')

# 8.1
# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name
# and location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.
# import mysql.connector   #导入 MySQL Connector 模块
#
# def connect_to_mariadb_airport():
#     connection= mysql.connector.connect(    #建立数据库连接：mysql.connector.connect()
#         user="luoying",
#         password="mypassword",
#         host="localhost",      # 设置主机地址,localhost，表示本地计算机
#         port=3306,             # 设置数据库端口：3306 是 MySQL 数据库的默认端口。
#         database="airport",    # 选择要连接的数据库名称
#         autocommit = True,     # 自动提交开启
#         charset="utf8mb4",     # 设置字符集：utf8mb4，它支持包括 emoji 在内的多字节 Unicode 字符。
#         collation= "utf8mb4_general_ci"    #设置字符排序规则：utf8mb4 字符集的一种不区分大小写的通用排序规则。
#     )                      # 结束连接设置
#
#     if connection.is_connected():  # 检查连接是否成功
#         print("Connected successfully to MariaDB!")
#
#     return connection          # 将建立的数据库连接对象返回给调用此函数的地方
#
# # icao：机场的 ICAO 代码。connection：数据库连接对象。
# def get_name_location_by_icao(icao,connection):
#
#     # 创建游标对象：创建一个游标对象 cursor。游标用于执行 SQL 查询和获取结果。
#     cursor = connection.cursor()
#
#     # 定义SQL查询字符串：选择 airport 表中的 name 和 municipality 列。%s：占位符，用于在执行查询时动态插入 icao 的值。
#     sql = "SELECT name, municipality FROM airport WHERE ident = %s"
#
#     # 执行SQL查询：调用游标execute()方法。将 icao 作为参数传递给查询，替换%s占位符。可防止SQL注入攻击并确保查询的正确性。
#     cursor.execute(sql, (icao,))
#
#     # 获取单条查询结果：调用fetchone()方法从游标中获取查询的第一行结果。如果没有结果，则result为None。
#     result = cursor.fetchone()
#
#     # 关闭游标：调用游标close()方法，关闭游标对象以释放数据库资源。
#     cursor.close()
#
#     # 如果找到结果，返回该结果；如果没有找到，则返回 None。
#     return result if result else None
#
# icao_input = input("Enter icao code of the airport:").upper()
#
# # 调用之前定义的函数，建立与数据库的连接，并将返回的连接对象赋值给变量conn
# conn = connect_to_mariadb_airport()
#
# # 调用函数,传入用户输入的ICAO代码和数据库连接对象conn。
# # 函数执行后，返回的机场名称和市区信息将赋值给变量airport_city。
# airport_city = get_name_location_by_icao(icao_input,conn)
#
# if airport_city:
#     print(f"Airport name: {airport_city[0]}, Location(Town): {airport_city[1]}.")
# else:
#     print(f"No airport found with icao code {icao_input.upper()}")
#
#  # 关闭与数据库的连接，释放资源。确保在所有数据库操作完成后关闭连接，以避免资源泄漏。
# conn.close()

# 8.2
# Write a program that asks the user to enter the area code (for example FI)
# and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports,
# 15 helicopter airports and so on.
#
# import mysql.connector
#
# def connect_to_mariadb_airport():
#     connection= mysql.connector.connect(
#         user="luoying",
#         password="mypassword",
#         host="localhost",
#         port=3306,
#         database="airport",
#         autocommit = True,
#         charset="utf8mb4",
#         collation= "utf8mb4_general_ci"
#     )
#     if connection.is_connected():
#         print("Connected successfully to MariaDB!")
#     return connection
#
# def get_airports_by_iso_country(iso_country,connection):
#
#     # 创建游标对象：创建一个游标对象 cursor。游标用于执行SQL查询和获取结果。
#     cursor = connection.cursor()
#
#     # 从airport表中选择type列
#     # 使用 COUNT(*) 聚合函数来计算每个 type 中机场的数量
#     # 给这个计算结果取了一个别名 airports_count，方便后续查询结果的读取和展示
#     sql = ("SELECT type, COUNT(*) as airports_count "
#            "FROM airport "
#            "WHERE iso_country = %s "
#            "GROUP BY type "    # 按type列对结果分组。同类型的机场会被归为一组，COUNT(*) 将统计每一组内的机场数量。
#            "ORDER BY type")    # 按type列对结果升序排列。确保不同类型的机场按字母顺序或其他自然顺序进行展示。
#
#     cursor.execute(sql, (iso_country,))
#
#     # 来获取SQL查询执行后返回的所有结果。如果没有任何数据返回，则返回一个空列表 []
#     result = cursor.fetchall()
#     cursor.close()
#     return result
#
# # 调用之前定义的函数，建立与数据库的连接，并将返回的连接对象赋值给变量conn
# conn = connect_to_mariadb_airport()
#
# iso_country_input = input("Enter the country code (e.g 'FI' for Finland):")
#
# # 使用传入的 conn 连接对象，执行一条 SQL 查询。
# # 查询条件是由 iso_country_input 来决定的国家代码，比如 iso_country_input 为 'FI'（芬兰），那么查询就会获取芬兰所有机场的数据。
# airport_type = get_airports_by_iso_country(iso_country_input,conn)
#
# if airport_type:
#     # 打印表头，20字符宽度用于机场类型，10字符宽度用于机场数量
#     print(f"\n{'Airport Type':<20} {'Count':<10}")
#     print("-" * 30)  # 表格分隔线
#
#     # 逐行打印每种类型的机场和数量，格式化输出
#     for i in airport_type:
#         print(f"{i[0]:<20} {i[1]:<10}")
# else:
#     print(f"No airports found for the country code: {iso_country_input}")
#
# conn.close()

# 8.3
# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library:
# https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.

