from numbers import Real
import math

class Figure:
    def __init__(self, colour = True, is_filled = True):
        self.colour = colour
        self.is_filled = is_filled
        

    def __str__(self):
        return "Kolor: {}, wypełnione: {}".format(self.colour, 'tak' if self.is_filled else 'nie')
    def __repr__(self):
        values = ', '.join(('{} = {!r}'.format(k, v)
                            for k, v in self.__dict__.items()))
        return "{} ({})".format(self.__class__.__name__, values)

class Circle(Figure):
    def __init__(self, radius = 5, colour = True, is_filled = True):
        super().__init__(colour, is_filled)
        self.radius = radius


    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if isinstance(new_radius, Real) and new_radius>0:
            self._radius = new_radius
        else:
            print("Podano złą wartość (<0?), ustawiono na 1")
            self._radius = 1

    @property
    def area(self):
        return math.ceil(math.pi * self.radius * self.radius)
        #zaokrąglanie do liczy całkowitej
    @property
    def perimeter(self):
        return math.ceil(2 * math.pi * self.radius)
    @property
    def diameter(self):
        return 2*self.radius

    def __str__(self):
        return "Obiekt {},\n kolor: {}, wypełnione: {}, promień: {}\n Pole: {}, Obwód: {}".format(
            self.__class__.__name__, self.colour ,'tak' if self.is_filled else 'nie', self.radius, self.area, self.perimeter)

    def __repr__(self):
        values = ", ".join(('{}: {!r}'.format(k, v)
                            for k, v in self.__dict__.items()))
        return "{} ({})".format(self.__class__.__name__, values)
    
class Rectangle(Figure):
    def __init__(self, width = 10, height = 10, colour = True, is_filled = True):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, new_width):
        if isinstance(new_width, Real) and new_width>0:
            self._width = new_width
        else:
            print("Podano złą liczbę(<0?). Ustawiono na 1.")
            self._width = 1

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, new_height):
        if isinstance(new_height, Real) and new_height>0:
            self._height = new_height
        else:
            print("Podano złą liczbę(<0?). Ustawiono na 1.")
            self._height = 1

    @property
    def area(self):
        return self.width * self.height
    @property
    def perimeter(self):
        return (2*self.width)+(2*self.height)
    @property
    def diagonal(self):
        return math.sqrt((self.width*self.width)+(self.height*self.height))

    def __repr__(self):
        values = ", ".join(('{}: {!r}'.format(k, v)
                            for k, v in self.__dict__.items()))
        return "{} ({})".format(self.__class__.__name__, values)
    def __str__(self):
        return "Obiekt {},\n kolor: {}, wypełnione: {}, szerokość: {}, wysokość: {}\n Pole: {}, Obwód: {}, przekątna {}".format(
            self.__class__.__name__, self.colour ,'tak' if self.is_filled else 'nie', self.width, self.height, self.area, self.perimeter, self.diagonal)

                           
        
    
        
            
    
