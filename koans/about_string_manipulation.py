#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual("The values are one and 2", string)
        #value1 and value2's values are being subbed in for {0} and {1}, the corresponding indices

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)
        #value1 and value2's values are being subbed in for {0} and {1}, the corresponding indices

    def test_any_python_expression_may_be_interpolated(self):
        import math # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
            decimal_places)
        self.assertEqual("The square root of 5 is 2.2361", string)
        #math.sqrt calls a function to find the square root of 5 and decimal_places stops the number at 4 decimal places

    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("let", string[7:10])
        #starts at index 7 and takes each letter up to but not including index 10

    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("a", string[1])
        #takes the letter from index of 1

    def test_single_characters_can_be_represented_by_integers(self):
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))
        #https://www.geeksforgeeks.org/ord-function-python/
        #ord takes a string and returns the unicode

    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual(["Sausage", "Egg", "Cheese"], words)
        #https://www.programiz.com/python-programming/methods/string/split
        #split separates at the white spaces because there was no seperator indicated

    def test_strings_can_be_split_with_different_patterns(self):
        import re #import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        self.assertListEqual(["the", "rain", "in", "spain"], words)
        #https://www.programiz.com/python-programming/methods/built-in/compile
        #compile turns it into a regular string and then split splits them up

        # Pattern is a Python regular expression pattern which matches ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        self.assertEqual('\\n', string)
        self.assertEqual(2, len(string))
        #r makes it a raw string so the \ is not an escape character

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        self.assertEqual("Now is the time", ' '.join(words))
        #.join joins all of the strings together into one string

    def test_strings_can_change_case(self):
        self.assertEqual('Guido', 'guido'.capitalize())
        #capitalizes the first letter
        self.assertEqual('GUIDO', 'guido'.upper())
        #changes all text to uppercase
        self.assertEqual('timbot', 'TimBot'.lower())
        #changes all text to lowercase
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())
        #capitalizes the first letter of each word
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())
        #switches the case of each letter
