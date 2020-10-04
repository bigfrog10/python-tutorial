import unittest
import tutorials.chapter_07_classes.match_digits_game.match_digits as match_digits


class MathDigitsTest(unittest.TestCase):
    def test_to_string(self):
        for i in range(0, 10):
            md = match_digits.MatchDigit(i)
            mds = str(md)
            print(mds)
            print("value = " + str(md.digit()))
            if i == 0:
                self.assertTrue(mds == ''' _ \n| |\n   \n| |\n - \n''')

    def test_match(self):
        self.assertTrue(match_digits.MatchDigit(9).only_missing_matches([match_digits.MatchPosition.LOWER_LEFT]))
        self.assertTrue(match_digits.MatchDigit(8).only_missing_matches([]))
        self.assertTrue(match_digits.MatchDigit(7).only_has_matches([
            match_digits.MatchPosition.TOP,
            match_digits.MatchPosition.UPPER_RIGHT,
            match_digits.MatchPosition.LOWER_RIGHT
        ]))
        self.assertTrue(match_digits.MatchDigit(6).only_missing_matches([match_digits.MatchPosition.UPPER_RIGHT]))
        self.assertTrue(match_digits.MatchDigit(5).only_missing_matches([
            match_digits.MatchPosition.LOWER_LEFT,
            match_digits.MatchPosition.UPPER_RIGHT
        ]))
        self.assertTrue(match_digits.MatchDigit(4).only_missing_matches([
            match_digits.MatchPosition.TOP,
            match_digits.MatchPosition.LOWER_LEFT,
            match_digits.MatchPosition.BOTTOM
        ]))
        self.assertTrue(match_digits.MatchDigit(3).only_missing_matches([
            match_digits.MatchPosition.LOWER_LEFT,
            match_digits.MatchPosition.UPPER_LEFT
        ]))
        self.assertTrue(match_digits.MatchDigit(2).only_missing_matches([
            match_digits.MatchPosition.LOWER_RIGHT,
            match_digits.MatchPosition.UPPER_LEFT
        ]))
        self.assertTrue(match_digits.MatchDigit(1).only_has_matches([
            match_digits.MatchPosition.UPPER_RIGHT,
            match_digits.MatchPosition.LOWER_RIGHT
        ]))
        self.assertTrue(match_digits.MatchDigit(0).only_missing_matches([match_digits.MatchPosition.MIDDLE]))

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
