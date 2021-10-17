import math


class Fraction:
    """
    This is a class Fraction that creates fractions and defines simple actions between them.
    """
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
            if (self.num < 0 and self.denom < 0) or (self.num > 0 > self.denom):
                self.num *= -1
                self.denom *= -1

    def __str__(self):
        """
        string representation of the fraction
        """
        if self.denom == 1:
            return str(self.num)
        elif self.denom == -1:
            self.num *= -1
            return str(self.num)
        elif self.num == 0:
            return "0"
        return f"{self.num}/{self.denom}"

    def __add__(self, other):
        """
        summing fractions
        """
        new_num = self.num * other.denom + other.num*self.denom
        new_denom = self.denom * other.denom
        new_fraction = Fraction(new_num, new_denom)
        return new_fraction

    def __sub__(self, other):
        """
        subtracting fractions
        """
        new_num = self.num * other.denom - other.num * self.denom
        new_denom = self.denom * other.denom
        new_fraction = Fraction(new_num, new_denom)
        return new_fraction

    def __mul__(self, other):
        """
        multiplying fractions
        """
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        new_fraction = Fraction(new_num, new_denom)
        return new_fraction

    def __truediv__(self, other):
        """
        dividing fractions
        """
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        new_fraction = Fraction(new_num, new_denom)
        return new_fraction

    def __lt__(self, other):
        """
        comparing fractions if fraction is lower than another
        """
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
        """
        comparing if fraction is lower equal to another
        """
        if self.num/self.denom <= other.num/other.denom:
            return True
        else:
            return False

    """def __ge__(self, other):
        if self.num/self.denom >= other.num/other.denom:
            return True
        else:
            return False"""

    def __eq__(self, other):
        """
        comparing if fraction is equal to another
        """
        if self.num/self.denom == other.num/other.denom:
            return True
        else:
            return False

    def __ne__(self, other):
        """
        comparing if fraction is not equal to another
        """
        if self.num/self.denom != other.num/other.denom:
            return True
        else:
            return False

    def get_num(self):
        """
        numerator of the fraction
        """
        return self.num

    def get_den(self):
        """
        denominator of the fraction
        """
        return self.denom


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1+f2
print(f3)
