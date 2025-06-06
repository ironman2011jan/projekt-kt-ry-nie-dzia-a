import random
znaki = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*"
wylosuj = int(input("podaj długósc hasła"))
hasło = "" 
for i in range(wylosuj):
    r = random.randint(0,len(znaki)-1)
    hasło += znaki[r]
print(hasło)
