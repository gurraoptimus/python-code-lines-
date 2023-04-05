tal=0
störst=0
minst= 2000
while tal >= 0:
    tal =int(input("tal:"))

    if störst <tal and tal>0:
        störst=tal
    if minst> tal and tal>0:
        minst=tal
print("störst:",störst)
print("minst:",minst)