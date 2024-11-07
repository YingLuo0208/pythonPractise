# 2.Variables and interactive programs
## 2.1
Write a program that asks your name and then greets you by your name: Examples:
If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!.

```python
name = input("Enter your name: ")
print(f"Hello {name}")
```
```monospace
Enter your name: luoying
Hello luoying
```

## 2.2
Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

```python
import math

radius = float(input("Enter your radius: "))
area = math.pi * radius**2
print(f"The area is {area:.2f}")
```
```monospace
Enter your radius: 2.3
The area is 16.62
```

## 2.3
Write a program that asks the user for the length and width of a rectangle.
The program then prints out the perimeter and area of the rectangle.
The perimeter of a rectangle is the sum of the lengths of each four sides.

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = (length + width) * 2
area = length * width
print(f"The perimeter is {perimeter:.2f},The area is {area:.2f}")
```
```monospace
Enter length: 3
Enter width: 5
The perimeter is 16.00,The area is 15.00
```

## 2.4
Write a program that asks the user for three integer numbers.
The program prints out the sum, product, and average of the numbers.

```python
num1 = float(input("input number1: "))
num2 = float(input("input number2: "))
num3 = float(input("input number3: "))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3
print(f"The sum is {sum:.2f},The product is {product:.2f},The average is {average:.2f}")
```
```monospace
input number1: 2.2
input number2: 6
input number3: 5.8
The sum is 14.00,The product is 76.56,The average is 4.67
```

## 2.5
Write a program that asks the user to enter a mass in medieval units:
talents (leiviskä), pounds (naula), and lots (luoti).
The program converts the input to full kilograms and grams and outputs the result to the user:
One talent is 20 pounds.
One pound is 32 lots.
One lot is 13,3 grams.

```python
talents = float(input("input talents: "))
pounds = float(input("input pounds: "))
lots = float(input("input lots: "))
total = lots * 13.3 + pounds * 13.3 * 32 + talents * 13.3 * 32 * 20
kilograms = total // 1000
grams = total % 1000
print(f"The weight in modern units: \n{kilograms:.0f} kilograms and {grams:.2f} grams.")
```
```monospace
input talents: 3
input pounds: 9
input lots: 13.5
The weight in modern units: 
29 kilograms and 545.95 grams.
```

## 2.6
Write a program that draws two random combinations of numbers for a combination lock:
a 3-digit code where each number is between 0 and 9.
a 4-digit code where each number is between 1 and 6.

```python
import random

n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
code1 = n1 , n2 , n3
print(f'code1 is : {code1}')
nn1 = random.randint(1, 6)
nn2 = random.randint(1, 6)
nn3 = random.randint(1, 6)
nn4 = random.randint(1, 6)
code2 = nn1 , nn2 , nn3 , nn4
print(f'code2 is : {code2}')
```
```monospace
code1 is : (9, 2, 0)
code2 is : (5, 1, 3, 4)
```

# 3. Conditional structures (if)
## 3.1
Write a program that asks a fisher the length of a zander in centimeters.
If the zander does not fulfill the size limit,the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was.
A zander must be 42 centimeters or longer to meet the size limit.

```python
length = float(input("The length of a zander in centimeters is: "))
if length >= 42:
    print("You can keep the fish.")
else:
    print("A zander must be 42 centimeters or longer to meet the size limit.\n"
           "Please release the fish back into the lake.")
```
```monospace
The length of a zander in centimeters is: 2
A zander must be 42 centimeters or longer to meet the size limit.
Please release the fish back into the lake.

The length of a zander in centimeters is: 42
You can keep the fish.
```
## 3.2
Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below.You must use an if/elif/else structure in your solution.
LUX: upper-deck cabin with a balcony.
A: above the car deck, equipped with a window.
B: windowless cabin above the car deck.
C: windowless cabin below the car deck.
If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

```python
cabin_class = input("Please enter the cabin class of a cruise ship:").upper()
if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else:
    print('Invalid cabin class.')
```
```monospace
Please enter the cabin class of a cruise ship:a
A: above the car deck, equipped with a window.

Please enter the cabin class of a cruise ship:lux
LUX: upper-deck cabin with a balcony.

Please enter the cabin class of a cruise ship:1
Invalid cabin class.
```

## 3.3
Write a program that asks for the biological gender and hemoglobin value (g/l).
The program the notifies the user if the hemoglobin value is low, normal or high.
A normal hemoglobin value for adult females is between 117-155 g/l.
A normal hemoglobin value for adult males is between 134-167 g/l.

```python
gender = input("Please enter your biological gender(Male/Female): ")
if gender == "Male":
    value = float(input("Please enter your hemoglobin value: "))
    if value > 155:
        print("Your hemoglobin is high.")
    elif value < 117:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is normal.")
elif gender == "Female":
    value = float(input("Please enter your hemoglobin value: "))
    if value > 167:
        print("Your hemoglobin is high.")
    elif value < 134:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is normal.")
else:
    print("Input error.")
```
```monospace
Please enter your biological gender(Male/Female): Male
Please enter your hemoglobin value: 167
Your hemoglobin is normal.

Please enter your biological gender(Male/Female): Male
Please enter your hemoglobin value: 13
Your hemoglobin is low.

Please enter your biological gender(Male/Female): Male
Please enter your hemoglobin value: 300
Your hemoglobin is high.

Please enter your biological gender(Male/Female): ww
Input error.

Please enter your biological gender(Male/Female): Female
Please enter your hemoglobin value: 122
Your hemoglobin is normal.

Please enter your biological gender(Male/Female): Female
Please enter your hemoglobin value: 167
Your hemoglobin is high.
```
        
## 3.4
Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
A year is a leap year if it is divisible by four.
However, years divisible by 100 are leap years only if they are also divisible by 400.

```python
year = int(input("Enter year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")
```
```monospace
Enter year: 2000
It is a leap year.

Enter year: 1900
It is not a leap year.

Enter year: 2024
It is a leap year.
```

# 4. While loops (while)
## 4.1
Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

```python
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1
```
```monospace
3
6
9
....
996
999
```
```python
i = 0
while i <= 1000:
    print(i)
    i += 3
```
```monospace
0
3
6
9
....
996
999
```

## 4.2
Write a program that converts inches to centimeters until the user inputs a negative value.
Then the program ends.

```python
inches = float(input("Enter inches: "))
while inches > 0:
    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters} centimeters")
    inches = float(input("Enter inches: "))
print("program ends")
```
```monospace
Enter inches: 1
1.0 inches = 2.54 centimeters
Enter inches: -1
program ends
```

## 4.3
Write a program that asks the user to enter numbers until they enter an empty string to quit.
Finally, the program prints out the smallest and largest number from the numbers it received.
The first way:

```python
max_number = None
min_number = None
number = input("Enter numbers: ")

