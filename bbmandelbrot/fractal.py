#!/usr/bin/python3

class Display:
    def __init__(self):
         self.t = turtle.Turtle()
         self.__s = turtle.Screen()
         self._screen = turtle.getscreen()
         self.t.ht()
         self.t.penup()
         self.__s.screensize(200,200)
         self.t.speed(0)
         self.__s.tracer(200,0)
         for x in range(-200, 200):
            for y in range(-200, 200):
                self.t.goto(x,y)
                x = x/100
                y = y/100
                point = Complex(x,y)
                mandel_val = Mandelbrot(point)
                color = mandel_val.get_color()
                self.t.pendown()
                self.t.pencolor(color)
                self.t.penup()
         #self.__screen.onlick(self.__mouseEvent)

from mandelbrot import Mandelbrot
from complex import Complex
def main():
    c = Complex(.4,0)
    c.spy()
    m = Mandelbrot(c)
    c.spy()
    color = m.get_color()
    c.spy()
    print("BB> for my input {c} m gives me {color}".format(**vars()))


main()
