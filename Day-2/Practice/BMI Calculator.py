height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

m = float(height)
kg = int(weight)
formula = kg / m**2

# print(f"{kg} % ({m} x {m}) = {formula}")

BMI = int(formula)
print(BMI)