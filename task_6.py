mass_lb = float(input())
height_in = float(input())
bmi = mass_lb/(height_in**2) * 4.53e-1 / (2.54e-2)**2
print(round(bmi, 2))
