class Smartphone:
    def __init__(self):
        _manufacturer=""
        _model=""
        _price=0.0
    def setManofacturer(self, name):
        self._manufacturer=name
    def setModel(self, name):
        self._model=name
    def setPrice(self, name):
        self._price=name
    def getManofacturer(self):
        return self._manufacturer
    def getModel(self):
        return self._model
    def getPrice(self):
        return self._price
        
        
    
