a = input("första talet:")
a = float(a)
b = input("andra talet:")
b = float(b)   
option = input("räknesätt:")
if option =="+":
    c = a + b
elif option =="-":
    c = a - b
elif option == "/":
    c = a / b
else: 
    c = a*b
print("ressultat är:",c)