while number != "":
    number = float(number)
    if  max_number is None or max_number < number :
        max_number = number
    if min_number is None or min_number > number :
        min_number = number
    number = input("Enter numbers: ")

print(f"The max_number is {max_number},the min_number is {min_number}")
```
```monospace
Enter numbers: 2
Enter numbers: 55
Enter numbers: 3
Enter numbers: 7
Enter numbers: 90
Enter numbers: 
The max_number is 90.0,the min_number is 2.0
```

The second way:

```python
numbers = []
number = input("Enter numbers: ")
while number != "":
    numbers.append(number)
    number = input("Enter numbers: ")

print(numbers)
number_max = max(numbers)
number_min = min(numbers)
print(number_max, number_min)
```
```monospace
Enter numbers: 2
Enter numbers: 55
Enter numbers: 3
Enter numbers: 7
Enter numbers: 90
Enter numbers: 
['2', '55', '3', '7', '90']
90 2
```

## 4.4
Write a game where the computer draws a random integer between 1 and 10.
The user tries to guess the number until they guess the right number.
After each guess the program prints out a text: Too high, Too low or Correct.
Notice that the computer must not change the number between guesses.

```python
import random

random_num = random.randint(1, 10)
while True:
    guess_num = int(input("Guess a number between 1 and 10: "))
    if guess_num < random_num:
        print("Too low!")
    elif guess_num > random_num:
        print("Too high!")
    else:
        print("Correct!")
        break
```
```monospace
Guess a number between 1 and 10: 3
Too low!
Guess a number between 1 and 10: 5
Too low!
Guess a number between 1 and 10: 7
Too high!
Guess a number between 1 and 10: 6
Correct!
```

## 4.5
Write a program that asks the user for a username and password.
If either or both are incorrect, the program ask the user to enter the username and password again.
This continues until the login information is correct or wrong credentials have been entered five times.
If the information is correct, the program prints out Welcome.
After five failed attempts the program prints out Access denied.
The correct username is python and password rules.

```python
T_username = "python"
T_password = "rules"
time = 0
while time < 5:
    time += 1
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    if username == T_username and password == T_password :
        print("Welcome!")
        break
    elif ( username != T_username or password != T_password )and time != 5:
        print("Try Again")
    else:
        print("Access denied")
```
```monospace
Enter your name: eee
Enter your password: eee
Try Again
Enter your name: eee
Enter your password: eee
Try Again
Enter your name: eee
Enter your password: eee
Try Again
Enter your name: eee
Enter your password: eee
Try Again
Enter your name: eee
Enter your password: eee
Access denied

Enter your name: eee
Enter your password: rules
Try Again
Enter your name: python
Enter your password: eee
Try Again
Enter your name: python
Enter your password: rules
Welcome!
```

## 4.6
Implement an algorithm for calculating an approximation for the value of pi (π).
Let's assume that A is a unit circle. A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B is drawn around the unit circle
so that circle A is completely inside the square.
The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1).
If a large number of random points are scattered inside the square,the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4.
This can be used as a simple method for calculating an approximation of the value of pi:
Let's generate a large number of random points, such as one million, inside square B.
Let N be the total number of random points.
Each point inside the square is tested for whether it resides inside circle A.
Let n be the total number of points that fall inside circle A.
Now we have n/N≈π/4, and from that we get π≈4n/N.
Write a program that asks the user how many random points to generate,and then calculates the approximate value of pi using the method explained above.
At the end, the program prints out the approximation of pi to the user.
(Notice that it is easy to test if a point falls inside circle A by testing
if it fulfills the inequation x^2+y^2<1.).

```python
import random

point_all = 0
point_circle = 0
point_user = int(input("How many points do you want? "))

while point_all < point_user:
    point_all = point_all + 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        point_circle = point_circle + 1

pi = 4 * point_circle / point_user
print(f"The approximation of pi is {pi:.10f}")
```
```monospace
How many points do you want? 1000000
The approximation of pi is 3.1406440000
```
    
# 5. List structures and iterative loops (for)
## 5.1
Write a program that asks the user how many dice to roll.
The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

```python
import random

times = int(input("How many times would you like to roll? : "))
sum_of_numbers = 0
numbers =[]
for i in range(times):
    roll = random.randint(1, 6)
    numbers.append(roll)
    sum_of_numbers = sum_of_numbers + roll
print(numbers)
print(sum_of_numbers)

```
```monospace
How many times would you like to roll? : 6
[3, 5, 4, 3, 1, 2]
18
```

## 5.2
Write a program that asks the user to enter numbers until they input an empty string to quit.
At the end, the program prints out the five greatest numbers sorted in descending order.
Hint: You can reverse the order of sorted list items by using the sort method
with the reverse=True argument.

```python
numbers = []

while True:
    user_number = input("Enter a number: ")
    if user_number == "":
        break
    numbers.append(int(user_number))

numbers.sort(reverse=True)
first_five_numbers = numbers[:5]

print(first_five_numbers)
```
```monospace
Enter a number: 5
Enter a number: 40
Enter a number: 56
Enter a number: 39
Enter a number: 28
Enter a number: 1
Enter a number: 888
Enter a number: 
[888, 56, 40, 39, 28]
```

## 5.3
Write a program that asks the user for an integer and tells if the number is a prime number.
Prime numbers are number that are only divisible by one or the number itself.
For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

```python
user_num = int(input("Enter a number: "))
divided_by = []

if user_num <= 1 or user_num == 4:
    print("Your number is not a prime number.")

elif user_num in { 2,3,5 }:
    print("Your number is a prime number.")

elif user_num > 5:
    for i in range(2,user_num,1):
        if user_num % i == 0 :
            divided_by.append(i)
            break

    if len(divided_by) == 0 :
        print("Your number is a prime number.")
    else:
        print("Your number is not a prime number.")
```
```monospace
Enter a number: 0
Your number is not a prime number.

Enter a number: 1
Your number is not a prime number.

Enter a number: 2
Your number is a prime number.

Enter a number: 4
Your number is not a prime number.

Enter a number: 21
Your number is not a prime number.
```

## 5.4
Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) and stores them into a list structure.
Finally, the program prints out the names of the cities one by one, one city per line,in the same order they were read as input.
Use a for loop for asking the names and a for/in loop to iterate through the list.

```python
cities = []

for a in range(5):
    city = input("Enter a city: ")
    cities.append(city)

for city in cities:
    print(city)
