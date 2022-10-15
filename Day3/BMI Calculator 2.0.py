height =  float(input("What is your height in meter ? "))
weight = float(input("What is weigth in kg ? "))
BMI = weight/height** 2
BMI = round(BMI,2)

if BMI < 18.5:
    print(f"You BMI is {BMI} ,  and you are underweight .")
elif BMI < 25:
    print(f"You BMI is {BMI} ,  and you have normal weight .")
elif BMI < 30:
    print(f"You BMI is {BMI} ,  and you are overweight .")
elif BMI < 35:
    print(f"You BMI is {BMI} ,  and you are obese .")
else:
    print(f"You BMI is {BMI} ,  and you are clinically obese .")