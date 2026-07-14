#BMI CALCULATOR

height = float(input("Enter your Height: "))
weight = float(input("Enter your weight: "))

bmi = weight/(height*height)

print("Your BMI is: ",round(bmi,5))