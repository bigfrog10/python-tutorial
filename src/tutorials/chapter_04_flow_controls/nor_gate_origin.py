# https://en.wikipedia.org/wiki/NOR_logic
# https://en.wikipedia.org/wiki/NAND_logic


# Defint NOR gate
def NOR(a: bool, b: bool) -> bool:
    if not a and not b:
        return True

    return False


# Now use NOR gate to define all other gates.
# With all gates here, we create the entire computer.
# So all things start from NOR gate.
# 一生二 二生三 三生万物
def NOT(a: bool) -> bool:
    return NOR(a, a)


def OR(a: bool, b: bool) -> bool:
    x = NOR(a, b)
    return NOR(x, x)


def AND(a: bool, b: bool) -> bool:
    return NOR(NOR(a, a), NOR(b, b))


def NAND(a: bool, b: bool) -> bool:
    return NOT(AND(a, b))


def XNOR(a: bool, b: bool) -> bool:
    x = NOR(a, b)
    return NOR(NOR(a, x), NOR(b, x))


def XOR(a: bool, b: bool) -> bool:
    x = NOR(a, a)
    y = NOR(b, b)
    z = NOR(a, b)
    return NOR(NOR(x, y), z)


if __name__ == '__main__':
    print(NOT(False))
