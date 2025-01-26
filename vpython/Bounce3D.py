from vpython import *
from time import *

#Room variable 
mRadius=.5
wallThickness=.1
roomWidth=12
roomDepth=20
roomHeight=2

#Room 
#vector(x,y,z)
floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)

#Marble
marble=sphere(radius=mRadius,color=color.red)

#initial Position of Marble
xPos=0
yPos=0
zPos=0

#change of position
deltaX=.1
deltaY=.1
deltaZ=.1

while True:
    rate(25)

    xPos=xPos+deltaX  # xPos changing
    yPos=yPos+deltaY  # yPos changing
    zPos=zPos+deltaZ  # zPos changing
 
    # xPos changing at edge
    Xrme=xPos+mRadius 
    Xlme=xPos-mRadius

    # yPos changing at edge
    Ycme=yPos+mRadius
    Ytme=yPos-mRadius

    # zPos changing at edge
    Zbme=zPos-mRadius
    Zfrme=zPos+mRadius

    #limit of x axis 
    Rwe=roomWidth/2-wallThickness/2
    Lwe=-roomWidth/2+wallThickness/2

    #limit of y axis
    Cwe=roomHeight/2-wallThickness/2
    Twe=-roomHeight/2+wallThickness/2

    #limit of z axis
    Bwe=-roomDepth/2+wallThickness/2
    Frwe=roomDepth/2-wallThickness/2

    # change direction base on postion- if across limit value change direction
    if (Xrme>=Rwe or Xlme<Lwe): 
        deltaX=deltaX*(-1)
    if (Ycme>=Cwe or Ytme<Twe):
        deltaY=deltaY*(-1)
    if (Zfrme>=Frwe or Zbme<Bwe):
        deltaZ=deltaZ*(-1)

    # visualize marble movement based on x,y,z-position
    marble.pos=vector(xPos,yPos,zPos)