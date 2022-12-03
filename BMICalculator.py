weight=int(input())
height=float(input())

height=height**2
health=weight/height
if health<18.5:
    print("Underweight")
elif health>=18.5 and health<25:
    print("Normal")
elif health>=25 and health<30:
    print("Overweight")
else:
   print("Obesity")