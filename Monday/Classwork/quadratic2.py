a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b*b - 4*a*c

x1 = (-b + D**0.5) / (2*a)
x2 = (-b - D**0.5) / (2*a)

print("x1 = {0}\nx2 = {1}".format(x1, x2))
