# 🚨 Don't change the code below 👇🏻
height = input(' Enter your height in m: ')
weight = input(' Enter your weight in kg: ')
# 🚨 Don't change the code above 👆🏻

####################################
# Write your code below this line 👇🏻

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = int(weight) / float(height) ** 2

# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)

# Write your code above this line 👆🏻
####################################