```
```monospace
Enter a city: city1
Enter a city: city2
Enter a city: city3
Enter a city: city4
Enter a city: city5
city1
city2
city3
city4
city5
```

# 6. Functions
## 6.1
Write a function that returns a random dice roll between 1 and 6.The function should not have any parameters.
Write a main program that rolls the dice until the result is 6.The main program should print out the result of each roll.

```python
import random

def roll():
    dice = random.randint(1,6)
    return dice
                           # result = roll()  # Start by rolling the dice
while True:                # while result != 6:
    result = roll()        #     print(result)  # Print the current roll
    if result == 6 :       #     result = roll()  # Roll the dice again
        print(result)      # print(result)  # Print the final result when it's 6
        break
    print(result)
```
```monospace
5
3
6
```

## 6.2
Modify the function above so that it gets the number of sides on the dice as a parameter.
With the modified function you can for example roll a 21-sided role-playing dice.
The difference to the last exercise is that the dice rolling in the main program continues until the program gets the maximum number on the dice,which is asked from the user at the beginning.

```python
import random

def roll(sides):
    dice = random.randint(1, sides)
    return dice

dice_max = int(input("Enter a number: "))

while True:
    result = roll(dice_max)

    if result == dice_max :
        print(result)
        print("You rolled the maximum number! ")
        break
    print(result)
```
```monospace
Enter a number: 12
1
8
4
12
```

## 6.3
Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres. Write a main program that asks for a volume in gallons from the user and converts the value to liters.
The conversion must be done by using the function.Conversions continue until the user inputs a negative value.

```python
def gasoline(gallons):
    litres = gallons * 3.78541
    return litres

user_gallons = float(input("Enter number of gasoline in American gallons : "))

while user_gallons >= 0 :
    user_litres = gasoline(user_gallons)
    print(f"{user_gallons} gallons = {user_litres:.3f} litres.")
    user_gallons = float(input("Enter number of gasoline in American gallons : "))

print("Error input.")
```
```monospace
Enter number of gasoline in American gallons : 1
1.0 gallons = 3.785 litres.
Enter number of gasoline in American gallons : 0
0.0 gallons = 0.000 litres.
Enter number of gasoline in American gallons : -1
Error input.
```

## 6.4
Write a function that gets a list of integers as a parameter.The function returns the sum of all the numbers in the list.
For testing, write a main program where you create a list,call the function, and print out the value it returned.

```python
def f(list_int):
    all_numbers = 0
    for i in list_int:
        all_numbers = all_numbers + i
    return all_numbers

numbers = [2,4,6,10]

sum_numbers = f(numbers)
print(f"The sum of {numbers} is {sum_numbers}")
```
```monospace
The sum of [2, 4, 6, 10] is 22
```

## 6.5
Write a function that gets a list of integers as a parameter.
The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed.
For testing, write a main program where you create a list, call the function,and then print out both the original as well as the cut-down list.

```python
def n(list_int):
    for i in list_int[:]:
        if i % 2 != 0:
            list_int.remove(i)
    return list_int

list_create = [1,1,1,1,2,2,3,4,5,56,6,7,8,9]
print(list_create)

new_list = n(list_create)
print(new_list)
```
```monospace
[1, 1, 1, 1, 2, 2, 3, 4, 5, 56, 6, 7, 8, 9]
[2, 2, 4, 56, 6, 8]
```

## 6.6
Write a function that receives two parameters:the diameter of a round pizza in centimeters and the price of the pizza in euros.
The function calculates and returns the unit price of the pizza per square meter.
The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money(which of them has a lower unit price).
You must use the function you wrote for calculating the unit prices.

```python
import math

def calculate_unit_price(diameter,price):
    # Calculate the area of the pizza (in square meters) Diameter is in cm, convert to meters
    pizza_size = (diameter /100 / 2) ** 2 * math.pi
    # Calculate the price per square meter
    unit_price = price / pizza_size
    return unit_price

# Get user input for the first pizza
diameter1 = float(input("Enter your first diameter(cm): "))
price1 = float(input("Enter your first price: "))

# Calculate unit price for the first pizza
unit_price1 = calculate_unit_price(diameter1,price1)

# Get user input for the second pizza
diameter2 = float(input("Enter your second diameter(cm): "))
price2 = float(input("Enter your second price: "))

# Calculate unit price for the second pizza
unit_price2 = calculate_unit_price(diameter2,price2)

# Compare unit prices and print results
if unit_price1 < unit_price2:
    print(f"The first pizza is {unit_price1:.2f} euros/square meter.")
    print(f"The second pizza is {unit_price2:.2f} euros/square meter.")
    print("The first pizza has a lower unit price.")
elif unit_price2 < unit_price1:
    print(f"The first pizza is {unit_price1:.2f} euros/square meter.")
    print(f"The second pizza is {unit_price2:.2f} euros/square meter.")
    print("The second pizza has a lower unit price.")
else:
    print(f"The first pizza is {unit_price1:.2f} euros/square meter.")
    print(f"The second pizza is {unit_price2:.2f} euros/square meter.")
    print("They have the same unit price.")
```
```monospace
Enter your first diameter(cm): 2
Enter your first price: 3.3
Enter your second diameter(cm): 3
Enter your second price: 4.4
The first pizza is 10504.23 euros/square meter.
The second pizza is 6224.73 euros/square meter.
The second pizza has a lower unit price.
```

# 7. Tuple, set, and dictionary
## 7.1
Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter).
Save the seasons as strings into a tuple in your program.
We can define each season to last three months,December being the first month of winter.
```python
season = ("","winter","winter","spring","spring","spring","summer",
          "summer","summer","autumn","autumn","autumn","winter")

month_input = int(input("Enter a number of a month(1-12):"))
if 12 >= month_input >= 1:
    print(season[month_input])
else:
    print("Invalid input")
```
```monospace
Enter a number of a month(1-12):20
Invalid input

Enter a number of a month(1-12):1
winter

Enter a number of a month(1-12):7
summer
```

## 7.2
Write a program that asks the user to enter names until he/she enters an empty string.
After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time.
Finally, the program lists out the input names one by one,one below another in any order. Use the set data structure to store the names.

```python
names = set()
while True:
    name_new = input('Please enter a name (or press Enter to finish): ')
    if name_new == "":
        break
    if name_new in names:
        print("It was entered.")
    else:
        names.add(name_new)
        print("It's a new name.")
for a in names:
    print(a)
