from complex import Complex
from mandelbrot import Mandelbrot
import turtle

def GetPos(x_location, y_location):
    return([x_location, y_location])

class Display:
    def __init__(self):
         turtle.bgcolor('grey')
         turtle.hideturtle()
         turtle.setup(300,300)
         self.t = turtle.Turtle()
         self.__s = turtle.Screen()
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
                mandel_val = Mandelbrot(point)
                color = mandel_val.get_color()
                self.t.pendown()
                self.t.pencolor(color)
                self.t.forward(1)
                self.t.penup()
         Zoom = 1
         [click_x, click_y] = self.t.onclick(GetPos)
         self.__screen.onlick(self.click())

    def click(click_x,click_y,Zoom):
        self.__Zoom = Zoom
        self.__X = click_x
        self.__Y = click_y
        if self.t.pos() == (151, 151):
            zoom(self.__X, self.__Y,Zoom )

    def zoom(click_x, click_y, Zoom):
        self.__zoom = Zoom
        self.__clickX = click_x
        self.__clickY = click_y
        if self.__zoom ==1:
            multiplier = 2*self.__zoom
        xShift = click_x/(75*multiplier)#new origin x
        yShift = click_y/(75*multiplier)#new origin y
        divisor = (75 * multiplier)
        draw(divisor, multiplier )

    def draw(divisor, multiplier):
        self.__multiplier = multiplier
        self.__divisor = divisor
        for screen_y in range(-150, 151):
           for screen_x in range(-150, 151):
               self.t.goto(screen_x,screen_y)
               real = screen_x/self.__divisor
               imaginary = screen_y/self.__divisor
               point = Complex(real,imaginary)
               mandel_val = Mandelbrot(point)
               color = mandel_val.get_color()
               self.t.pendown()
               self.t.pencolor(color)
               self.t.forward(1)
               self.t.penup()
        self.__multiplier = 2*self.__multiplier
        return(self.__multiplier)

d = Display()

def __main__():
    Display()

if __name__ == '__main__':
        main()
