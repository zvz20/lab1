a = float(input("Enter a first number: "))
b = float(input("Enter a secound number: "))
dia = input("Dia = ")
if dia == "+":
    res1 = (a+b)
elif dia == "-":
    res1 = (a+b)
elif dia == "/":
    res1 = (a/b)
elif dia == "*":
    res1 = (a*b)
elif dia == "**":
    res1 = (a**b)
else:
    res1 = (a/0)
print(res1)
c = float(input("Enter a 3 number: "))
dia2 = input("Dia = ")
if dia2 == "+":
    res2 = (res1+c)
elif dia2 == "-":
    res2 = (res1-c)
elif dia2 == "/":
    res2 = (res1/c)
elif dia2 == "*":
    res2 = (res1*c)
elif dia2 == "**":
    res2 = (res1**c)
print(res2)