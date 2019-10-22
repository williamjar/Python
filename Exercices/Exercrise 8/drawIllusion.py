import math
import turtle

def drawingMachine(bob,xPos, yPos,squareSize,squareColor,gridColor,circleColor):
    bob.penup()
    bob.color(gridColor)
    bob.goto(xPos,yPos)
    bob.fillcolor(squareColor)
    bob.begin_fill()
    bob.pendown()
    for x in range(4):
        bob.right(90)
        bob.forward(squareSize)

    bob.end_fill()

    for x in range(4):
        bob.color(circleColor)
        bob.fillcolor(circleColor)
        bob.dot(8)
        bob.penup()
        bob.right(90)
        bob.forward(squareSize)
        bob.pendown()

'''This function draws a rectangle and draws dots in the corner of the rectangles. It does draw dots for each rectangle.'''

def drawIllusion(gridColor, squareColor, circleColor, imgSize, squareSize, gridWidth):
    turtle.setup(imgSize, imgSize)
    bob = turtle.Turtle()   # creating a turtle
    bob.pensize(gridWidth)
    bob.speed(0)            # max speed
    for x in range(math.ceil(imgSize/squareSize)):     # deciding how many squares to draw horizontally
        for y in range(math.ceil(imgSize/squareSize)): # deciding how many squares to draw vertically
            drawingMachine(bob,(-imgSize/2)+squareSize+(y*squareSize),imgSize/2-(x*squareSize),squareSize,squareColor, gridColor, circleColor)

    turtle.done() # keeping the display after drawing is done

'''Function that sets up the so the drawing machine doesn't go out of bounds'''


if __name__ == "__main__":
    ultramarine = "#003E52"
    drawIllusion("white", ultramarine,"light grey",800,100,6)