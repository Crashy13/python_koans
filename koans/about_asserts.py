#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutAsserts(Koan):

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        # self.assertTrue(False) # This should be True
        self.assertTrue(True) #assert dictates True must be in the ()

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """
        # self.assertTrue(False, "This should be True -- Please fix this")
        self.assertTrue(True, "This should be True -- Please fix this") #assert dictates True must be in the () and can also have messages

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        # self.assertEqual(__, 1 + 1)
        self.assertEqual(2, 1 + 1) #assert dictates what's on the left of the comma must equal what's on the right

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.
        """
        # expected_value = __
        # actual_value = 1 + 1
        # self.assertTrue(expected_value == actual_value)
        expected_value = 2
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value) #assert dictates both sides of equation must be equal

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        # expected_value = __
        # actual_value = 1 + 1
        #
        # self.assertEqual(expected_value, actual_value)
        expected_value = 2
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value) #assert dictates both sides of the comma must be equal

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        """
        Understand what lies within.
        """

        # This throws an AssertionError exception
        # assert False
        assert True #assert needs to be set to True

    def test_that_sometimes_we_need_to_know_the_class_type(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:

        self.assertEqual(str, "navel".__class__) # It's str, not <type 'str'> the class type of navel is string

        # Need an illustration? More reading can be found here:
        #
        #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute
