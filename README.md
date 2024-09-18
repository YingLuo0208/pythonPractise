import math
import random
# 2.Variables and interactive programs
## 2.1
Write a program that asks your name and then greets you by your name: Examples:
If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!.

```python
name = input("Enter your name: ")
print(f"Hello {name}")
```

## 2.2
Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

```python
radius = float(input("Enter your radius: "))
area = math.pi * radius**2
print(f"The area is {area:.2f}")
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

## 2.6
Write a program that draws two random combinations of numbers for a combination lock:
a 3-digit code where each number is between 0 and 9.
a 4-digit code where each number is between 1 and 6.

```python
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

## 3.2
Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below.You must use an if/elif/else structure in your solution.
LUX: upper-deck cabin with a balcony.
A: above the car deck, equipped with a window.
B: windowless cabin above the car deck.
C: windowless cabin below the car deck.
If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

```python
cabin_class = input("Please enter the cabin class of a cruise ship:")
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


## 4.4
Write a game where the computer draws a random integer between 1 and 10.
The user tries to guess the number until they guess the right number.
After each guess the program prints out a text: Too high, Too low or Correct.
Notice that the computer must not change the number between guesses.

```python
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
    
# 5. List structures and iterative loops (for)
## 5.1
Write a program that asks the user how many dice to roll.
The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

```python
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

## 5.3
Write a program that asks the user for an integer and tells if the number is a prime number.
Prime numbers are number that are only divisible by one or the number itself.
For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

```python
user_num = int(input("Enter a number: "))
divided_by = []

if user_num <= 1 :
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

# 6. Functions
## 6.1
Write a function that returns a random dice roll between 1 and 6.The function should not have any parameters.
Write a main program that rolls the dice until the result is 6.The main program should print out the result of each roll.

```python
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


## 6.2
Modify the function above so that it gets the number of sides on the dice as a parameter.
With the modified function you can for example roll a 21-sided role-playing dice.
The difference to the last exercise is that the dice rolling in the main program continues until the program gets the maximum number on the dice,which is asked from the user at the beginning.

```python
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

## 6.6
Write a function that receives two parameters:the diameter of a round pizza in centimeters and the price of the pizza in euros.
The function calculates and returns the unit price of the pizza per square meter.
The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money(which of them has a lower unit price).
You must use the function you wrote for calculating the unit prices.

```python
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

# 7. Tuple, set, and dictionary
## 7.1
Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter).
Save the seasons as strings into a tuple in your program.
We can define each season to last three months,December being the first month of winter.




## 7.2
Write a program that asks the user to enter names until he/she enters an empty string.
After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time.
Finally, the program lists out the input names one by one,one below another in any order. Use the set data structure to store the names.




## 7.3
Write a program for fetching and storing airport data.
The program asks the user if they want to enter a new airport,fetch the information of an existing airport or quit.
If the user chooses to enter a new airport,the program asks the user to enter the ICAO code and name of the airport.
If the user chooses to fetch airport information instead,the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit,the program execution ends.
The user can choose a new option as many times they want until they choose to quit.
(The ICAO code is an identifier that is unique to each airport.For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.You can easily find the ICAO codes of different airports online.)






