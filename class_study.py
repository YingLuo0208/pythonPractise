import math
import random

'''
## others ：
##2.6
code1 = tuple(random.randint(0, 9) for _ in range(3))
print(f'code1 is: {code1}')
code2 = tuple(random.randint(1, 6) for _ in range(4))
print(f'code2 is: {code2}')

##3.2
cabin_classes = {
    "LUX": "LUX: upper-deck cabin with a balcony.",
    "A": "A: above the car deck, equipped with a window.",
    "B": "B: windowless cabin above the car deck.",
    "C": "C: windowless cabin below the car deck."
}

cabin_class = input("Please enter the cabin class of a cruise ship: ")

if cabin_class in cabin_classes:
    print(cabin_classes[cabin_class])
else:
    print("Invalid cabin class.")

##3.4
gender = input("Please enter your biological gender (Male/Female): ")

if gender == "Male" or gender == "Female":
    value = float(input("Please enter your hemoglobin value: "))

    # 设置性别对应的血红蛋白阈值
    high_threshold = 155 if gender == "Male" else 167
    low_threshold = 117 if gender == "Male" else 134

    if value > high_threshold:
        print("Your hemoglobin is high.")
    elif value < low_threshold:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is normal.")
else:
    print("Input error.")


age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))
if age >= 18 or (15 <= age <= 18 and weight >=55):
    print("The medicine can be used.")

age = int(input("Enter your age: "))
if age >= 18 :
    print("Your age can be used.")
elif 15 <= age <= 18 :
    weight = int(input("Enter your weight: "))
    if weight >= 55:
        print("Your age can be used.")
    else:
        print("Your age can not be used.")



your_score = int(input("Enter your score: "))
if your_score >= 90:
    print("your grade is A1")
elif your_score >= 80:
    print("your grade is A2")
elif your_score >= 70:
    print("your grade is B1")
elif your_score >= 60:
    print("your grade is B2")
elif your_score >= 50:
    print("your grade is C1")
elif your_score >= 35:
    print("your grade is C2")
elif your_score < 35:
    print("Fail")


car_wheel = input("Enter your car wheels(2/3/4) : ")
if car_wheel == "2" :
    battery = input("If your car have battery?(Y/N) : ")
    if battery == "Y":
        print("You have an electric bikes.")
    elif battery == "N":
        print("You have a bike.")
    else:
        print("Input error.")
elif car_wheel == "3" :
    print("You have a tricycle.")
elif car_wheel == "4" :
    print("You have a car.")
else:
    print("Input error.")


age = int(input("Enter your age: "))
if age>=65:
    print("You are retired.")
elif age>=18:
    print("You are working-age.")
elif age>=7:
    print("You are in school.")
else:
    print("You are a small child.")


sun = 0
counter = 1
while counter <= 5:
    sun = sun + counter
    print(f"the counter is: {counter},and the sun is {sun}")
    counter = counter + 1


i = 1
n = int(input("Enter a limit: "))
while i <= n:
    if i % 2 == 0:
        print(f"{i} is an even number.")
    else :
        print(f"{i} is an odd number.")
    i = i + 1


number = int(input("Enter a number(1-9): "))
random_number = random.randint(1, 9)
times = 0
while True :
##  times = times + 1  或者加在这里
    if number != random_number:
        print("Try again!")
        number = int(input("Enter a number(1-9): "))
        times = times + 1
    else:
        print("well guessed!")

        break
print(f"Guessed {times} times")


user_input = " "
while user_input != "exit":
    user_input = input("Please enter your input: ")
    print("your typed",user_input)


coin = random.choice(['heads', 'tails'])
times = 1
while coin != 'heads':
    print("flipped",coin)
    coin = random.choice(['heads', 'tails'])
    times = times + 1
print("your flipped ",coin,", flipped ",times, "times")


first = 1
while first < 5 :
    second = 1
    while second < 5 :
        print(f"{first} time {second} is ",first * second)
        second += 1
    first += 1
    print("done")
print("all done")


for i in range(5):
    print(i)


names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
otherNames = ["Allu","Ninni"]
names.append("Matti")
names.remove("Pekka")
#数字代表插入的位置
names.insert(0, "Teppo")
#插入列表
names.extend(otherNames)

print(names)

names.sort()
print(names)

#返回指定项第一次出现的索引号
what_index = names.index("Olga")
print(what_index)

if "Mary" in names:
    print("Mary found")

for n in names:
    print(f"Hello, {n}!")

#第一个参数是起点，第二个参数是终点，第三个可选参数定义数字之间的步长。
for number in range(1,10,2):
    print(number)

for a in range(2):
    print(f"hello!,{a}")
'''

