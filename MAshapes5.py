from graphics import*

shapesWin = GraphWin("Shapes",500,500)
shapesWin.setCoords(0,0,500,500)

bTri = Polygon(Point(10,50),Point(50,100), Point(150,100))
bTri.setFill(color_rgb(30,30,230))
bTri.draw(shapesWin)


rSquare = Polygon(Point(50,450),Point(150,450),Point(150,350),Point(50,350))
rSquare.setFill(color_rgb(178,34,34))               
rSquare.draw(shapesWin)
