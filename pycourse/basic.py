#n = input('Skriv ditt namn: ')
#print('Hej', n)
#old = input("hur gammal är du:" )
#print("jag är:", old ,("år:") )

#tal1 = input("skriv ett heltal:")
#tal2 = input("skriv ett decimaltal:")
#tal1 = int (tal1)
#tal2 = float(tal2)
#summa = tal1 + tal2
#print ("summa är", summa)

#i=30
#temp = input("Temperatur:")
#temp = float(temp)
#if temp >=i:
    #print("det är varmt")
    #print("ta med dig en vattenfalska")
#elif temp <=18:
#print("det är kalt")
#print("ta med dig en varm tröja")
#else:
#print("det är lagom Temperatur")

import datetime
born = input("när är du född:" )
born = int(born)
ct = datetime.datetime.now()
print("jag är:", ct.year - born, "år" )
