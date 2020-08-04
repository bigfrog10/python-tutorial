def AND(a: bool, b: bool) -> bool:
    return a and b


def OR(a: bool, b: bool) -> bool:
    return a or b


def NOT(a: bool) -> bool:
    return not a


def NOR(a: bool, b: bool) -> bool:
    return NOT(OR(a, b))


def NAND(a: bool, b: bool) -> bool:
    return NOT(AND(a, b))


def XOR(a: bool, b: bool) -> bool:
    return AND(NOT(AND(a, b)), OR(a, b))


def XNOR(a: bool, b: bool) -> bool:
    return NOT(XOR(a, b))


if __name__ == '__main__':
    B = [True, False]

    for x in B:
        for y in B:
            z = OR(x, y)
            print(f'{x!s:6} {y!s:6} | {z!s:6}')
