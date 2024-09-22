#TurtleGraphics.py
#Name: Lukas Gibbs
#Date: 9/22/24
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides) : 
        bob. forward(50)
        bob.right(360/sides)
        
        
def fillCorner(alice, corner) :
    #draw big square
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 3:
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 4:
        alice.forward(50)
        alice.up()
        alice.right(90)
        alice.forward(50)
        alice.down()
        alice.left(90)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        
def squaresInSquares(alex, num):
    alex.up()
    alex.left(180)
    alex.forward(50)
    alex.right(90)
    alex.forward(50)
    alex.down()
    alex.right(90)
    drawSquare(alex, 100)

    if num == 2:
        alex.up()
        alex.left(180)
        alex.forward(10)
        alex.right(90)
        alex.forward(10)
        alex.down()
        alex.right(90)
        drawSquare(alex, 120)
    if num == 3:
        alex.up()
        alex.left(180)
        alex.forward(10)
        alex.right(90)
        alex.forward(10)
        alex.down()
        alex.right(90)
        drawSquare(alex, 120)
        alex.up()
        alex.left(180)
        alex.forward(10)
        alex.right(90)
        alex.forward(10)
        alex.down()
        alex.right(90)
        drawSquare(alex, 140)
    if num == 4:
        alex.up()
        alex.left(180)
        alex.forward(10)
        alex.right(90)
        alex.forward(10)
        alex.down()
        alex.right(90)
        drawSquare(alex, 120)
        alex.up()
        alex.left(180)
        alex.forward(10)
        alex.right(90)
        alex.forward(10)
        alex.down()
        alex.right(90)
        drawSquare(alex, 140)
        alex.up()
        alex.left(180)
        alex.forward(10)
        alex.right(90)
        alex.forward(10)
        alex.down()
        alex.right(90)
        drawSquare(alex, 160)
    if num == 5:
        alex.up()
        alex.left(180)
        alex.forward(10)
        alex.right(90)
        alex.forward(10)
        alex.down()
        alex.right(90)
        drawSquare(alex, 120)
        alex.up()
        alex.left(180)
        alex.forward(10)
        alex.right(90)
        alex.forward(10)
        alex.down()
        alex.right(90)
        drawSquare(alex, 140)
        alex.up()
        alex.left(180)
        alex.forward(10)
        alex.right(90)
        alex.forward(10)
        alex.down()
        alex.right(90)
        drawSquare(alex, 160)
        alex.up()
        alex.left(180)
        alex.forward(10)
        alex.right(90)
        alex.forward(10)
        alex.down()
        alex.right(90)
        drawSquare(alex, 180)
def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 3)
    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
