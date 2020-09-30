import unittest
import tutorials.chapter_05_functions.string_exercise as string_exercise


class StringTest(unittest.TestCase):
    def test_lcs(self):
        s1 = 'hello'
        s2 = 'man'
        x = string_exercise.lcs(s1, s2)
        print(f's1 = {s1}, s2 = {s2}, common string = {x}')
        self.assertTrue(x == '')

        s1 = 'hello'
        s2 = 'bye'
        x = string_exercise.lcs(s1, s2)
        print(f's1 = {s1}, s2 = {s2}, common string = {x}')
        self.assertTrue(x == 'e')

        s1 = 'hello world'
        s2 = 'bye world'
        x = string_exercise.lcs(s1, s2)
        print(f's1 = {s1}, s2 = {s2}, common string = {x}')
        self.assertTrue(x == ' world')

        s1 = 'hello world'
        s2 = 'hello world'
        x = string_exercise.lcs(s1, s2)
        print(f's1 = {s1}, s2 = {s2}, common string = {x}')
        self.assertTrue(x == 'hello world')
