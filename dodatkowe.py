import math


class Fraction:

    type = "simple"

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        self.if_fraction()
        if self.denom == 0:
            raise ZeroDivisionError("You can't divide by 0.")
        else:
            self.if_float()
            self.reduce()
            self.customize()

    def reduce(self):
        gcd = math.gcd(self.num, self.denom)
        self.num //= gcd
        self.denom //= gcd

    def customize(self):
        if (self.num < 0 and self.denom < 0) or (self.num > 0 > self.denom):
            self.num *= -1
            self.denom *= -1

    def if_fraction(self):
        if isinstance(self.num, Fraction):
            self.num = self.num.num / self.num.denom
        if isinstance(self.denom, Fraction):
            self.denom = self.denom.num / self.denom.denom

    def if_float(self):
        if type(self.num) == float and type(self.denom) == float:
            n = len(str(self.num).split('.')[1])
            m = len(str(self.denom).split('.')[1])
            if n >= m:
                self.num *= 10 ** n
                self.num = int(self.num)
                self.denom *= 10 ** n
                self.denom = int(self.denom)
            else:
                self.num *= 10 ** m
                self.num = int(self.num)
                self.denom *= 10 ** m
                self.denom = int(self.denom)
        elif type(self.num) == float and type(self.denom) == int:
            n = len(str(self.num).split('.')[1])
            self.num *= 10 ** n
            self.num = int(self.num)
            self.denom *= 10 ** n
        elif type(self.num) == int and type(self.denom) == float:
            m = len(str(self.denom).split('.')[1])
            self.num *= 10 ** m
            self.num = int(self.num)
            self.denom *= 10 ** m
            self.denom = int(self.denom)

    @staticmethod
    def mixed(opt):
        if opt == "False":
            Fraction.type = "simple"
        elif opt == "True":
            Fraction.type = "mixed"

    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        elif self.denom == -1:
            self.num *= -1
            return str(self.num)
        elif self.num == 0:
            return "0"
        elif Fraction.type == "simple":
            return f"{self.num}/{self.denom}"
        elif Fraction.type == "mixed":
            if self.num > 0 and (self.num < self.denom):
                return f"{self.num}/{self.denom}"
            elif self.num < 0 and abs(self.num) > self.denom:
                int_number = self.num // self.denom + 1
                return f"{int_number}({-(self.num - int_number * self.denom)}/{self.denom})"
            else:
                int_number = self.num // self.denom
                return f"{int_number}({self.num - int_number * self.denom}/{self.denom})"

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.denom + other.num * self.denom
            new_denom = self.denom * other.denom
            new_fraction = Fraction(new_num, new_denom)
        else:
            new_fraction = Fraction(self.num + other * self.denom, self.denom)
        return new_fraction

    def __radd__(self, other):
        new_fraction = Fraction(other * self.denom + self.num, self.denom)
        return new_fraction

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.denom - other.num * self.denom
            new_denom = self.denom * other.denom
            new_fraction = Fraction(new_num, new_denom)
        else:
            new_fraction = Fraction(self.num - other * self.denom, self.denom)
        return new_fraction

    def __rsub__(self, other):
        new_fraction = Fraction(other * self.denom - self.num, self.denom)
        return new_fraction

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.num
            new_denom = self.denom * other.denom
            new_fraction = Fraction(new_num, new_denom)
        else:
            new_fraction = Fraction(self.num * other, self.denom)
        return new_fraction

    def __rmul__(self, other):
        new_fraction = Fraction(other * self.num, self.denom)
        return new_fraction

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.denom
            new_denom = self.denom * other.num
            new_fraction = Fraction(new_num, new_denom)
        else:
            new_fraction = Fraction(self.num, self.denom * other)
        return new_fraction

    def __rtruediv__(self, other):
        new_fraction = Fraction(self.denom * other, self.num)
        return new_fraction

    def __lt__(self, other):
        if self.num / self.denom < other.num / other.denom:
            return True
        else:
            return False

    """def __gt__(self, other):
        if self.num/self.denom > other.num/other.denom:
            return True
        else:
            return False"""

    def __le__(self, other):
        if self.num / self.denom <= other.num / other.denom:
            return True
        else:
            return False

    """def __ge__(self, other):
        if self.num/self.denom >= other.num/other.denom:
            return True
        else:
            return False"""

    def __eq__(self, other):
        if self.num / self.denom == other.num / other.denom:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.num / self.denom != other.num / other.denom:
            return True
        else:
            return False

    def __neg__(self):
        return Fraction(-self.num, self.denom)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.denom
