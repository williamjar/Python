import turtle
import math


def generatePoints(intervals, radius):
    points = []
    for x in range(intervals):
        points.append(
            [math.sin(x * (2 * math.pi) / intervals) * radius, math.cos(x * (2 * math.pi) / intervals) * radius])
    return points


def multiplication(points, multiplier):
    sum = []
    for x in range(0, len(points)):
        sum.append(x * multiplier)
    return sum


def multiplicationGenerator(points, multiplier):
    for x in range(0, len(points)):
        yield x * multiplier


def drawGenerator(pen, points, sum):
    pen.circle(radius)
    for x, y in zip(points, sum):
        pen.penup()
        pen.goto(x)
        pen.pendown()
        pen.goto(points[y % intervals])

def draw(pen, points, sumArr):
    pen.circle(radius)
    for x in range(0, len(points)):
        pen.penup()
        pen.goto(points[x])
        pen.pendown()
        pen.goto(points[sumArr[x] % intervals])







if __name__ == "__main__": 

    turtle.setup(500, 500)  # screen size
    pen = turtle.Turtle()  # creating an object
    pen.speed(0)  # max speed
    pen.penup()
    pen.goto(0, -200)  # Offset to have origo in the middle of the screen
    pen.pendown()

    # adjust these variables to be used in the functions
    intervals = 150
    radius = 200
    multiplier = 100
    positions = generatePoints(intervals, radius)



    #task 2
    #sumGen = multiplicationGenerator(positions, multiplier)
    #drawGenerator(pen, positions, sumGen)

    #task 1
    sum = multiplication(positions, multiplier)
    draw(pen, positions, sum)

    

    turtle.done() 
