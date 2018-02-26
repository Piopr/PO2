import smartphone

list_of_objects = []
for x in range(2):
    tmp = smartphone.Smartphone()
    tmp.setManofacturer(input("Podaj marke: "))
    tmp.setModel(input("Podaj model: "))
    tmp.setPrice(int(input("Podaj cene: ")))
    list_of_objects.append(tmp)

for x in list_of_objects:    
    i=1
    print("Telefon nr: ", i)
    print("Marka: ", x.getManofacturer())
    print("Model: ", x.getModel())
    print("Cena: ", x.getPrice())
    i+=1
    
