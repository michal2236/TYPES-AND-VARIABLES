height = int(input("Enter your height in cm:"))
weight = int(input("Enter your weight in kg:"))
bmi = weight/(height/100)**2
print(f"BMI index: {round(bmi, 2)}")