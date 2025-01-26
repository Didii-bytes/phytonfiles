class Rectangle:
    def __init__(self,c,l,w):
        self.color=c
        self.length=l
        self.width=w
    def area(self):
        self.area=self.length*self.width
        return self.area
    def perimeter(self):
        self.perimeter=2*self.length+2*self.width
        return self.perimeter
    def diagonal(self):
        self.diag=(self.width**2+self.length**2)**(1/2)
        return self.diag
    def volume(self,h):
        self.height=h
        self.volume=self.height*self.area
        return self.volume

myRect1=Rectangle('red',1,2)
myRect2=Rectangle('blue',4,2)
print('')
print('1st rectangle Color:',myRect1.color)
print('Length:',myRect1.length)
print('Area:',myRect1.area())
print('perimeter:',myRect1.perimeter())
print('Hypotaneus:',round(myRect1.diagonal(),2))
myVol=myRect1.volume(5)
print('Volume:',myVol)
print('')
print('2nd rectangle Color:',myRect2.color)
print('Length:',myRect2.length)
print('Area:',myRect2.area())
print('perimeter:',myRect2.perimeter())
print('hypotaneus:',round(myRect2.diagonal(),2))
myVol=myRect2.volume(6)
print('Volume:',myVol)