import math

class Fraction:
    def __init__(self, num: int, denom: int):
        if denom == 0:
            raise ZeroDivisionError("You can't divide by 0.")
        elif type(num) != int or type(denom) != int:
            raise TypeError("Numerator and denominator must be integers.")
        else:
            self.num = num
            self.denom = denom
            gcd = math.gcd(self.num, self.denom)
            self.num //= gcd
            self.denom //= gcd
            if (self.num < 0 and self.denom < 0) or (self.num > 0 and self.denom < 0):
                self.num *= -1
                self.denom *= -1

    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        elif self.denom == -1:
            self.num *= -1
            return str(self.num)
        elif self.num == 0:
            return "0"
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        new_num = self.num * other.denom + other.num*self.denom
        new_denom = self.denom * other.denom
        new_fraction = Fraction(new_num,new_denom)
        return new_fraction

    def __sub__(self,other):
        new_num = self.num * other.denom - other.num * self.denom
        new_denom = self.denom * other.denom
        new_fraction = Fraction(new_num, new_denom)
        return new_fraction

    def __mul__(self, other):
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        new_fraction = Fraction(new_num, new_denom)
        return new_fraction

    def __truediv__(self, other):
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        new_fraction = Fraction(new_num, new_denom)
        return new_fraction

    def __lt__(self, other):
        if self.num/self.denom < other.num/other.denom:
            return True
        else:
            return False

    """def __gt__(self, other):
        if self.num/self.denom > other.num/other.denom:
            return True
        else:
            return False"""

    def __le__(self, other):
        if self.num/self.denom <= other.num/other.denom:
            return True
        else:
            return False

    """def __ge__(self, other):
        if self.num/self.denom >= other.num/other.denom:
            return True
        else:
            return False"""

    def __eq__(self,other):
        if self.num/self.denom == other.num/other.denom:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.num/self.denom != other.num/other.denom:
            return True
        else:
            return False

    def get_num(self):
        return self.num

    def get_den(self):
        return self.denom


f = Fraction(2,1)
f1 = Fraction(-12,8)
f > 0/6