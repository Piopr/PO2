class Pet:
    def __init__(self, name, hunger = 0, tiredness = 0):
        self.name = name
        self.hunger = hunger
        self.tiredness = tiredness
        self.mood = 'szczęśliwy'

    def _passage_of_time(self):
        self.hunger+=1
        self.tiredness+=1

    @property
    def mood(self):
        if self.hunger + self.tiredness < 5:
            self._mood = 'szczęśliwy'
            return self._mood
        elif 5>= self.hunger + self.tiredness <=10:
            self._mood = 'zadowolony'
            return self._mood
        elif 11>= self.hunger + self.tiredness <=15:
            self._mood = 'podenerwowany'
            return self._mood
        elif self.hunger + self.tiredness >15:
            self._mood = 'wściekły'
            return self._mood
        else:
            print("Coś poszło źle")        

    @mood.setter
    def mood(self, zmiana):
        self._mood = zmiana

    def talk(self):
        print("{0} jest {1}.".format(self.name, self.mood))
        self._passage_of_time()

    def eat(self, food = 4):
        self.hunger-=food
        self._passage_of_time()

    def play(self, fun = 4):
        self.tiredness-= fun
        self._passage_of_time()

def main():
    nazwa_zwierzaka = input("Podaj nazwę zwierzaka\n")
    zwierzak = Pet(nazwa_zwierzaka)
    #while(True):
    print("1. Zwierzak daje głos.")
    print("2. Nakarm zwierzaka (wpisz \"2 ilosc_pokarmu\" aby nakarmić nistandardową ilością")
    print("3. Baw się (wpisz \"3 ilosc_czasu\" aby bawić się niestandardową długość czasu")
    print("4. Wyświetl informacje o zwierzaku.")
    print("5. Koniec")
      
    while True:
        option = input("Opcja: ").split(" ")  
        if option[0] == '1':
            zwierzak.talk()
        elif option[0] == '4':
            print(zwierzak)
        elif option[0]== '5':
            print(zwierzak)
            break
        elif option[0]=='2':
            try:
                option[1]
            except IndexError:
                zwierzak.eat()
            else:
                zwierzak.eat(int(option[1]))
        #dorobić obsługę opcji 3 i __str__
            

if __name__ == "__main__":
    main()    
          
    
    
    





    

    
        
    
