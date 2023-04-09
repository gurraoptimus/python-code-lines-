# a = input("vad är ditt namn:")
# b = int(input("när är du född:"))
# ar = 2023 -b
# print(ar)

import datetime
n = input("vad är ditt namn:")
f = int(input("när är du född:"))
ct = datetime.datetime.now()
ar = ct.year-f
for i in range(100):
   print(i+1,n,ar,ct.year)