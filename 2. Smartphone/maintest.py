import smartphone
import pickle

def create_phones(n):
    file = open('phones.dat', 'wb')
    for i in range(n):
        print("Telefon nr: ",i+1)
        manufacturer = input("Podaj producenta: ")
        model = input("podaj model: ")
        price = float(input("Podaj cene"))
        phone = smartphone.Smartphone(manufacturer, model, price)
        pickle.dump(phone, file)

    file.close()

create_phones(2)

file = open('phones.dat', 'rb')

for i in range(2):
    print("\nTelefon nr: ", i+1)
    phone = pickle.load(file)
    print(phone)

file.close
