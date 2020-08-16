import unittest
import puzzles.match_digits_game.match_digits as match_digits


class MathDigitsTest(unittest.TestCase):
    def test_to_string(self):
        for i in range (0, 10):
            md = match_digits.MatchDigit(i)
            mds = str(md)
            print(mds)
            print("value = " + str(md.digit()))
            if i == 0:
                self.assertTrue(mds == ''' _\n| |\n  \n| |\n -\n''')

    def test_match(self):
        md = match_digits.MatchDigit(9)
        for p in match_digits.MatchPosition:
            print(md.has_match(p))
            if p == match_digits.MatchPosition.LOWER_LEFT:
                self.assertTrue(not md.has_match(p))
            else:
                self.assertTrue(md.has_match(p))
        print('-' * 80)

        md = match_digits.MatchDigit(8)
        for p in match_digits.MatchPosition:
            print(md.has_match(p))
            self.assertTrue(md.has_match(p))
        print('-' * 80)

        md = match_digits.MatchDigit(7)
        for p in match_digits.MatchPosition:
            print(md.has_match(p))
            if p == match_digits.MatchPosition.TOP or p == match_digits.MatchPosition.UPPER_RIGHT or p == match_digits.MatchPosition.LOWER_RIGHT:
                self.assertTrue(md.has_match(p))
            else:
                self.assertTrue(not md.has_match(p))
        print('-' * 80)

        md = match_digits.MatchDigit(6)
        for p in match_digits.MatchPosition:
            print(md.has_match(p))
            if p == match_digits.MatchPosition.UPPER_RIGHT:
                self.assertTrue(not md.has_match(p))
            else:
                self.assertTrue(md.has_match(p))
        print('-' * 80)

        md = match_digits.MatchDigit(5)
        for p in match_digits.MatchPosition:
            print(md.has_match(p))
            if p == match_digits.MatchPosition.LOWER_LEFT or p == match_digits.MatchPosition.UPPER_RIGHT:
                self.assertTrue(not md.has_match(p))
            else:
                self.assertTrue(md.has_match(p))
        print('-' * 80)

        md = match_digits.MatchDigit(4)
        for p in match_digits.MatchPosition:
            print(md.has_match(p))
            if p == match_digits.MatchPosition.LOWER_LEFT or p == match_digits.MatchPosition.TOP or p == match_digits.MatchPosition.BOTTOM:
                self.assertTrue(not md.has_match(p))
            else:
                self.assertTrue(md.has_match(p))
        print('-' * 80)

        md = match_digits.MatchDigit(3)
        for p in match_digits.MatchPosition:
            print(md.has_match(p))
            if p == match_digits.MatchPosition.LOWER_LEFT or p == match_digits.MatchPosition.UPPER_LEFT:
                self.assertTrue(not md.has_match(p))
            else:
                self.assertTrue(md.has_match(p))
        print('-' * 80)

        md = match_digits.MatchDigit(2)
        for p in match_digits.MatchPosition:
            print(md.has_match(p))
            if p == match_digits.MatchPosition.LOWER_RIGHT or p == match_digits.MatchPosition.UPPER_LEFT:
                self.assertTrue(not md.has_match(p))
            else:
                self.assertTrue(md.has_match(p))
        print('-' * 80)

        md = match_digits.MatchDigit(1)
        for p in match_digits.MatchPosition:
            print(md.has_match(p))
            if p == match_digits.MatchPosition.UPPER_RIGHT or p == match_digits.MatchPosition.LOWER_RIGHT:
                self.assertTrue(md.has_match(p))
            else:
                self.assertTrue(not md.has_match(p))
        print('-' * 80)

        md = match_digits.MatchDigit(0)
        for p in match_digits.MatchPosition:
            print(md.has_match(p))
            if p == match_digits.MatchPosition.MIDDLE:
                self.assertTrue(not md.has_match(p))
            else:
                self.assertTrue(md.has_match(p))
        print('-' * 80)

    def test_set_match(self):
        md = match_digits.MatchDigit(5)
        md = md.set_match(match_digits.MatchPosition.UPPER_RIGHT)
        print(md)
        self.assertTrue(md.digit() == 9)

    def test_remove_match(self):
        md = match_digits.MatchDigit(9)
        md = md.remove_match(match_digits.MatchPosition.UPPER_LEFT)
        print(md)
        self.assertTrue(md.digit() == 3)