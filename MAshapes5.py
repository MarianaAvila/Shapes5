from graphics import*

xWindowSize = 500
yWindowSize = 500 

shapesWin = GraphWin("Shapes",500,500)
shapesWin.setCoords(0,0,500,500)

bTri = Polygon(Point(10,50),Point(50,100), Point(150,100))
bTri.setFill(color_rgb(30,30,230))
bTri.draw(shapesWin)


rSquare = Rectangle(Point(50,350),Point(150,450))
rSquare.setFill(color_rgb(178,34,34))               
rSquare.draw(shapesWin)

oCircle= Circle(Point(440,440),50)
oCircle.setFill(color_rgb(255,69,0))
oCircle.draw(shapesWin)

gPentagon = Polygon(Point(370,80),Point(370,130),Point(395,180),Point(420,130),Point(420,80))
gPentagon.setFill(color_rgb(50,205,50)) 
gPentagon.draw(shapesWin)

bDiamond = Polygon(Point(xWindowSize/2,yWindowSize/2+50),Point(xWindowSize/2 + 50,yWindowSize/2),Point(xWindowSize/2, yWindowSize/2 -50),Point(xWindowSize/2 -50,yWindowSize/2))
bDiamond.setFill(color_rgb(135,206,250))
bDiamond.draw(shapesWin)
    
