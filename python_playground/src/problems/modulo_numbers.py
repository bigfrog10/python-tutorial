import problems.integer_factors as int_factors


class ModuloNumber:
    """
    model integer modulo numbers, e.g., x ≡ 2 (mod 5), which is ModuloNumber(2, 5).
    Integer 10 can be rewritten as ModuleNumber(10, 1).

    Furthermore, we treat following as same number: 2 (mod 5) and 4 (mod 10), i.e.,
    times 2 on both residue and mod. This provide a common ground for different
    modulo

    operations:
    (a ± b) mod n = [(a mod n) ± (b mod n)] mod n
    k(a mod n) = ka mod n

    ab mod n = [(a mod n)(b mod n)] mod n
    (a mod n)^k = a^k mod n

    This is to model periodic behaviors, such as every minute(60 seconds), hour,
    day, weekday, month, year

    https://en.wikipedia.org/wiki/Modulo_operation
    https://en.wikipedia.org/wiki/Modular_arithmetic
    https://www.geeksforgeeks.org/operator-overloading-in-python/

    keywords: remainder/residue, congruent/modulo
    """
    def __init__(self, residue, modulo):
        if modulo == 0:
            raise ValueError('modulo is zero, not allowed!')

        self.modulo = modulo if modulo > 0 else -modulo

        if self.modulo == 1:
            self.residue = residue if residue > 0 else -residue
        else:
            self.residue = residue if residue > 0 \
                else residue - self.modulo * (residue // self.modulo)

        self.residue = self.residue % self.modulo

        # to ensure gcd(residue, module) = 1 (co-prime), so that it has
        # multiplicative inverse.
        gcd = int_factors.gcd(self.residue, self.modulo)
        self.modulo = self.modulo // gcd
        self.residue = self.residue // gcd

    # unary operators
    def __invert__(self):  # multiplicative inverse
        x, y, gcd = int_factors.euclidean_tuple(self.residue, self.modulo)
        return x

    def __neg__(self):  # additive inverse
        return ModuloNumber(-self.residue, self.modulo)

    # arithmetic operations
    def __add__(self, other):
        if isinstance(other, int):
            return ModuloNumber(self.residue + other, self.modulo)
        elif isinstance(other, ModuloNumber):
            if other.modulo == self.modulo:  # separate these 2 cases for performance reason.
                return ModuloNumber(self.residue + other.residue, self.modulo)
            else:
                modulo_lcm = int_factors.lcm(self.modulo, other.modulo)
                x = modulo_lcm / other.modulo
                y = modulo_lcm / self.modulo
                return ModuloNumber(self.residue * x + other.residue * y, modulo_lcm)
        else:
            raise ValueError('unknow data type: {}'.format(other))

    def __sub__(self, other):
        if isinstance(other, int):
            return ModuloNumber(self.residue - other, self.modulo)
        elif isinstance(other, ModuloNumber):
            if other.modulo == self.modulo:  # separate these 2 cases for performance reason.
                return ModuloNumber(self.residue - other.residue, self.modulo)
            else:
                modulo_lcm = int_factors.lcm(self.modulo, other.modulo)
                x = modulo_lcm / other.modulo
                y = modulo_lcm / self.modulo
                return ModuloNumber(self.residue * x - other.residue * y, modulo_lcm)
        else:
            raise ValueError('unknow data type: {}'.format(other))

    def __mul__(self, other):
        if isinstance(other, int):
            return ModuloNumber(self.residue * other, self.modulo)
        elif isinstance(other, ModuloNumber):
            if other.modulo == self.modulo:  # separate these 2 cases for performance reason.
                return ModuloNumber(self.residue * other.residue, self.modulo)
            else:
                modulo_lcm = int_factors.lcm(self.modulo, other.modulo)
                x = modulo_lcm / other.modulo
                y = modulo_lcm / self.modulo
                return ModuloNumber(self.residue * x * other.residue * y, modulo_lcm)
        else:
            raise ValueError('unknow data type: {}'.format(other))

    def __truediv__(self, other):
        if isinstance(other, int):
            return ModuloNumber(self.residue // other, self.modulo)
        elif isinstance(other, ModuloNumber):
            return self.__mul__(other.__invert__())
        else:
            raise ValueError('unknow data type: {}'.format(other))

    def __pow__(self, power, modulo=None):
        ret = self
        for i in range(power-1):
            ret = ret.__mul__(self)

        return ret

    # comparisons
    def __eq__(self, other):
        if isinstance(other, int):
            return self.residue == other  # ??? is this correct?
        elif isinstance(other, ModuloNumber):
            if other.modulo == self.modulo:  # separate these 2 cases for performance reason.
                return self.residue == other.residue
            else:
                modulo_lcm = int_factors.lcm(self.modulo, other.modulo)
                x = modulo_lcm / other.modulo
                y = modulo_lcm / self.modulo
                return self.residue * x == other.residue * y
        else:
            raise ValueError('unknow data type: {}'.format(other))

    def __ne__(self, other):
        if isinstance(other, int):
            return self.residue != other  # ??? is this correct?
        elif isinstance(other, ModuloNumber):
            if other.modulo == self.modulo:  # separate these 2 cases for performance reason.
                return self.residue != other.residue
            else:
                modulo_lcm = int_factors.lcm(self.modulo, other.modulo)
                x = modulo_lcm / other.modulo
                y = modulo_lcm / self.modulo
                return self.residue * x != other.residue * y
        else:
            raise ValueError('unknow data type: {}'.format(other))

    def __gt__(self, other):
        if isinstance(other, int):
            return self.residue > other  # ??? is this correct?
        elif isinstance(other, ModuloNumber):
            if other.modulo == self.modulo:  # separate these 2 cases for performance reason.
                return self.residue > other.residue
            else:
                modulo_lcm = int_factors.lcm(self.modulo, other.modulo)
                x = modulo_lcm / other.modulo
                y = modulo_lcm / self.modulo
                return self.residue * x > other.residue * y
        else:
            raise ValueError('unknow data type: {}'.format(other))

    def __ge__(self, other):
        if isinstance(other, int):
            return self.residue >= other  # ??? is this correct?
        elif isinstance(other, ModuloNumber):
            if other.modulo == self.modulo:  # separate these 2 cases for performance reason.
                return self.residue >= other.residue
            else:
                modulo_lcm = int_factors.lcm(self.modulo, other.modulo)
                x = modulo_lcm / other.modulo
                y = modulo_lcm / self.modulo
                return self.residue * x >= other.residue * y
        else:
            raise ValueError('unknow data type: {}'.format(other))

    def __lt__(self, other):
        if isinstance(other, int):
            return self.residue < other  # ??? is this correct?
        elif isinstance(other, ModuloNumber):
            if other.modulo == self.modulo:  # separate these 2 cases for performance reason.
                return self.residue < other.residue
            else:
                modulo_lcm = int_factors.lcm(self.modulo, other.modulo)
                x = modulo_lcm / other.modulo
                y = modulo_lcm / self.modulo
                return self.residue * x < other.residue * y
        else:
            raise ValueError('unknow data type: {}'.format(other))

    def __le__(self, other):
        if isinstance(other, int):
            return self.residue <= other  # ??? is this correct?
        elif isinstance(other, ModuloNumber):
            if other.modulo == self.modulo:  # separate these 2 cases for performance reason.
                return self.residue <= other.residue
            else:
                modulo_lcm = int_factors.lcm(self.modulo, other.modulo)
                x = modulo_lcm / other.modulo
                y = modulo_lcm / self.modulo
                return self.residue * x <= other.residue * y
        else:
            raise ValueError('unknow data type: {}'.format(other))