```
```monospace
Please enter a name (or press Enter to finish): 123
It's a new name.
Please enter a name (or press Enter to finish): aaa
It's a new name.
Please enter a name (or press Enter to finish): aaa
It was entered.
Please enter a name (or press Enter to finish): ccc
It's a new name.
Please enter a name (or press Enter to finish): 
ccc
123
aaa
```

## 7.3
Write a program for fetching and storing airport data.
The program asks the user if they want to enter a new airport,fetch the information of an existing airport or quit.
If the user chooses to enter a new airport,the program asks the user to enter the ICAO code and name of the airport.
If the user chooses to fetch airport information instead,the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit,the program execution ends.
The user can choose a new option as many times they want until they choose to quit.
(The ICAO code is an identifier that is unique to each airport.For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.You can easily find the ICAO codes of different airports online.)

```python
chooses = {'EFHK': 'Helsinki-Vantaa Airport',
           'ZBAA': 'Beijing Capital International Airport',
           'VHHH': 'Hong Kong International Airport',
           'KLAX': 'Los Angeles International Airport',
           'YSSY': 'Sydney Kingsford-Smith International Airport',
           'LFPG': 'Paris Charles de Gaulle Airport',
           'CYYZ': 'Toronto Pearson International Airport'}
while True:
    print('1:Enter a new airport.\n2:Fetch the information of an existing airport.\n3:Quit.')
    user = input('Please enter a number ：')
    if user == '1':
        code_new = input('Please enter the ICAO code of the airport: ').upper()
        if code_new in chooses:
            print(f'The ICAO code "{code_new}" already exists in the database.')
        else:
            name_new = input('Please enter the name of the airport: ').strip()
            if name_new:
                chooses[code_new] = name_new
                print(f'New airport "{name_new}" with ICAO code "{code_new}" added.')
            else:
                print('Error: Airport name cannot be empty.')

    elif user == '2':
        if chooses:
            print("Here is the list of available airports:")
            for key in chooses.keys():
                print(key)

            code = input('Please enter the ICAO code: ').upper()
            if code in chooses:
                print(f'The name of the airport with ICAO code "{code}" is: {chooses[code]}')
            else:
                print(f'Airport not found.')
        else:
            print("No airports available in the database.")
    elif user == '3':
        print('Quit')
        break
    else:
        print('Error enter.')
```
```monospace
1:Enter a new airport.
2:Fetch the information of an existing airport.
3:Quit.
Please enter a number ：1
Please enter the ICAO code of the airport: aaaa
Please enter the name of the airport: 123456
New airport "123456" with ICAO code "AAAA" added.
1:Enter a new airport.
2:Fetch the information of an existing airport.
3:Quit.
Please enter a number ：aaaa
Error enter.
1:Enter a new airport.
2:Fetch the information of an existing airport.
3:Quit.
Please enter a number ：2
Here is the list of available airports:
EFHK
ZBAA
VHHH
KLAX
YSSY
LFPG
CYYZ
AAAA
Please enter the ICAO code: aaaa
The name of the airport with ICAO code "AAAA" is: 123456
1:Enter a new airport.
2:Fetch the information of an existing airport.
3:Quit.
Please enter a number ：2
Here is the list of available airports:
EFHK
ZBAA
VHHH
KLAX
YSSY
LFPG
CYYZ
AAAA
Please enter the ICAO code: bbbb
Airport not found.
1:Enter a new airport.
2:Fetch the information of an existing airport.
3:Quit.
Please enter a number ：3
Quit
```
```python
chooses = {
    'EFHK': 'Helsinki-Vantaa Airport',
    'ZBAA': 'Beijing Capital International Airport',
    'VHHH': 'Hong Kong International Airport',
    'KLAX': 'Los Angeles International Airport',
    'YSSY': 'Sydney Kingsford-Smith International Airport',
    'LFPG': 'Paris Charles de Gaulle Airport',
    'CYYZ': 'Toronto Pearson International Airport'
}

def print_airports():
    # Prints all ICAO codes in columns with five codes per row, left-aligned.
    if chooses:
        print("\nHere is the list of available airports:")
        # 获取所有键
        keys = list(chooses.keys())
        num_columns = 5
        column_width = max(len(key) for key in keys) + 2  # +2 for padding
        # 打印每行的键
        for i in range(0, len(keys), num_columns):
            row_keys = keys[i:i + num_columns]
            print(''.join(f"{key.ljust(column_width)}" for key in row_keys))
    else:
        print("No airports available in the database.")

def add_airport():
    # Adds a new airport to the database.
    code_new = input('Please enter the ICAO code of the airport: ').upper()
    if code_new in chooses:
        print(f'The ICAO code "{code_new}" already exists in the database.')
    else:
        name_new = input('Please enter the name of the airport: ').strip()
        if name_new:
            chooses[code_new] = name_new
            print(f'New airport "{name_new}" with ICAO code "{code_new}" added.')
        else:
            print('Error: Airport name cannot be empty.')

def fetch_airport_info():
    # Fetches and displays information for an existing airport.
    print_airports()
    code = input('\nPlease enter the ICAO code: ').upper()
    if code in chooses:
        print(f'The name of the airport with ICAO code "{code}" is: {chooses[code]}')
    else:
        print(f'Airport with ICAO code "{code}" not found.')


while True:
    print('\n1: Enter a new airport.\n2: Fetch the information of an existing airport.\n3: Quit.')
    user = input('Please enter a number: ')
    if user == '1':
        add_airport()
    elif user == '2':
        fetch_airport_info()
    elif user == '3':
        print('Quitting the program.')
        break
    else:
        print('Error: Invalid input. Please enter 1, 2, or 3.')
```
```monospace

1: Enter a new airport.
2: Fetch the information of an existing airport.
3: Quit.
Please enter a number: 1
Please enter the ICAO code of the airport: aaaa
Please enter the name of the airport: 123456
New airport "123456" with ICAO code "AAAA" added.

1: Enter a new airport.
2: Fetch the information of an existing airport.
3: Quit.
Please enter a number: aaaa
Error: Invalid input. Please enter 1, 2, or 3.

1: Enter a new airport.
2: Fetch the information of an existing airport.
3: Quit.
Please enter a number: 2

Here is the list of available airports:
EFHK  ZBAA  VHHH  KLAX  YSSY  
LFPG  CYYZ  AAAA  

Please enter the ICAO code: aaaa
The name of the airport with ICAO code "AAAA" is: 123456

1: Enter a new airport.
2: Fetch the information of an existing airport.
3: Quit.
Please enter a number: 2

Here is the list of available airports:
EFHK  ZBAA  VHHH  KLAX  YSSY  
LFPG  CYYZ  AAAA  

Please enter the ICAO code: bbbb
Airport with ICAO code "BBBB" not found.

