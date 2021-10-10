import math


class Fraction:
    def __init__(self, num, denom, option: str = "simple"):
        self.option = option
        if denom == 0:
            raise ZeroDivisionError("You can't divide by 0.")
        else:
            if type(num) == float or type(denom) == float:
                n = len(str(num).split('.')[1])
                m = len(str(denom).split('.')[1])
                if n >= m:
                    num *= 10 ** n
                    num = int(num)
                    denom *= 10 ** n
                    denom = int(denom)
                else:
                    num *= 10 ** m
                    num = int(num)
                    denom *= 10 ** m
                    denom = int(denom)
            self.num = num
            self.denom = denom
            gcd = math.gcd(self.num, self.denom)
            self.num //= gcd
            self.denom //= gcd
            if (self.num < 0 and self.denom < 0) or (self.num > 0 > self.denom):
                self.num *= -1
                self.denom *= -1

    def mixed(self, opt):
        if opt == "False":
            self.option = "simple"
        elif opt == "True":
            self.option = "mixed"

    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        elif self.denom == -1:
            self.num *= -1
            return str(self.num)
        elif self.num == 0:
            return "0"
        elif self.option == "simple":
            return f"{self.num}/{self.denom}"
        elif self.option == "mixed":
            if self.num > 0 and (self.num < self.denom):
                return f"{self.num}/{self.denom}"
            elif self.num < 0 and abs(self.num) > self.denom:
                int_number = self.num // self.denom + 1
                return f"{int_number}({-(self.num - int_number * self.denom)}/{self.denom})"
            else:
                int_number = self.num // self.denom
                return f"{int_number}({self.num - int_number * self.denom}/{self.denom})"

    def __add__(self, other):
        try:
            new_num = self.num * other.denom + other.num * self.denom
            new_denom = self.denom * other.denom
            new_fraction = Fraction(new_num, new_denom, self.option)
        except:
            new_fraction = Fraction(self.num + other * self.denom, self.denom)
        return new_fraction

    def __sub__(self, other):
        try:
            new_num = self.num * other.denom - other.num * self.denom
            new_denom = self.denom * other.denom
            new_fraction = Fraction(new_num, new_denom, self.option)
        except:
            new_fraction = Fraction(self.num - other * self.denom, self.denom)
        return new_fraction

    def __mul__(self, other):
        try:
            new_num = self.num * other.num
            new_denom = self.denom * other.denom
            new_fraction = Fraction(new_num, new_denom, self.option)
        except:
            new_fraction = Fraction(self.num * other, self.denom)
        return new_fraction

    def __truediv__(self, other):
        try:
            new_num = self.num * other.denom
            new_denom = self.denom * other.num
            new_fraction = Fraction(new_num, new_denom, self.option)
        except:
            new_fraction = Fraction(self.num, self.denom * other)
        return new_fraction

    def __lt__(self, other):
        self.mixed("False")
        other.mixed("False")
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

    def get_num(self):
        return self.num

    def get_den(self):
        return self.denom
