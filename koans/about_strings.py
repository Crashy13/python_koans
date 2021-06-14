#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, str))
        #isinstance compares the first object to the class type being called
        #double quotes can be used to indicate a string

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        self.assertEqual(True, isinstance(string, str))
        #single quotes can be used to indicate a string

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        self.assertEqual(True, isinstance(string, str))
        #triple quotes can be used to indicate a string

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, str))
        #triple single quotes can be used to indicate a string

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        self.assertEqual(True, isinstance(string, str))
        #https://www.askpython.com/python/string/python-raw-strings
        #the r before the string creates a raw string, meaning all content in the string will be literal, meaning everything will be printed, no escape characters

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        self.assertEqual('He said, "Go Away."', string)
        #when using single quotes, you can use double quotes inside without it disrupting the string

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        self.assertEqual("Don't", string)
        #when using double quotes, you can use single quotes inside without it disrupting the string

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b))
        #https://www.python-ds.com/python-strings
        #you can use single or double quotes inside a string that uses the same if you use a \, also known as an escape character

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        self.assertEqual(52, len(string))
        #\n\ causes the string to break out into a new line, but it's the same string

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        self.assertEqual(15, len(string))
        #https://www.geeksforgeeks.org/triple-quotes-in-python/
        #using triple quotes will cause the string to span over multiple lines

    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual("Hello \"world\"." == """Hello "world".""", (a == b))
        #since there is only a single double quote inside the triple double quotes separated by a character, no escape characters are needed

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        self.assertEqual("""Hello "world\"""", string)
        #since the end of the double quotes is not separated from the ending triple quotes by any characters, the escape character is needed

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual("Hello, world", string)
        #https://www.jquery-az.com/5-ways-python-string-concatenation-6-examples/
        #using the + sign will concatenate the two strings into one

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual("Hello, world", string)
        #https://www.jquery-az.com/5-ways-python-string-concatenation-6-examples/
        #when separating string literals with just a space, they will automatically concatenate

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)
        #you can use the + sign with the variables that the strings are assigned to as well

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)
        #using += will add the second string to the first without having to use a new variable

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original)
        #eventhough hi is = to original, using += does not change original

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))
        #https://www.geeksforgeeks.org/preventing-escape-sequence-interpretation-in-python/
        #escape characters work in most strings, except for raw string and when using double backslashes
