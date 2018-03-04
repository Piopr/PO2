class RocketEngine:    
    count = 0
    all_power = 0
    #def __init__(self):
     #   self.name = False
      #  self.power = False
       # self.working = False
        #RocketEngine.count+=1
    def __init__(self, nazwa = False, moc = False):
        self.name = nazwa
        self.power = moc
        self.working = False
        RocketEngine.count+=1
    def start(self):
        if self.working==False:
            RocketEngine.all_power+=self.power
            self.working=True

    def stop(self):
        if self.working==True:
            RocketEngine.all_power+=self.power
            self.working=False

    def __str__(self):
        to_return="Silnik \"{0}\":\n\tMoc: {1}\n\tCzy pracuje: {2}".format(self.name, self.power, self.working)
        return to_return
    def __del__(self):
        RocketEngine.count-=1
    @staticmethod
    def status():
        print("Ilosc silnikow: {0}\nIlosc mocy: {1}".format(RocketEngine.count, RocketEngine.all_power))
        
            
print("Komputer pokładowy: Witaj Komandorze! Czas wyruszyć na misję w sektorze Hawkinge Eta.")
print("Komputer pokładowy: Punkt startowy: Mgławica Węża, Cytadela")
print("Komputer pokładowy: Punkt pośredni: Strefa DMZ Krogan, przekaźnik")
print("Komputer pokładowy: Proszę o rozkaz stworzenia silników manewrowych, by zbliżyć się do przekaźnika masy.")
print("Komandor: Stwórz dwa silniki manewrowe o mocy 50")
manewrowy1=RocketEngine("Manewrowy 1", 50)
manewrowy2=RocketEngine("Manewrowy 2", 50)
print(manewrowy1)
print(manewrowy2)
RocketEngine.status()
print("\nKomandor: Uruchom silniki manewrowe i zbliż się do przekaźnika masy")
manewrowy1.start()
manewrowy2.start()
print(manewrowy1)
print(manewrowy2)
RocketEngine.status()
print("\nKomputer pokładowy: Zbliżyliśmy się do przekaźnika.")
print("Komandor: Wyłącz silniki manewrowe, stwórz silniki rozpędzające.")
manewrowy1.stop()
manewrowy2.stop()
print(manewrowy1)
print(manewrowy2)
rozpedzajacy1=RocketEngine("Rozpedzajacy 1",500)
rozpedzajacy2=RocketEngine("Rozpedzajacy 2",500)
print("\nKomputer pokładowy: Silniki stworzone.")
print("Komandor: Zamknij się i wyświetl statusy silników.")
print(rozpedzajacy1)
print(rozpedzajacy2)
RocketEngine.status()
print("\nKomandor: Rozpędź się by nabrać mocy z przekaźnika i stworzyć silniki szybkiej podrózy")
rozpedzajacy1.start()
rozpedzajacy2.start()
print(rozpedzajacy1)
print(rozpedzajacy2)
RocketEngine.status()
print("\nKomputer pokładowy: Wystarczająca prędkość i zebrana moc, by wytworzyć silniki szybkiej podróży.")
print("Komandor: Stworz silniki szybkiej podrózy, moc 400000")
szybkiej_podrozy1=RocketEngine("Szybkiej podrozy 1", 400000)
szybkiej_podrozy2=RocketEngine("Szybkiej podrozy 2", 400000)
print(szybkiej_podrozy1)
print(szybkiej_podrozy2)
RocketEngine.status()
print("\nKomandor: przełącz silniki na silniki szybkiej podróży")
rozpedzajacy1.stop()
rozpedzajacy2.stop()
szybkiej_podrozy1.start()
szybkiej_podrozy2.start()
print(rozpedzajacy1)
print(rozpedzajacy2)
print(szybkiej_podrozy1)
print(szybkiej_podrozy2)
RocketEngine.status()
print("\nKomputer pokładowy: Zgromadzono wystarczającą ilość mocy, by wytworzyć nowe silniki. Zniszczyć manewrowe i rozpędzające?")
print("Komandor: Zniszczyć! I przekazać kucharzowi by podał obiad.")
del manewrowy1
del manewrowy2
del rozpedzajacy1
del rozpedzajacy2
RocketEngine.status()
print("Komputer pokładowy: Energia z zniszczoncyh silników zgromadzona.")
print("\nKomputer pokładowy: Zbliżamy się do przekaźnika w gromadzie Hawking Eta.")
print("Komputer pokładowy: Przypominam o procedurze niszczenia silników szybkiej podróży, by uniknąć przeciążenia.")
print("Komandor: Stworzyć silniki manewrowe, przełączyć z silników szybkiej podróży i zniszczyć je.")
manewrowy1=RocketEngine("Manewrowy 1", 50)
manewrowy2=RocketEngine("Manewrowy 2", 50)
print(manewrowy1)
print(manewrowy2)
RocketEngine.status()
szybkiej_podrozy1.stop()
szybkiej_podrozy2.stop()
print(szybkiej_podrozy1)
print(szybkiej_podrozy2)
manewrowy1.start()
manewrowy2.start()
print("\nKomandor: Dobrze, teraz zniszczyć silniki szybkiej podróży.")
del szybkiej_podrozy1
del szybkiej_podrozy2
print("\nKomputer pokładowy: Procedura przebiegła pomyślnie.")
RocketEngine.status()
print("\nZbliż się do doków")







