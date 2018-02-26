class Account:
    def __init__(self):
        _balance=0
    def __init__(self, _balance):
        self._balance = _balance
    def pay(self, how_many):
        if how_many>0:
            self._balance+=how_many
    def take(self, how_many):
        if how_many>0:
            if self._balance-how_many>=0:
                self._balance-=how_many
            else:
                print("Masz za malo srodkow na koncie")
    def show_balance(self):
        return self._balance
    def __str__(self):
        #B = self.show_balance
        return 'Twoje saldo: {B}'.format(B=self._balance)
    
        
