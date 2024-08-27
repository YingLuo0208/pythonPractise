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
'''

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