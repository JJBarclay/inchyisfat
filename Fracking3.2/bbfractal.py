from complex import Complex
from mandelbrot import Mandelbrot
import turtle


class Display:

    def __init__(self):

         # set this to 1 before turning in.
         # set it to 4 to go real fast
         self.pixel_step = 4 # increase to skip pixels; draw faster during testing
         

         turtle.bgcolor('grey')
         turtle.hideturtle()

         # pixels_max_x and y define the extent of our screen from origin
         self.pixels_max_x = int(150) # extends from -150 to 150 (300 pixels)
         self.pixels_max_y = int(150) # "

         # our "aperature" what we call the section of the mandelbrot
         # image plane displayed on the screen.  Our aperature has four
         # properties which we use to calculate the mapping of
         #  screen x/y location to mandelbrot r/i location during:
         #     1) screen update
         #     2) click callback

         # define properties for aperature
         self.r_offset = 0  # offset in real axis where our screen origin is 
         self.i_offset = 0  # offset in imag axis where our screen origin is


         self.r_extent = 2  # distance from r_offset that corresponds to screen edge
         self.i_extent = 2  # distance from r_offset that corresponds to screen edge

         # we start with aperature of extent 2 and offset of zero, showing
         # mandelbrot centered at origin from -2 to +2 in real/imag plane

         # scale factor by which we reduce the extent on clicking
         #  - reduced extent means the screen covers a smaller portion
         #    of the mandelbrot plane, thus zooming in
         self.zoom_scale = 2 # 2x zoom per click

         self.still_drawing = 0 # set to 1 while drawing.


         # take care of initializing our display
         turtle.setup(2*self.pixels_max_x,2*self.pixels_max_y)
         self.t = turtle.Turtle()
         self.__s = turtle.Screen()
         self.__s.screensize(300,300)
         self._screen = turtle.getscreen()
         self.t.ht()
         self.t.penup()
         self.t.speed(0)
         self.__s.tracer(100,0)





         # callback for turtle onclick
         #   turtle onclick calls callback with x and y as arguments
         #   this callback then calls the click object method
         onclick_callback = lambda x,y: self.click(x,y)

         # register our callback with a click event 
         self.__s.onclick(onclick_callback)


         # draw mandelbrot initially
         self.update_display()

         # kick off event loop for turtle so it waits for clicks and
         #  does not just exit immediately.
         turtle.mainloop()
         


    # method: screen_coords_to_mandelbrot_coords
    #         ==================================
    #         in: screen_x (int), screen_y (int) -- screen coordinates.
    #         out: r (float), i (float)          -- mandelbrot coordinates
    
    #   this method maps an x/y coordinate on the screen to a r/i coordinate
    #      in the mandelbrot plane conforming to our current aperature

    #
    # the  properties of the aperature are
    #   r_extent, which starts at 2 initially
    #   i_extent, which starts at 2 initially
    #   r_offset, which starts at 0 initially
    #   i_offset, which starts at 0 initially
    #  
    # the mandelbrot image at the screen origin corresponds to
    #    the mandelbrot plane at r=r_offset, i=i_offset
    # the right extent of the screen (screen_x=150) corresponds to
    #    the mandelbrot plane at r_offset + r_extent 
    # the left extent of the screen (screen_x=-150) corresponds to
    #    the mandelbrot plane at r_offset - r_extent 
    # the top extent of the screen (screen_y=150) corresponds to
    #    the mandelbrot plane at i_offset + i_extent 
    # the bottom extent of the screen (screen_y=-150) corresponds to
    #    the mandelbrot plane at i_offset - i_extent 
    def screen_coords_to_mandelbrot_coords(self, screen_x, screen_y):
        # calculate real position
        r = screen_x / ( self.pixels_max_x / self.r_extent ) + self.r_offset
        # calculate imag position
        i = screen_y / ( self.pixels_max_y / self.i_extent ) + self.i_offset
        return(r,i)

    # method: update_display
    #         ==============
    #         draw mandelbrot image on screen.
    def update_display(self):
        self.still_drawing = 1 # disable click callback while drawing
        for screen_y in range(-1 * self.pixels_max_y,
                              self.pixels_max_y,
                              self.pixel_step):
            for screen_x in range(-1 * self.pixels_max_x,
                                  self.pixels_max_x,
                                  self.pixel_step):
                self.t.goto(screen_x,screen_y)

                # call our method to translate screen coordinates
                #    to mandelbrot plane coordinates.
                real, imaginary = self.screen_coords_to_mandelbrot_coords(screen_x, screen_y)
                #real = screen_x/75.0
                #imaginary = screen_y/75.0
                point = Complex(real,imaginary)
                mandel_val = Mandelbrot(point)
                color = mandel_val.get_color()
                self.t.pendown()
                self.t.pencolor(color)
                self.t.forward(1)
                self.t.penup()
        self.still_drawing = 0 # re-enable click callback 

    # method: click
    #         =====
    #     called when user clicks on mandelbrot image
    #     in: click_x(int), click_y(int) -- screen coords where user clicked
    #     out: none
    #
    #     we do four things in our callback.
    #          1) calculate real and imag coords where user clicked
    #          2) recenter image at these coordinates
    #          3) zoom in
    #          4) redraw our mandelbrot
    #
    def click(self, click_x, click_y):
        if self.still_drawing == 1:
            print("Sorry, we are still drawing.  Wait till done.")
            return

        # 1) calculate real and imag coords where user clicked
        if abs(click_x) > self.pixels_max_x or abs(click_y) > self.pixels_max_y:
            print("You clicked outside the allowable image.  Ignoring.")
            return
        print("BB> click called. with {click_x}, {click_y}".format(**vars()))
        click_r, click_i = self.screen_coords_to_mandelbrot_coords(click_x, click_y)
        print("BB> click at r={click_r}, i={click_i}".format(**vars()))

        # 2) recenter image at clicked coordinates
        self.r_offset = click_r
        self.i_offset = click_i
        
        # 3) zoom in
        self.r_extent /= self.zoom_scale
        self.i_extent /= self.zoom_scale

        # 4) redraw our mandelbrot
        self.update_display()


def main():
    Display()

if __name__ == '__main__':
        main()
