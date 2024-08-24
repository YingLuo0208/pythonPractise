import math
import random

##2.1
name = input("Enter your name: ")
print(f"Hello {name}")

##2.2
radius = float(input("Enter your radius: "))
area = math.pi * radius**2
print(f"The area is {area:.2f}")

##2.3
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = (length + width)*2
area = length * width
print(f"The perimeter is {perimeter:.2f},The area is {area:.2f}")

##2.4
num1 = float(input("input number1: "))
num2 = float(input("input number2: "))
num3 = float(input("input number3: "))
sum = num1 +num2 +num3
product = num1*num2*num3
average = sum/3
print(f"The sum is {sum:.2f},The product is {product:.2f},The average is {average:.2f}")

##2.5
talents = float(input("input talents: "))
pounds = float(input("input pounds: "))
lots = float(input("input lots: "))
total = lots * 13.3 + pounds * 13.3 * 32 + talents * 13.3 * 32 *20
kilograms = total // 1000
grams = total % 1000
print(f"The weight in modern units: \n{kilograms:.0f} kilograms and {grams:.2f} grams.")

##2.6
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


##3
##1.Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit,
# the program instructs to release the fish back into the lake
# and notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.
length = float(input("The length of a zander in centimeters is: "))
if length >= 42:
    print("You can keep the fish.")
else:
    print("A zander must be 42 centimeters or longer to meet the size limit.\n"
           "Please release the fish back into the lake.")
    

##2.Write a program that asks the user to enter the cabin class of a cruise ship
# and then prints out a written description according to the list below.
# You must use an if/elif/else structure in your solution.
##  LUX: upper-deck cabin with a balcony.
##  A: above the car deck, equipped with a window.
##  B: windowless cabin above the car deck.
##  C: windowless cabin below the car deck.
##  If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.
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


##3.Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
##  A normal hemoglobin value for adult females is between 117-155 g/l.
##  A normal hemoglobin value for adult males is between 134-167 g/l.
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


##4.Write a program that asks the user to enter a year
# and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.
year = int(input("Enter year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")
'''


##4
##1.Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.



##2.Write a program that converts inches to centimeters until the user inputs a negative value.
# Then the program ends.




##3.Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.





##4.Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.





##5.Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.
# The correct username is python and password rules.





##6.Implement an algorithm for calculating an approximation for the value of pi (π).
# Let's assume that A is a unit circle. A unit circle has the radius of one
# and it is centered at the origin (0,0). Smallest possible square B is drawn around the unit circle
# so that circle A is completely inside the square.
# The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1).
# If a large number of random points are scattered inside the square,
# the fraction of points that fall inside the circle A correlates with
# the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4.
# This can be used as a simple method for calculating an approximation of the value of pi:
# Let's generate a large number of random points, such as one million, inside square B.
# Let N be the total number of random points.
# Each point inside the square is tested for whether it resides inside circle A.
# Let n be the total number of points that fall inside circle A.
# Now we have n/N≈π/4, and from that we get π≈4n/N.
# Write a program that asks the user how many random points to generate,
# and then calculates the approximate value of pi using the method explained above.
# At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).













