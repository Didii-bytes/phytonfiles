from vpython import *
from time import *

#Room variable 
mRadius=.75
wallThickness=.1
roomWidth=10
roomDepth=5
roomHeigth=10

#Room 
#vector(x,y,z)
floor=box(pos=vector(0,-roomHeigth/2,0),color=color.white,size=vector(roomWidth,wallThickness,roomDepth))
ceiling=box(pos=vector(0,roomHeigth/2,0),color=color.white,size=vector(roomWidth,wallThickness,roomDepth))
backWall=box(pos=vector(0,0,-roomDepth/2),color=color.white,size=vector(roomWidth,roomHeigth,wallThickness))
rightWall=box(pos=vector(roomWidth/2,0,0),color=color.white,size=vector(wallThickness,roomHeigth,roomDepth))
leftWall=box(pos=vector(-roomWidth/2,0,0),color=color.white,size=vector(wallThickness,roomHeigth,roomDepth))

#Marble
marble=sphere(color=color.red,radius=mRadius)

#initial Position of Marble
deltaX=.1
xPos=0

#Loop to run Marble move
while True:
    rate(10)
    xPos=xPos+deltaX
    if xPos>(roomWidth/2) or (xPos<-roomWidth/2):
        deltaX=deltaX*(-1)
    marble.pos=vector(xPos,0,0)