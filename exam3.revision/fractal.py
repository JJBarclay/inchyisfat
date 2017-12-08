from complex import Complex
from mandelbrot import Mandelbrot
import turtle

class Display:
    def __init__(self):
         self.t = turtle.Turtle()
         self.__s = turtle.Screen()
         self._screen = turtle.getscreen()
         self.t.ht()
         self.t.penup()
         self.__s.screensize(200,200)
         self.t.speed(0)
         self.__s.tracer(100,0)
         for y in range(-200, 201):
            for x in range(-200, 201):
                self.t.goto(x,y)
                x = x/100
                y = y/100
                point = Complex(x,y)
                print(point)
                mandel_val = Mandelbrot(point)
                color = mandel_val.get_color()
                print('Color at (' + str(x) + ',' + str(y) + ') is ' + str(color))
                self.t.pendown()
                self.t.pencolor(color)
                self.t.forward(1)
                self.t.penup()
         #self.__screen.onlick(self.__mouseEvent)

def test():
    turtle.tracer(1000, 0)
    for x in range(-200, 200):
        for y in range(-200, 200):
            turtle.penup()
            turtle.goto(x,y)
            turtle.pencolor('blue')
            turtle.pendown()
            turtle.forward(.5)
            turtle.penup()
