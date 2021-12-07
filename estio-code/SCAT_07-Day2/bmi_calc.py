# bmi_calc with if elif and else

weight = eval(input("Enter your weight in pounds: "))
height = eval(input("Enter your height in inches: "))

kg_per_pound = 0.45359237
meters_per_inch = 0.0254

weight_in_kg = weight * kg_per_pound
height_in_inches = height * meters_per_inch

bmi = weight_in_kg / (height_in_inches ** 2)

print("BMI is", format(bmi, ".2f"))

if (bmi > 12) and (bmi <=18.5):
    print("You're underweight")
elif (bmi > 18.5) and (bmi < 24.5):
    print("You're healthy")
elif (bmi >= 24.5) and (bmi < 30):
    print("You're overweight")
elif (bmi >= 30) and (bmi < 39):
    print("You're obese")
else:
    print("You're extremely obese")
