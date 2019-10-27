import random
import turtle


class Die:
    colorDots = "black"
    colorDie = "white"
    value = ''

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def getpos(self):
        return 'x = {} y = {}'.format(self.x, self.y)

    '''
    function returning the position of the dice

    takes:
    self

    yields:
    value of the x and y coordinates of the dice
    '''

    def getvalue(self):
        return self.value

    def setcolor(self, colorDots, colorDie):
        self.colorDots = colorDots
        self.colorDie = colorDie

    '''
    function for setting colors

    takes:
    self, colorDots, colorDie
    
    yields:
    sets class variables for the dice colors
    '''

    def roll(self):
        self.value = random.randint(1, 6)

    '''
    function that gives a random number between and including 1 and 6. 

    takes:
    self

    yields:
    random value between and including 1 and 6
    '''

    def drawdie(self):
        pen = turtle.Turtle()
        screen = turtle.Screen()

        pen.hideturtle()
        pen.speed(0)
        pen.color(self.colorDie)
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()

        # drawing the die body
        pen.begin_fill()
        for i in range(4):
            pen.forward(self.size)
            pen.left(90)
        pen.end_fill()

        pen.color(self.colorDots)
        pen.penup()
        pen.forward(self.size / 2)
        pen.left(90)
        pen.forward(self.size / 2)
        pen.left(90)

        if self.value == 1:
            pen.dot(self.size / 5)

        pen.penup()
        if self.value == 2:
            pen.forward(self.size / 4)
            pen.right(90)
            pen.forward(self.size / 4)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 2)
            pen.right(90)
            pen.forward(self.size / 2)
            pen.dot(self.size / 5)

        if self.value == 3:
            pen.forward(self.size / 4)
            pen.right(90)
            pen.forward(self.size / 4)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 4)
            pen.right(90)
            pen.forward(self.size / 4)
            pen.dot(self.size / 5)

            pen.left(90)
            pen.forward(self.size / 4)
            pen.right(90)
            pen.forward(self.size / 4)
            pen.dot(self.size / 5)

        if self.value == 4:
            pen.forward(self.size / 4)

            pen.right(90)
            pen.forward(self.size / 4)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 2)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 2)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 2)
            pen.dot(self.size / 5)

        if self.value == 5:
            pen.dot(self.size / 5)

            pen.left(90)
            pen.forward(self.size / 4)
            pen.right(90)
            pen.forward(self.size / 4)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 2)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 2)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 2)
            pen.dot(self.size / 5)

        if self.value == 6:
            pen.forward(self.size / 4)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 4)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 2)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 4)
            pen.dot(self.size / 5)

            pen.forward(self.size / 4)
            pen.dot(self.size / 5)

            pen.right(90)
            pen.forward(self.size / 2)
            pen.dot(self.size / 5)

        turtle.done()

    '''
    Function that draws the value, based on the value based on the roll. 
    This function could be it's own drawing class instead, to keep things tidy.
    This could also be tidied up by using a different drawing interface. 

    takes:
    self

    prints(graphics):
    dice with dots corresponding to self.value
    '''


# test

def main():
    die1 = Die(0, 0, 100)
    die1.setcolor("blue", "black")
    die1.roll()

    die1.drawdie()


if __name__ == "__main__":
    main()
