from complex import Complex
from mandelbrot import Mandelbrot
import turtle

class Display:
    def __init__(self):
         turtle.setup(height=300, width=300)
         self.t = turtle.Turtle()
         self.t.bgcolor('grey')
         self.__s = turtle.Screen()
<<<<<<< HEAD
         self.__s.screensize(300,300)
         self._screen = turtle.getscreen()
         self.t.ht()
         self.t.penup()
         self.t.speed(0)
         self.__s.tracer(100,0)
         for screen_y in range(-150, 151):
            for screen_x in range(-150, 151):
                self.t.goto(screen_x,screen_y)
                real = screen_x/75.0
                imaginary = screen_y/75.0
                point = Complex(real,imaginary)
=======
         turtle.hideturtle()
         self._screen = turtle.getscreen()
         self.t.ht()
         self.t.penup()
         
         self.t.speed(0)
         self.__s.tracer(500,0)
         for screen_y in range(-150, 150):
            for screen_x in range(-150, 150):
                self.t.goto(screen_x,screen_y)
                r = screen_x * 2.0 / 150 
                i = screen_y * 2.0 / 150  
                point = Complex(r,i)
                #print(point)
>>>>>>> e2cdade0ab17ea42bee01609745a43d02f8e4ed6
                mandel_val = Mandelbrot(point)
                color = mandel_val.get_color()
                self.t.pendown()
                self.t.pencolor(color)
                self.t.forward(1)
                self.t.penup()
         self.__screen.onlick(self.__mouseEvent)

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

d = Display()

def __main__():
    Display()

if __name__ == '__main__':
        main()
