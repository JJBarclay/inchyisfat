class Complex: #class Complex initiator
    def __init__(self, real = 0, imaginary = 0):
        self.__real = float(real)
        temp = self.__real
        #print("BB> in the initter we get self.__real = {temp}".format(**vars()))
        self.__imaginary = float(imaginary)

    def dupe(self):
        new = Complex(self.__real, self.__imaginary)
        return new

    def spy(self, message=''):
        temp = self.__real
        #print("BB> spy({message}):  self.__real = {temp}".format(**vars()))


    def __repr__(self): #makes it print out the complex number in the right form
        #print("BB> complex.repr called")
        rv = None
        temp = self.__real
        #print("BB> in the complex.repr we get self.__real = {temp}".format(**vars()))

        i = self.__imaginary
        r = self.__real
        #print("BB> complex.repr -- i got i={i} r={r}".format(**vars()))

        if self.__imaginary > 0:
            rv = str(self.__real) + ' + ' + str(self.__imaginary) + 'i'
        elif self.__imaginary < 0:
            rv = str(self.__real) + ' - ' +  str(self.__imaginary) + 'i'
        else:
            rv = str(self.__real)
            
        #print("BB> complex.repr about to return {rv}".format(**vars()))
        return rv

    def new_real(self, newReal): #change real number and display change
        self.__real = newReal
        print("Real number value is now " + str(newReal))

    def new_imaginary(self, newImaginary): #change imaginary number and display change
        self.__imaginary = newImaginary
        print('Imaginary number value is now ' + str(newImaginary) + 'i')

    def __add__(self, value):
        added__real = self.__real + value.__real
        added__imaginary = self.__imaginary + value.__imaginary
        self.__real = added__real
        self.__imaginary = added__imaginary
        return(self)

    def __mul__(self, value):
        mul_real = (self.__real * value.__real) - (self.__imaginary * value.__imaginary)
        mul_imaginary = (self.__real * value.__imaginary) + (self.__imaginary * value.__real)
        self.__real = mul_real
        self.__imaginary = mul_imaginary
        return(self)

    def __abs__(self):
        distance = ((self.__real)**2 + (self.__imaginary)**2)**.5
#        print("BB> __abs__ called")
        return(distance)
