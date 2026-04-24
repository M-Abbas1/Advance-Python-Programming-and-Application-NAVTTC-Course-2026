class Fraction:
    def __init__(self, nom, den):
        self.__nom = nom
        self.__den = den

    def __str__(self):
        return f"{self.__nom}/{self.__den}"      
    

    def __add__(self, other):
        res_den = self.__den * other.__den
        res_nom = (self.__nom * other.__den) + (self.__den * other.__nom)
        return f"{res_nom}/{res_den}"
    
    def __sub__(self, other):                                    
        res_den = self.__den * other.__den                             
        res_nom = (self.__nom * other.__den) - (other.__nom * self.__den)
        return f"{res_nom}/{res_den}"
    

    def __mul__(self, other):                             ## 20/2 * 10/4  =  200/8
        res_nom = self.__nom * other.__nom
        res_den = self.__den * other.__den
        return f"{res_nom}/{res_den}"
    
    def __truediv__(self, other):
        res_nom = self.__nom * other.__den
        res_den = self.__den * other.__nom
        return f"{res_nom}/{res_den}"

    @property
    def nom(self):
        return self.__nom
    
    @property
    def den(self):
        return self.__den
    

    @nom.setter
    def nom(self, val):
        if isinstance(val, int):
            self.__nom = val
        else:
            print("Nomirator must be an integer")

    
    @den.setter
    def den(self, val):
        if val == 0:
            print("Denominator must not be zero ")
        elif isinstance(val, int): 
            self.__den = val
        else:
            print("Denominator must be an integer")
    

    def simplify(self):
        if self.__nom <= self.__den:
            sd = self.__nom
        else:
            sd = self.__den

        for i in range(sd, 1, -1):
            if self.__nom%i == 0  and self.__den%i == 0:
                res_nom = self.__nom//i
                res_den = self.__den//i
                return Fraction(res_nom, res_den)
            
        return self
            

    def simplified(self):
        if self.__nom <= self.__den:
            sd = self.__nom
        else:
            sd = self.__den

        for i in range(sd, 1, -1):
            if self.__nom%i == 0  and self.__den%i == 0:
                self.nom = self.__nom//i
                self.den = self.__den//i
            

    
    def __eq__(self, other):
        sf = self.simplify()
        ss = other.simplify()
        return sf.nom == ss.nom  and sf.den == ss.den