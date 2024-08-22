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
m = lots * 13.3 + pounds * 13.3 * 32 + talents * 13.3 * 32 *20
kilograms = m // 1000
grams = m % 1000
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













