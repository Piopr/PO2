import Account



    
test = Account.Account(1500)
#print(test.show_balance())
print(test)
wplata = int(input("Podaj kwote do wplaty: "))
test.pay(wplata)
print(test)
wyplata = int(input("Podaj kwote do wyplaty: "))
test.take(wyplata)
print(test)

