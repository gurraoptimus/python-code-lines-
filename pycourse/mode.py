import random as rand
tal = input('Skriv ett heltal: ')
tal = int(tal)
slump = rand.randint(1,tal)

gissning = input('Vilket tal tror du jag slumpade?')
gissning = int(gissning)

if gissning > slump:
    print("Du gissade för högt!")
    print("Rätt svar var", slump)
elif gissning < slump:
    print("Du gissade för lågt!")
    print("Rätt svar var", slump)
else:
    print("du gissade rätt!")