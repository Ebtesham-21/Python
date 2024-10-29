# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_new = float(height)
weight_new = float(weight)
BMI = weight_new / (height_new * height_new)
print(int(BMI))
if(BMI > 18 and BMI < 24): print("good bmi")
else:print("Bad BMI")