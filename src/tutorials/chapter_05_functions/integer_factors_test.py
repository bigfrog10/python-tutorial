import unittest
import tutorials.chapter_05_functions.integer_factors as integer_factors
import cProfile


class EvenOddTest(unittest.TestCase):
    def test_even(self):
        # print(print.__doc__)

        x = 0
        y = integer_factors.even_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [0])

        x = 1
        y = integer_factors.even_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [0])

        x = 4
        y = integer_factors.even_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [0, 2, 4])

        x = 5
        y = integer_factors.even_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [0, 2, 4])

    def test_odd(self):
        x = 0
        y = integer_factors.odd_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [])

        x = 2
        y = integer_factors.odd_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [1])

        x = 4
        y = integer_factors.odd_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [1, 3])

        x = 5
        y = integer_factors.odd_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [1, 3, 5])

    def test_smaller_primes(self):
        x = 0
        y = integer_factors.smaller_prime_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [])

        x = 3
        y = integer_factors.smaller_prime_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [2])

        x = 10
        y = integer_factors.smaller_prime_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [2, 3, 5, 7])

        x = 25
        y = integer_factors.smaller_prime_numbers(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [2, 3, 5, 7, 11, 13, 17, 19, 23])

    def test_smaller_primes_performance(self):
        cProfile.run('import integer_factors; integer_factors.smaller_prime_numbers(10000)')

    def test_is_prime(self):
        x = 0
        y = integer_factors.is_prime(x)
        print(f'{y}')
        self.assertTrue(not y)

        x = 1
        y = integer_factors.is_prime(x)
        print(f'{y}')
        self.assertTrue(not y)

        x = 2
        y = integer_factors.is_prime(x)
        print(f'{y}')
        self.assertTrue(y)

        x = 4
        y = integer_factors.is_prime(x)
        print(f'{y}')
        self.assertTrue(not y)

        for x in [3, 5, 7, 11]:
            y = integer_factors.is_prime(x)
            print(f'{y}')
            self.assertTrue(y)

        x = 9
        y = integer_factors.is_prime(x)
        print(f'{y}')
        self.assertTrue(not y)

    def test_sieve_of_eratosthenes(self):
        x = 0
        y = integer_factors.sieve_of_eratosthenes(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [])

        x = 2
        y = integer_factors.sieve_of_eratosthenes(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [2])

        x = 10
        y = integer_factors.sieve_of_eratosthenes(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [2, 3, 5, 7])

    def test_sieve_of_eratosthenes1(self):
        x = 0
        y = integer_factors.sieve_of_eratosthenes1(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [])

        x = 2
        y = integer_factors.sieve_of_eratosthenes1(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [2])

        x = 10
        y = integer_factors.sieve_of_eratosthenes1(x)
        print(f'x = {x}, y = {y}')
        self.assertTrue(y == [2, 3, 5, 7])

    def test_prime_factors(self):
        x = 0
        y = integer_factors.prime_factors(x)
        print(f'{y}')
        self.assertTrue(y == {})

        x = 1
        y = integer_factors.prime_factors(x)
        print(f'{y}')
        self.assertTrue(y == {})

        x = 2
        y = integer_factors.prime_factors(x)
        print(f'{y}')
        self.assertTrue(y == {2: 1})

        x = 4
        y = integer_factors.prime_factors(x)
        print(f'{y}')
        self.assertTrue(y == {2: 2})

        x = 3
        y = integer_factors.prime_factors(x)
        print(f'{y}')
        self.assertTrue(y == {3: 1})

        x = 9
        y = integer_factors.prime_factors(x)
        print(f'{y}')
        self.assertTrue(y == {3: 2})

        x = 15
        y = integer_factors.prime_factors(x)
        print(f'{y}')
        self.assertTrue(y == {3: 1, 5: 1})

        x = 45
        y = integer_factors.prime_factors(x)
        print(f'{y}')
        self.assertTrue(y == {3: 2, 5: 1})

        x = 225
        y = integer_factors.prime_factors(x)
        print(f'{y}')
        self.assertTrue(y == {3: 2, 5: 2})

        product = 1
        for k, v in y.items():
            z = k ** v
            product *= z
        self.assertTrue(x == product)

        for x in range(1, 100000):
            y = integer_factors.prime_factors(x)
            product = 1
            for k, v in y.items():
                z = k ** v
                product *= z
            self.assertTrue(x == product)

        x = 11
        y = integer_factors.prime_factors(x)
        print(f'{y}')
        self.assertTrue(y == {11: 1})

    def test_gcd(self):
        x = 0
        y = 1
        z = integer_factors.gcd(x, y)
        print(f'z = {z}')
        self.assertTrue(z == 1)

        x = 1
        y = 0
        z = integer_factors.gcd(x, y)
        print(f'z = {z}')
        self.assertTrue(z == 1)

        x = 20
        y = 6
        z = integer_factors.gcd(x, y)
        print(f'z = {z}')
        self.assertTrue(z == 2)

        x = 20
        y = 4
        z = integer_factors.gcd(x, y)
        print(f'z = {z}')
        self.assertTrue(z == 4)

        self.assertTrue(integer_factors.gcd(10, 10) == 10)

    def test_gcd1(self):
        x = 0
        y = 1
        z = integer_factors.gcd1(x, y)
        print(f'z = {z}')
        self.assertTrue(z == 1)

        x = 1
        y = 0
        z = integer_factors.gcd1(x, y)
        print(f'z = {z}')
        self.assertTrue(z == 1)

        x = 20
        y = 6
        z = integer_factors.gcd1(x, y)
        print(f'z = {z}')
        self.assertTrue(z == 2)

        x = 20
        y = 4
        z = integer_factors.gcd1(x, y)
        print(f'z = {z}')
        self.assertTrue(z == 4)

    def test_gcdm(self):
        x = [16, 32, 40, 20]
        y = integer_factors.gcdm(x)
        print(f'y = {y}')
        self.assertTrue(y == 4)

    def test_gcdm1(self):
        a = integer_factors.gcdm1([0, 1])
        self.assertTrue(a == 1)

    def test_lcm(self):
        x = 0
        y = 0
        z = integer_factors.lcm(x, y)
        print(f'z = {z}')
        self.assertTrue(z == 0)

        x = -1
        y = 0
        z = integer_factors.lcm(x, y)
        print(f'z = {z}')
        self.assertTrue(z == 0)
