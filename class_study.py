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

'''

age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))
if age >= 18 or (age >=18 or age>=15 and weight >=55):
    print("The medicine can be used.")



