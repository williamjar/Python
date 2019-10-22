import turtle


def drawGrid(colorGrid, sizeSquare, sizeImage):
    turtle.setup(sizeImage, sizeImage)
    print("drawingRectangle")
    bob = turtle.Turtle()
    bob.color(colorGrid)
    bob.pensize(5)
    bob.penup()
    bob.setx(-sizeImage/2)
    bob.sety(sizeImage/2)
    while bob.position < sizeImage:
        bob.pendown()
        bob.fd(sizeImage)


def drawIllusion(colorGrid, colorSquare, colorCircles, sizeImage, sizeSquare, sizeCircle):


    drawGrid(colorGrid, sizeSquare, sizeImage)

    turtle.done()



def main():
    drawIllusion("red",2,3,400,5,6)


if __name__ == '__main__':
    main()