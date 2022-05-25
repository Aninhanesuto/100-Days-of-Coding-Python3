# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
operacao = (weight/(height**2))
op = round(operacao)
if operacao < 18.5:
	print(f"Your BMI is {op}, you are underweight.")
elif operacao > 18.5 and operacao < 25:
	print(f"Your BMI is {op}, you have a normal weight.")
elif operacao > 25 and operacao < 30:
	print(f"Your BMI is {op}, you are slightly overweight.")
elif operacao > 30 and operacao < 35:
	print(f"Your BMI is {op}, you are obese.")
elif operacao > 35:
	print(f"Your BMI is {op}, you are clinically obese.")