class Mandelbrot:
    def __init__(self, starting_value, limit = 50, colormap = ['white','pink','red','orange','yellow','green','turquoise','blue', 'indigo', 'violet', 'black'], cardinality = 0):
        #starting_value.spy("at the begginning of mand init")
        self.__start = starting_value
        self.__limit = limit
        self.__colormap = colormap
        self.__cardinality = cardinality
        z = self.__start.dupe()
        c = self.__start.dupe()
        lim_val = self.__limit
        #starting_value.spy("before the loop")
        for i in range(self.__limit):
            #starting_value.spy("*** at the top of the loop with i={i}".format(**vars()))
            #starting_value.spy("before if")
            if abs(z) > 2:
                self.__cardinality = i
                break
            else:
                z = z*z + c
            #starting_value.spy("after if if")
            self.__cardinality = self.__limit
        #starting_value.spy("at the end of mand init")

    def __repr__(self):
        print(self.__start)
        print(self.__limit)
        print(self.__cardinality)

    def get_color(self):
        c = self.__cardinality
        color = self.__colormap
        lim = self.__limit
        if 0 <= c <= (.1*lim):
            return(color[0])
        if (.1*lim) < c <= (.2*lim):
            return(color[1])
        if (.2*lim) < c <= (.3*lim):
            return(color[2])
        if (.3*lim) < c <= (.4*lim):
            return(color[3])
        if (.4*lim) < c <= (.5*lim):
            return(color[4])
        if (.5*lim) < c <= (.6*lim):
            return(color[5])
        if (.6*lim) < c <= (.7*lim):
            return(color[6])
        if (.7*lim) < c <= (.8*lim):
            return(color[7])
        if (.8*lim) < c <= (.9*lim):
            return(color[8])
        if (.9*lim) < c < lim:
            return(color[9])
        if c >= lim:
            return(color[10])
