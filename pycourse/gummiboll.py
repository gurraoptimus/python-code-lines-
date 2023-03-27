#.Förlorar 30% stutsaid
#boll = input("hur många meter släpps från marken:")
#boll = float(boll)
#stuts = 0
#while 0.01 < boll:
    #boll = boll *0.7
    #stuts = stuts + 1
#print(stuts)

#.Förlorar 30% stutsaid
while True:
    boll = input("hur många meter släpps från marken:")
    boll = float(boll)
    stuts = 0
    if boll<=0:
        break
    while 0.01 < boll:
        boll = boll *0.7
        stuts = stuts + 1
    print(stuts) 