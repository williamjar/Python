import turtle

class Drawer:

    def __init__(self, function, xrange):
        self.function = function
        self.xrange = xrange



    def drawGraph(self):

        graphpointer = turtle.Turtle()
        x = 0
        while(x <= self.xrange):
            for y in self.function:
                graphpointer.goto(x, y)
                x += 10

        turtle.done()





func = [1,2,6,7,9,10,18,19,100]
graph = Drawer(func, 50)
graph.drawGraph()