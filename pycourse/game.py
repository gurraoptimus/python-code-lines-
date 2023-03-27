#k = 0
#while True:
    #print(f"{k:2}",end="")
#if k >=6:
        #break
    #k = k + 2

#k = 0
#while k<6:
   # k =k+1
    #if  k% 2 != 0:
     #   continue
    #print(f"{k:2}",end ="")

while True:
    n = int(input("n:"))
    if n<=0:
        break
    summa =0
    k=1
    while k<=n:
        summa = summa+k
        k=k+1
    print("summa blir ",summa)