1: Enter a new airport.
2: Fetch the information of an existing airport.
3: Quit.
Please enter a number: 3
Quitting the program.
```
# 8. Using relational databases
## 8.1
Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course. The ICAO codes are stored in the ident column of the airport table.

```python
import mysql.connector   #导入 MySQL Connector 模块

def connect_to_mariadb_airport():
    connection= mysql.connector.connect(    #建立数据库连接：mysql.connector.connect()
        user="luoying",
        password="mypassword",
        host="localhost",      # 设置主机地址,localhost，表示本地计算机
        port=3306,             # 设置数据库端口：3306 是 MySQL 数据库的默认端口。
        database="airport",    # 选择要连接的数据库名称
        autocommit = True,     # 自动提交开启
        charset="utf8mb4",     # 设置字符集：utf8mb4，它支持包括 emoji 在内的多字节 Unicode 字符。
        collation= "utf8mb4_general_ci"    #设置字符排序规则：utf8mb4 字符集的一种不区分大小写的通用排序规则。
    )                      # 结束连接设置

    if connection.is_connected():  # 检查连接是否成功
        print("Connected successfully to MariaDB!")

    return connection          # 将建立的数据库连接对象返回给调用此函数的地方

# icao：机场的 ICAO 代码。connection：数据库连接对象。
def get_name_location_by_icao(icao,connection):

    # 创建游标对象：创建一个游标对象 cursor。游标用于执行 SQL 查询和获取结果。
    cursor = connection.cursor()

    # 定义SQL查询字符串：选择 airport 表中的 name 和 municipality 列。%s：占位符，用于在执行查询时动态插入 icao 的值。
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"

    # 执行SQL查询：调用游标execute()方法。将 icao 作为参数传递给查询，替换%s占位符。可防止SQL注入攻击并确保查询的正确性。
    cursor.execute(sql, (icao,))

    # 获取单条查询结果：调用fetchone()方法从游标中获取查询的第一行结果。如果没有结果，则result为None。
    result = cursor.fetchone()

    # 关闭游标：调用游标close()方法，关闭游标对象以释放数据库资源。
    cursor.close()

    # 如果找到结果，返回该结果；如果没有找到，则返回 None。
    return result if result else None

icao_input = input("Enter icao code of the airport:").upper()

# 调用之前定义的函数，建立与数据库的连接，并将返回的连接对象赋值给变量conn
conn = connect_to_mariadb_airport()

# 调用函数,传入用户输入的ICAO代码和数据库连接对象conn。
# 函数执行后，返回的机场名称和市区信息将赋值给变量airport_city。
airport_city = get_name_location_by_icao(icao_input,conn)

if airport_city:
    print(f"Airport name: {airport_city[0]}, Location(Town): {airport_city[1]}.")
else:
    print(f"No airport found with icao code {icao_input.upper()}")

 # 关闭与数据库的连接，释放资源。确保在所有数据库操作完成后关闭连接，以避免资源泄漏。
conn.close()
```
```monospace
Enter icao code of the airport:aaaa
Connected successfully to MariaDB!
No airport found with icao code AAAA

Enter icao code of the airport:efhk
Connected successfully to MariaDB!
Airport name: Helsinki Vantaa Airport, Location(Town): Helsinki.
```

## 8.2
Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.
```python
import mysql.connector

def connect_to_mariadb_airport():
    connection= mysql.connector.connect(
        user="luoying",
        password="mypassword",
        host="localhost",
        port=3306,
        database="airport",
        autocommit = True,
        charset="utf8mb4",
        collation= "utf8mb4_general_ci"
    )
    if connection.is_connected():
        print("Connected successfully to MariaDB!")
    return connection

def get_airports_by_iso_country(iso_country,connection):

    # 创建游标对象：创建一个游标对象 cursor。游标用于执行SQL查询和获取结果。
    cursor = connection.cursor()

    # 从airport表中选择type列
    # 使用 COUNT(*) 聚合函数来计算每个 type 中机场的数量
    # 给这个计算结果取了一个别名 airports_count，方便后续查询结果的读取和展示
    sql = ("SELECT type, COUNT(*) as airports_count "
           "FROM airport "
           "WHERE iso_country = %s "
           "GROUP BY type "    # 按type列对结果分组。同类型的机场会被归为一组，COUNT(*) 将统计每一组内的机场数量。
           "ORDER BY type")    # 按type列对结果升序排列。确保不同类型的机场按字母顺序或其他自然顺序进行展示。

    cursor.execute(sql, (iso_country,))

    # 来获取SQL查询执行后返回的所有结果。如果没有任何数据返回，则返回一个空列表 []
    result = cursor.fetchall()
    cursor.close()
    return result

# 调用之前定义的函数，建立与数据库的连接，并将返回的连接对象赋值给变量conn
conn = connect_to_mariadb_airport()

iso_country_input = input("Enter the country code (e.g 'FI' for Finland):")

# 使用传入的 conn 连接对象，执行一条 SQL 查询。
# 查询条件是由 iso_country_input 来决定的国家代码，比如 iso_country_input 为 'FI'（芬兰），那么查询就会获取芬兰所有机场的数据。
airport_type = get_airports_by_iso_country(iso_country_input,conn)

if airport_type:
    # 打印表头，20字符宽度用于机场类型，10字符宽度用于机场数量
    print(f"\n{'Airport Type':<20} {'Count':<10}")
    print("-" * 30)  # 表格分隔线

    # 逐行打印每种类型的机场和数量，格式化输出
    for i in airport_type:
        print(f"{i[0]:<20} {i[1]:<10}")
else:
    print(f"No airports found for the country code: {iso_country_input}")

conn.close()
```
```monospace
Connected successfully to MariaDB!
Enter the country code (e.g 'FI' for Finland):fi

Airport Type         Count     
------------------------------
closed               6         
heliport             15        
large_airport        1         
medium_airport       30        
small_airport        65  
```
## 8.3
Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.
```python
import mysql.connector
from geopy.distance import geodesic

# 建立与MariaDB的连接
def connect_to_mariadb_airport():
    connection = mysql.connector.connect(
        user="luoying",
        password="mypassword",
        host="localhost",
        port=3306,
        database="airport",
        autocommit=True,
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )
    if connection.is_connected():
        print("Connected successfully to MariaDB!")
    return connection

# 接受一个 ICAO 代码和数据库连接作为参数。
def get_airport_location(icao,conn):
    cursor = conn.cursor()
    spl = ("SELECT latitude_deg, longitude_deg "
           "FROM airport "
           "WHERE ident = %s")
    cursor.execute(spl, (icao,))
    result = cursor.fetchone()
    cursor.close()
    return result

