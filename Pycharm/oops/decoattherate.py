class ColorRadius:
    colors = ('red', 'green', 'blue')

    def __init__(self, color, radius,dia):
        self._c = color
        self._radius = radius
        self._dia = dia

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if isinstance(r, int) and r > 0:
            self._radius = r
        else:
            print('Not a valid radius')


cr = ColorRadius('blue', 5,15)
print(cr.radius)
cr.radius=10
print(cr.radius)
print(cr.__dict__)