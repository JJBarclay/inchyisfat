import turtle
import random

class Shape:
    def __init__(self,x=0,y=0,fill_color = "",filled = False):
        self.x = x
        self.y = y
        self.fill_color = fill_color
        self.filled = filled

    def setFillColor(self,new_color):
        self.fill_color = new_color
        print(self.fill_color)

    def setFilled(self,boolean):
        self.filled = boolean
        return(self.filled)

    def isFilled(self):
        return(self.filled)

class Circle(Shape):
    def __init__(self,x=0,y=0,radius=1,fill_color = "",filled = False):
        super().__init__(x,y,fill_color,filled)
        self.radius = radius

    def status(self):
        print('radius = ' + str(self.radius))
        print('x = ' + str(self.x))
        print('y = ' + str(self.y))
        print('fill color = ' + str(self.fill_color))
        print('Filled? = ' + str(self.filled))

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        if self.filled == True or 'True':
            turtle.begin_fill()
            turtle.fillcolor(self.fill_color)
            turtle.circle(self.radius)

            turtle.end_fill()
        if self.filled == False or 'False':
            turtle.circle(self.radius)

class Display(Circle):
    def __init__(self):
        self.t = turtle.Turtle()
        self.elements = []
        self.screen = turtle.getscreen()
        self.t.hideturtle()
        self.t.speed(0)
        self.screen.delay(0)
        self.screen.onclick(self.mouseEvent)

    def mouseEvent(self,x,y):
        c = Circle(x,y,random.randint(10,100))
        c.setFilled(True)
        c.setFillColor(random.choice(['blue', 'red', 'yellow', 'green']))
        c.draw(self.t)

def main():
    Display()

if __name__ == '__main__':
    main()