# 接受两个 ICAO 代码和数据库连接作为参数。
def calculate_distance(icao1, icao2, conn):
    location1 = get_airport_location(icao1, conn)
    location2 = get_airport_location(icao2, conn)

    if location1 and location2:
        airports_distance = geodesic(location1, location2).kilometers
        return airports_distance
    else:
        return None

conn = connect_to_mariadb_airport()

airport_a = input("Enter the first ICAO code: ").upper().strip()
airport_b = input("Enter the second ICAO code: ").upper().strip()

distance = calculate_distance(airport_a, airport_b, conn)

if distance is not None:
    print(f"The distance between {airport_a} and {airport_b} is {distance:.2f} kilometers.")
else:
    print("Could not find one or both airports.")

conn.close()
```
```monospace
Connected successfully to MariaDB!
Enter the first ICAO code: YUDA
Enter the second ICAO code: YUPG
The distance between YUDA and YUPG is 1139.25 kilometers.
```
# 9. Fundamentals of object-oriented programming
## 9.1
Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance. Add a class initializer that sets the first two of the properties based on parameter values. The current speed and travelled distance of a new car must be automatically set to zero. Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car.
```python
class Car:
    def __init__(self, number, max_speed,speed = 0,distance = 0):
        self.number = number
        self.max_speed = max_speed
        self.speed = speed
        self.distance = distance

    def car_info(self):
        print(f"Registration number : {self.number}")
        print(f"Maximum speed : {self.max_speed}(km/h)")
        print(f"Current speed : {self.speed}(km/h)")
        print(f"Travelled distance : {self.distance}(km)")

new_car = Car("ABC-123",142)
new_car.car_info()
```
```monospace
Registration number : ABC-123
Maximum speed : 142(km/h)
Current speed : 0(km/h)
Travelled distance : 0(km)
```
## 9.2
Extend the program by adding an accelerate method into the new class. The method should receive the change of speed (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the speed property of the object. The speed of the car must stay below the set maximum and cannot be less than zero. Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed. The travelled distance does not have to be updated yet.
```python
class Car:
    def __init__(self, number, max_speed,speed = 0,distance = 0):
        self.number = number
        self.max_speed = max_speed
        self.speed = speed
        self.distance = distance

    def accelerate(self, speed_change):
        self.speed += speed_change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0

    def car_info(self):
        print(f"Registration number : {self.number}")
        print(f"Maximum speed : {self.max_speed}(km/h)")
        print(f"Current speed : {self.speed}(km/h)")
        print(f"Travelled distance : {self.distance}(km)")

new_car = Car("ABC-123",142)
new_car.car_info()

new_car.accelerate(30)
new_car.car_info()

new_car.accelerate(70)
new_car.car_info()

new_car.accelerate(50)
new_car.car_info()

new_car.accelerate(-200)
new_car.car_info()
```
```monospace
Registration number : ABC-123
Maximum speed : 142(km/h)
Current speed : 0(km/h)
Travelled distance : 0(km)

Registration number : ABC-123
Maximum speed : 142(km/h)
Current speed : 30(km/h)
Travelled distance : 0(km)

Registration number : ABC-123
Maximum speed : 142(km/h)
Current speed : 100(km/h)
Travelled distance : 0(km)

Registration number : ABC-123
Maximum speed : 142(km/h)
Current speed : 142(km/h)
Travelled distance : 0(km)

Registration number : ABC-123
Maximum speed : 142(km/h)
Current speed : 0(km/h)
Travelled distance : 0(km)
```
## 9.3
Again, extend the program by adding a new drive method that receives the number of hours as a parameter. The method increases the travelled distance by how much the car has travelled in constant speed in the given time. Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.
```python
class Car:
    def __init__(self, number, max_speed,speed = 0,distance = 0):
        self.number = number
        self.max_speed = max_speed
        self.speed = speed
        self.distance = distance

    def accelerate(self, speed_change):
        self.speed += speed_change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0

    def drive(self, time_hours):
        self.distance += time_hours * self.speed

    def car_info(self):
        print(f"Registration number : {self.number}")
        print(f"Maximum speed : {self.max_speed}(km/h)")
        print(f"Current speed : {self.speed}(km/h)")
        print(f"Travelled distance : {self.distance}(km)")

new_car = Car("ABC-123",142,60,2000)
new_car.drive(1.5)
new_car.car_info()
```
```monospace
Registration number : ABC-123
Maximum speed : 142(km/h)
Current speed : 60(km/h)
Travelled distance : 2090.0(km)
```
## 9.4
Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race, the following operations are performed:

The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accerelate method.

Each car is made to drive for one hour. This is done with the drive method.
  
The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car are printed out formatted into a clear table.
```python
import random

class Car:
    def __init__(self, number, max_speed,speed = 0,distance = 0):
        self.number = number
        self.max_speed = max_speed
        self.speed = speed
        self.distance = distance

    def accelerate(self, speed_change):
        self.speed += speed_change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0

    def drive(self, time_hours):
        self.distance += time_hours * self.speed

    def car_info(self):
        # 设置高亮颜色
        # if self.distance >= 10000:
        #     highlight = "\033[93m"  # 黄色高亮
        #     reset = "\033[0m"  # 重置颜色
        # else:
        #     highlight = ""  # 没有高亮
        #     reset = ""  # 无需重置
        # 条件表达式 <值1> if <条件> else <值2>
        highlight = "\033[93m" if self.distance >= 10000 else ""
        reset = "\033[0m"  # 重置颜色

        print(
            f" {highlight}{self.number:<15}{self.max_speed:<20}"
            f"{self.speed:<25}{self.distance:<20}{reset}")


def car_race():
    cars = []
    for i in range(1,11):
        car_name = f"ABC-{i}"
        new_car = Car(car_name, random.randint(100,200))
        cars.append(new_car)

    race = True
    hours = 0
    while race:
        hours += 1

        for car in cars:
            car.accelerate(speed_change = random.randint(-10,15))
            car.drive(1)

            if car.distance >= 10000:
                race = False
                break

    print(f"Race finished at hour: {hours}h ! Final standings:")
    print(f"{'Registration':<14} {'Max Speed (km/h)':<19} {'Current Speed (km/h)':<24} {'Distance (km)':<20}")
    print("-" * 75)
    for car in cars:
        car.car_info()

car_race()
```
```monospace
Race finished at hour: 82h ! Final standings:
Registration   Max Speed (km/h)    Current Speed (km/h)     Distance (km)       
---------------------------------------------------------------------------
 ABC-1          174                 163                      7102                
 ABC-2          191                 162                      7029                
 ABC-3          144                 144                      8369                
 ABC-4          134                 123                      5492                
 ABC-5          179                 171                      8479                
 ABC-6          122                 122                      7113                
 ABC-7          159                 158                      10001            
 ABC-8          163                 163                      7534                
 ABC-9          160                 160                      9447                
 ABC-10         188                 183                      5775   
