def gcd(n, m):
    n = abs(n)
    m = abs(m)
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


def convert_to_fraction(variable):
    if type(variable) is Fraction:
        return variable
    elif type(variable) is int:
        return Fraction(variable)
    elif type(variable) is float:
        den = 0
        num = 0.1
        while num != int(num):  # подумать над оптимизацией
            den += 1
            num = variable * den
        return Fraction(int(num), den)
    else:
        raise ValueError(f'Unsupported operand type: {type(variable)} for variable {variable}')


class Fraction:

    def __init__(self, top: int, bottom=1):
        common = gcd(top, bottom)
        coef = 1
        if bottom * top < 0:
            coef = -1
        self.num = abs(top) // common * coef
        self.den = abs(bottom) // common

    def __str__(self):
        if self.num == 0:
            return str(self.num)
        elif self.num % self.den == 0:  # is not type convert
            return str(self.num // self.den)
        else:
            return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        other = convert_to_fraction(other)
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        common = gcd(new_den, new_num)
        return Fraction(new_num, new_den)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = convert_to_fraction(other)
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        common = gcd(new_den, new_num)
        return Fraction(new_num, new_den)

    def __rsub__(self, other):
        other = convert_to_fraction(other)
        new_num = other.num * self.den - self.num * other.den
        new_den = self.den * other.den
        common = gcd(new_den, new_num)
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        other = convert_to_fraction(other)
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num, new_den)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other) -> int:
        other = convert_to_fraction(other)
        num = self.num * other.den
        den = self.den * other.num
        return num // den

    def __rfloordiv__(self, other) -> int:
        other = convert_to_fraction(other)
        num = self.den * other.num
        den = self.num * other.den
        return num // den

    def __divmod__(self, other):
        # [0] - div, [1] - mod
        other = convert_to_fraction(other)

        pass

    def __pow__(self, power, modulo=None):
        pass

    def __neg__(self):
        return Fraction(self.num * -1, self.den)

    def __abs__(self):
        return Fraction(abs(self.num), self.den)

    def __round__(self, n=None) -> float:
        return round(self.num / self.den, n)

    def __eq__(self, other) -> bool:
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __ne__(self, other) -> bool:
        if self.__eq__(other):
            return False
        else:
            return True

    def __lt__(self, other) -> bool:
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num < second_num

    def __gt__(self, other) -> bool:
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num > second_num

    def __le__(self, other) -> bool:
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num <= second_num

    def __ge__(self, other) -> bool:
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num >= second_num

    def __float__(self) -> float:
        return self.num / self.den

    def __int__(self) -> int:
        return int(self.__round__())

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den


def main():
    f = Fraction(1, 2)
    print(f)
    print(2 + f)
    print(f - 2)
    print(f * 2)
    print(Fraction(2) // f)
    return


if __name__ == "__main__":
    main()
