import tutorials.chapter_05_functions.integer_factors as int_factors
import tutorials.chapter_07_classes.modulo_numbers as mod_nums


# linear congruent system:
#     ax ≡ b (mod n)
# if gcd(a, n) = 1, there is unique solution. Otherwise, there are multiple solutions
# if gcd != 1, then we can divide the equation by gcd.
# The solution is
#      x ≡ c (mod n)
# c will be returned

def solve_eq(coeff, residue, mod):
    x, y, gcd = int_factors.euclidean_tuple(coeff, mod)
    if residue % gcd != 0:
        return None  # no solution in this case

    return mod_nums.ModuloNumber(residue * x // gcd, mod // gcd)


def solve_linear_sys(a_n: mod_nums.ModuloNumber, b_m: mod_nums.ModuloNumber):
    """
    solve linear system:
         x ≡ a (mod n)
         x ≡ b (mod m)
    where modulo are different. The solution is
         x ≡ c (mod k)
    so a modulo number will be returned.

    Chinese Remainder Theorem
    https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    https://math.stackexchange.com/questions/1644677/what-to-do-if-the-modulus-is-not-coprime-in-the-chinese-remainder-theorem

    An example is:
        x ≡ 2 (mod 3)
        x ≡ 6 (mod 7)
    Rewrite first equation as x = 3t + 2 for some t, substitute this into 2nd
    equation:
        3t + 2 ≡ 6 (mod 7)
        3t ≡ 4 (mod 7)
    now solve this intermediate from the first function:
        t ≡ 6 (mod 7)
    Rewrite this as t = 7s + 6 and plug this t back into x's expression:
        x = 3t + 2 = 3(7s + 6) + 2 = 21s + 20
    """
    t = solve_eq(a_n.modulo, b_m.residue - a_n.residue, b_m.modulo)
    return mod_nums.ModuloNumber(a_n.modulo * t.residue + a_n.residue, a_n.modulo * b_m.modulo)