# print(" Maanantai \n Tiistai \n Keskiviikko \n Torstai \n perjantai \n Lauantai \n Sunnuntai \n")

# day = ["Mikä päivä tänään on?","Mikä päivä huomenna on?","Mikä päivä ylihuomenna on?",
#        "Mikä päivä eilen on?","Mikä päivä toissapäivänä on?"]
#
# while True:
#     user = input("1 is days of week and 2 is unmbers . Enter your number : ")
#
#     if user == "1":
#         today = random.randint(1, 7)
#         question = random.choice(day)
#         print("Today is : ", today)
#         print(question)
#
#     if user == "2":
#         number_1 = random.randint(0, 10)
#         number_2 = random.randint(0, 10)
#         print(number_1, " + ", number_2, " = ?")

# name = ["ab","bc","cd","ef"]
# print(id(name))
# name [3] = "xy"
# print(id(name))
#
# name = ["ab","bc","cd","ef"]
# print(id(name[3]))
# name [3] = "xy"
# print(id(name[3]))



# name = []
# user = input("Enter your name:")
#
# while user != "":
#     if "*" in user:
#         name_t = user.replace('*', '')
#         name.append(name_t)
#     else:
#         name.append(user)
#
#     user = input("Enter your name:")
#
# print(name)


# def greet():
#     print("Hello!")
#     return
#
# a = 1
# while a < 10:
#     b = 1
#     while b < 10:
#         print(f"{a} * {b} = {a*b}")
#         b += 1
#     a = a + 1
#
# def num_sum(a,b):
#     return a+b
#
# print(num_sum(2,3))
#
#
# def num_minus(a,b):
#     return a-b
#
# print(num_minus(2,3))
#
#
# def num_multiply(a,b):
#     return a*b
#
# print(num_multiply(2,3))
#
#
# def num_divide(a,b):
#     if b != 0:
#         return a/b
#
# print(num_divide(2,3))
#
# def num_count(a,b):
#     sum = a + b
#     minus = a - b
#     multiply = a * b
#     divide = a / b
#     if b != 0:
#         return sum, minus, multiply, divide
#
# print(num_count(2,3))
#
# num = [2,3,5,7,9,2,10,434,13,134]
#
# num_max = max(num)
# num_min = min(num)
#
# print(num_max)
# print(num_min)


# num.sort(reverse=True)
# print(num)
#
# nun_max = num[0]
# print(nun_max)
# num_min = num[-1]
# print(num_min)


# import math
#
# # Given values
# v0 = 6.5  # Initial velocity in m/s
# a = 0.48  # Acceleration in m/s^2
# angle = 35  # Angle of wind gust in degrees
# t = 6.3  # Time in seconds
#
# # Convert angle to radians for calculations
# angle_rad = math.radians(angle)
#
# # Components of acceleration
# a_x = a * math.cos(angle_rad)  # Along the original direction
# a_y = a * math.sin(angle_rad)  # Perpendicular to the original direction
#
# # Displacement along the original direction (d_x)
# d_x = v0 * t + 0.5 * a_x * t**2
#
# # Displacement perpendicular to the original direction (d_y)
# d_y = 0.5 * a_y * t**2
#
# # Magnitude of the total displacement
# d_total = math.sqrt(d_x**2 + d_y**2)
#
# # Direction of the displacement (angle relative to the original direction)
# theta = math.degrees(math.atan2(d_y, d_x))
#
# d_x, d_y, d_total, theta


def remove_odd_numbers(number):
# function takes list of integer, removes odd number and return only even number in new list
    return[num for num in number if num % 2==0]
#test function
#creating orignal list of integer
original_list=[1,1,1,1,2,2,3,4,5,56,6,7,8,9]
#call function to remove odd num
second_list=remove_odd_numbers(original_list)

#print result
print (f"original_list: {original_list}")
print (f"second_list:{second_list}")