```
# 10. Association
## 10.1
Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell what floor the elevator is after each move. Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.
```python
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def go_to_floor(self, floor):
        print(f"Elevator is now on floor {self.current_floor}")
        if floor < self.bottom or floor > self.top:
            print("Invalid floor.")
            return

        while self.current_floor < floor:  # Move up if below target floor
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

        while self.current_floor > floor:  # Move down if above target floor
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

        print(f"Already at the {floor} floor.")

        if self.current_floor == self.bottom:
            print("It is the bottom floor.")
        if self.current_floor == self.top:
            print("It is the top floor.")



elevator = Elevator(1, 7)
elevator.go_to_floor(5)
elevator.go_to_floor(1)
```
```monospace
Elevator is now on floor 1
Elevator is now on floor 2
Elevator is now on floor 3
Elevator is now on floor 4
Elevator is now on floor 5
Already at the 5 floor.
Elevator is now on floor 5
Elevator is now on floor 4
Elevator is now on floor 3
Elevator is now on floor 2
Elevator is now on floor 1
Already at the 1 floor.
It is the bottom floor.
```
## 10.2
Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building. When a building is created, the building creates the required number of elevators. The list of elevators is stored as a property of the building. Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main program, write the statements for creating a new building and running the elevators of the building.
```python
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def go_to_floor(self, floor):

        if floor < self.bottom or floor > self.top:
            print("Invalid floor.")
            return

        print(f"Elevator is now on floor {self.current_floor}")

        while self.current_floor < floor:  # Move up if below target floor
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

        while self.current_floor > floor:  # Move down if above target floor
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

        print(f"Already at the {floor} floor.")

        if self.current_floor == self.bottom:
            print("It is the bottom floor.")
        if self.current_floor == self.top:
            print("It is the top floor.")

class Building:
    def __init__(self, bottom,top,numbers):
        self.bottom = bottom
        self.top = top
        # 创建指定数量的电梯并将它们存储在列表中,_ in Loop循环中未使用的一次性变量
        self.elevators = [Elevator(bottom, top) for _ in range(numbers)]

    def run_elevator(self, elevator_num, destination_floor):
        if 1 <= elevator_num <= len(self.elevators):
            print(f"\nRunning elevator {elevator_num} to floor {destination_floor}:")
            self.elevators[elevator_num-1].go_to_floor(destination_floor)

        else:
            print("Invalid elevator number.")

building = Building(1, 7, 3)
building.run_elevator(0, 3)
building.run_elevator(1, 3)
building.run_elevator(3, 8)
```
```monospace
Invalid elevator number.

Running elevator 1 to floor 3:
Elevator is now on floor 1
Elevator is now on floor 2
Elevator is now on floor 3
Already at the 3 floor.

Running elevator 3 to floor 8:
Invalid floor.
```
## 10.3
Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor. Continue the main program by causing a fire alarm in your building.
```python
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def go_to_floor(self, floor):

        if floor < self.bottom or floor > self.top:
            print("Invalid floor.")
            return

        print(f"Elevator is now on floor {self.current_floor}")

        while self.current_floor < floor:  # Move up if below target floor
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

        while self.current_floor > floor:  # Move down if above target floor
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

        print(f"Already at the {floor} floor.")

        if self.current_floor == self.bottom:
            print("It is the bottom floor.")
        if self.current_floor == self.top:
            print("It is the top floor.")

class Building:
    def __init__(self, bottom,top,numbers):
        self.bottom = bottom
        self.top = top
        # 创建指定数量的电梯并将它们存储在列表中,_ in Loop循环中未使用的一次性变量
        self.elevators = [Elevator(bottom, top) for _ in range(numbers)]

    def run_elevator(self, elevator_num, destination_floor):
        if 1 <= elevator_num <= len(self.elevators):
            print(f"\nRunning elevator {elevator_num} to floor {destination_floor}:")
            self.elevators[elevator_num-1].go_to_floor(destination_floor)

        else:
            print("Invalid elevator number.")

    def fire_alarm(self):
        print("\nFire alarm! Moving all elevators to the bottom floor.")
        for i in range(len(self.elevators)):
            print(f"\nMoving elevator {i + 1} to the bottom floor:")
            self.elevators[i].go_to_floor(self.bottom)


building = Building(1, 7, 3)
building.run_elevator(1, 3)
building.run_elevator(2, 4)
building.run_elevator(3, 2)

building.fire_alarm()
```
```monospace
Running elevator 1 to floor 3:
Elevator is now on floor 1
Elevator is now on floor 2
Elevator is now on floor 3
Already at the 3 floor.

Running elevator 2 to floor 4:
Elevator is now on floor 1
Elevator is now on floor 2
Elevator is now on floor 3
Elevator is now on floor 4
Already at the 4 floor.

Running elevator 3 to floor 2:
Elevator is now on floor 1
Elevator is now on floor 2
Already at the 2 floor.

Fire alarm! Moving all elevators to the bottom floor.

Moving elevator 1 to the bottom floor:
Elevator is now on floor 3
Elevator is now on floor 2
Elevator is now on floor 1
Already at the 1 floor.
It is the bottom floor.

Moving elevator 2 to the bottom floor:
Elevator is now on floor 4
Elevator is now on floor 3
Elevator is now on floor 2
Elevator is now on floor 1
Already at the 1 floor.
It is the bottom floor.

Moving elevator 3 to the bottom floor:
Elevator is now on floor 2
Elevator is now on floor 1
Already at the 1 floor.
It is the bottom floor.
```
## 10.4
This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race. The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class. The class has the following methods:

hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.

print_status, which prints out the current information of each car as a clear, formatted table.

race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
  
Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method to check if the race has finished. The current status is printed out using the print_status method every ten hours and then once more at the end of the race.
```python
import random

class Car:
    def __init__(self, number, max_speed, speed=0, distance=0):
        self.number = number
        self.max_speed = max_speed
        self.speed = speed
        self.distance = distance

    def accelerate(self, speed_change):
        self.speed += speed_change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0

    def drive(self, time_hours):
        self.distance += time_hours * self.speed

    def car_info(self):
        highlight = "\033[93m" if self.distance >= 8000 else ""
        reset = "\033[0m"  # Reset color
        print(
            f"{highlight}{self.number:<15}{self.max_speed:<20}"
            f"{self.speed:<25}{self.distance:<20}{reset}"
        )

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(speed_change=random.randint(-10, 15))
            car.drive(1)

    def print_status(self, hour):
        print(f"\nStatus after {hour} hour(s):")
        print(f"{'Registration':<14} {'Max Speed (km/h)':<19} {'Current Speed (km/h)':<24} {'Distance (km)':<20}")
        print("-" * 75)
        for car in self.cars:
            car.car_info()

    def race_finished(self):
        return any(car.distance >= self.distance for car in self.cars)


