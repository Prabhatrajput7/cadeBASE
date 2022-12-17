class ColorRadius:
    colors = ('red','green','blue')
    def __init__(self,color,radius):
        self._c = color
        self._r = radius

    def get_rad(self):
        return self._r
    
    def set_rad(self,r):
        if isinstance(r,int) and r>0:
            self._r = r
        else:
            print('Not a valid radius')

    r = property(get_rad,set_rad)

cr = ColorRadius('blue',5)
print(cr.r)
cr.r += 10
print(cr.r)