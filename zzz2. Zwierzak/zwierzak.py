class Pet:
    def __init__(self, name, hunger = 0, tiredness = 0):
        self.name = name
        self.hunger = hunger
        self.tiredness = tiredness        

    def _passage_of_time(self):
        self.hunger+=1
        self.tiredness+=1

    @property
    def mood(self):
        if self.hunger + self.tiredness < 5:            
            return 'szczęśliwy'
        elif self.hunger + self.tiredness <=10:            
            return 'zadowolony'
        elif self.hunger + self.tiredness <=15:            
            return 'podenerwowany'
        elif self.hunger + self.tiredness >15:            
            return 'wściekły'
        else:
            print("Coś poszło źle")



    def talk(self):
        self._passage_of_time()
        print("{0} jest {1}.".format(self.name, self.mood))
        

    def eat(self, food = 4):
        self._passage_of_time()
        self.hunger-=food
        print("om nom nom")
        

    def play(self, fun = 4):
        self._passage_of_time()
        self.tiredness-= fun
        print(self.name, " bawi sie piłką.")

    def __str__(self):
        return '''Nazwa zwierzaka: {}
Poziom głodu: {}
Poziom znudzenia: {}
Nastrój: {}'''.format(self.name, self.hunger, self.tiredness, self.mood)
        


def menu():
    print("1. Zwierzak daje głos.")
    print("2. Nakarm zwierzaka (wpisz \"2 ilosc_pokarmu\" aby nakarmić nistandardową ilością")
    print("3. Baw się (wpisz \"3 ilosc_czasu\" aby bawić się niestandardową długość czasu")
    print("4. Wyświetl informacje o zwierzaku.")
    print("5. Koniec")
    

def main():
    nazwa_zwierzaka = input("Podaj nazwę zwierzaka\n")
    zwierzak = Pet(nazwa_zwierzaka)
      
    while True:
        menu()
        option = input("Opcja: ").split(" ")  
        if option[0] == '1':
            zwierzak.talk()
        elif option[0]=='2':
            try:
                option[1]
            except IndexError:
                zwierzak.eat()
            else:
                zwierzak.eat(int(option[1]))
        elif option[0]=='3':
            try:
                option[1]
            except IndexError:
                zwierzak.play()
            else:
                zwierzak.play(int(option[1]))
        elif option[0] == '4':
            print(zwierzak)
        elif option[0]== '5':
            print(zwierzak)
            break
        else:
            print("Zła opcja!")        
            

if __name__ == "__main__":
    main()    
          
    
    
    





    

    
        
    
