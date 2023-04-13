n =int(input("hur många siffror vill du ta ut i kvadrat:"))

for i in range(1,n+1):
    print(f"{i:3} {i*i:4} {i*i*i:5}")