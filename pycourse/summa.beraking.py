# beräkrna 1+2+3+...+n
#n =int(input("n:"))
#summa =0
#k = 1
#while k<=n:
   # summa = summa+ k*k
   # k = k+1
#print("summa blir",summa)

# for loop
n =int(input("n:"))
summa =0
for k in range(n):
    summa = summa + (k+1)*(k+1)
print("summa blir",summa)