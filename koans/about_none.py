#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *

class AboutNone(Koan):

    def test_none_is_an_object(self):
        "Unlike NULL in a lot of languages"
        self.assertEqual(True, isinstance(None, object))
        #https://realpython.com/null-in-python/#:~:text=Python%20uses%20the%20keyword%20None,and%20a%20first%2Dclass%20citizen!
        #in Python, none is the closest equivilant of null, and it is an object and first class citizen!

    def test_none_is_universal(self):
        "There is only one None"
        self.assertEqual(True, None is None)
        #https://realpython.com/null-in-python/#:~:text=Python%20uses%20the%20keyword%20None,and%20a%20first%2Dclass%20citizen!
        #None is immutable so it can not be changed

    def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        What is the Exception that is thrown when you call a method that does
        not exist?

        Hint: launch python command console and try the code in the block below.

        Don't worry about what 'try' and 'except' do, we'll talk about this later
        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            ex2 = ex

        # What exception has been caught?
        #
        # Need a recap on how to evaluate __class__ attributes?
        #
        #     https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

        self.assertEqual(AttributeError, ex2.__class__)

        # What message was attached to the exception?
        # (HINT: replace __ with part of the error message.)
        self.assertRegex(ex2.args[0], "'NoneType' object has no attribute 'some_method_none_does_not_know_about'")

    def test_none_is_distinct(self):
        """
        None is distinct from other things which are False.
        """
        self.assertEqual(True, None is not 0)
        self.assertEqual(True, None is not False)
        #None is it's own thing and is not like null in other language