# Create a list of cars
cars = []
for i in range(1, 11):
    car_name = f"ABC-{i}"
    new_car = Car(car_name, random.randint(100, 200))
    cars.append(new_car)

# Create a race
race = Race("Grand Demolition Derby", 8000, cars)

# Simulate the race
hours = 0
while not race.race_finished():
    hours += 1
    race.hour_passes()

    if hours % 10 == 0:  # Print status every 10 hours
        race.print_status(hours)

# Final status print after the race finishes
race.print_status(hours)
print(f"\nRace finished after {hours} hours!")
```
```monospace
Status after 10 hour(s):
Registration   Max Speed (km/h)    Current Speed (km/h)     Distance (km)       
---------------------------------------------------------------------------
ABC-1          176                 60                       367                 
ABC-2          173                 30                       130                 
ABC-3          182                 55                       333                 
ABC-4          151                 9                        56                  
ABC-5          111                 20                       194                 
ABC-6          157                 6                        12                  
ABC-7          178                 32                       140                 
ABC-8          169                 31                       145                 
ABC-9          113                 40                       248                 
ABC-10         115                 13                       130
             
...
...

Status after 60 hour(s):
Registration   Max Speed (km/h)    Current Speed (km/h)     Distance (km)       
---------------------------------------------------------------------------
ABC-1          176                 162                      5651                
ABC-2          173                 145                      5811                
ABC-3          182                 172                      7635                
ABC-4          151                 102                      3104                
ABC-5          111                 111                      2649                
ABC-6          157                 126                      2129                
ABC-7          178                 178                      6304                
ABC-8          169                 50                       2177                
ABC-9          113                 92                       4326                
ABC-10         115                 47                       2152                

Status after 63 hour(s):
Registration   Max Speed (km/h)    Current Speed (km/h)     Distance (km)       
---------------------------------------------------------------------------
ABC-1          176                 150                      6107                
ABC-2          173                 147                      6235                
ABC-3          182                 182                      8171                
ABC-4          151                 105                      3429                
ABC-5          111                 108                      2979                
ABC-6          157                 157                      2561                
ABC-7          178                 164                      6816                
ABC-8          169                 26                       2281                
ABC-9          113                 71                       4555                
ABC-10         115                 59                       2320                

Race finished after 63 hours!

```
# 11. Inheritance
## 11.1
Implement the following class hierarchy using Python: A publication can be either a book or a magazine. Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor. Also write the required initializers to both classes. Create a print_information method to both subclasses for printing out all information of the publication in question. In the main program, create publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both publications using the methods you implemented.
```python
# Base class Publication
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication Name: {self.name}")

# Subclass Magazine
class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")

# Subclass Book
class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.pages}")

# Main program
# Creating publications
magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192)

# Printing information of each publication
print("Magazine Information:")
magazine.print_information()
print("\nBook Information:")
book.print_information()
```
```monospace
Magazine Information:
Publication Name: Donald Duck
Chief Editor: Aki Hyyppä

Book Information:
Publication Name: Compartment No. 6
Author: Rosa Liksom
Page Count: 192
```
## 11.2
Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have the capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in liters as their property. Write initializers for the subclasses. For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter. It calls the initializer of the base class to set the first two properties and then sets its capacity. Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.
```python
# Base Car class
class Car:
    def __init__(self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.current_speed = 0
        self.kilometer_counter = 0

    def set_speed(self, speed):
        # Sets the speed without exceeding max_speed
        self.current_speed = min(speed, self.max_speed)

    def drive(self, hours):
        # Calculates distance traveled and updates kilometer counter
        distance = self.current_speed * hours
        self.kilometer_counter += distance

    def print_information(self):
        # Prints the basic information of the car
        print(f"Registration Number: {self.number}")
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        # Print kilometer counter in yellow
        print(f"Kilometer Counter: \033[33m{self.kilometer_counter} km\033[0m")

# Subclass for ElectricCar
class ElectricCar(Car):
    def __init__(self, number, max_speed, battery):
        super().__init__(number, max_speed)
        self.battery = battery  # in kilowatt-hours

    def print_information(self):
        super().print_information()  # Print basic car information
        print(f"Battery Capacity: {self.battery} kWh")

# Subclass for GasolineCar
class GasolineCar(Car):
    def __init__(self, number, max_speed, volume):
        super().__init__(number, max_speed)
        self.volume = volume  # in liters

    def print_information(self):
        super().print_information()  # Print basic car information
        print(f"Tank Volume: {self.volume} liters")

# Main program
# Create an electric car and a gasoline car
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

# Set speeds for both cars
electric_car.set_speed(200)
gasoline_car.set_speed(150)

# Drive each car for 3 hours
electric_car.drive(3)
gasoline_car.drive(3)

# Print out information and kilometer counters for both cars
print("\nElectric Car Information:")
electric_car.print_information()

print("\nGasoline Car Information:")
gasoline_car.print_information()
```
```monospace
Electric Car Information:
Registration Number: ABC-15
Max Speed: 180 km/h
Current Speed: 180 km/h
Kilometer Counter: 540 km
Battery Capacity: 52.5 kWh

Gasoline Car Information:
Registration Number: ACD-123
Max Speed: 165 km/h
Current Speed: 150 km/h
Kilometer Counter: 450 km
Tank Volume: 32.3 liters
```
# 12. Using external interfaces
## 12.1
Write a program that fetches and prints out a random Chuck Norris joke for the user. Use the API presented here: https://api.chucknorris.io/. The user should only be shown the joke text.
```python

```
```monospace

```
## 12.2
Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a program that asks the user for the name of a municipality and then prints out the corresponding weather condition description text and temperature in Celsius degrees. Take a good look at the API documentation. You must register for the service to receive the API key required for making API requests. Furthermore, find out how you can convert Kelvin degrees into Celsius.
```python

```
```monospace

```
# 13. Setting up a backend service with an interface
## 13.1
Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not. Use the prior prime number exercise as a starting point. For example, a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number/31. The response must be in the format of {"Number":31, "isPrime":true}.
```python

```
```monospace

```
## 13.2
Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport in JSON format. The information is fetched from the airport database used on this course. For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK. The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.
```python
zz
```
```monospace

```


