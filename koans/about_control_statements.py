#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutControlStatements(Koan):

    def test_if_then_else_statements(self):
        if True:
            result = 'true value'
        else:
            result = 'false value'
        self.assertEqual('true value', result)
        #True would be the default

    def test_if_then_statements(self):
        result = 'default value'
        if True:
            result = 'true value'
        self.assertEqual('true value', result)
        #True is the default value

    def test_if_then_elif_else_statements(self):
        if False:
            result = 'first value'
        elif True:
            result = 'true value'
        else:
            result = 'default value'
        self.assertEqual('true value', result)
        #True is the default value

    def test_while_statement(self):
        i = 1
        result = 1
        while i <= 10:
            result = result * i
            i += 1
        self.assertEqual(3628800, result)
        #sets i = 1 and result = 1, loops through and every time i is less than 11, it multiplies the result by the value of i, sets the new value of resutl to that number, increases i by one, and does it again.

    def test_break_statement(self):
        i = 1
        result = 1
        while True:
            if i > 10: break
            result = result * i
            i += 1
        self.assertEqual(3628800, result)
        #similar to above, but when i becomes greater than ten, it breaks out of the loop using the break statement

    def test_continue_statement(self):
        i = 0
        result = []
        while i < 10:
            i += 1
            if (i % 2) == 0: continue
            result.append(i)
        self.assertEqual([1, 3, 5, 7, 9], result)
        #sets reult to an empty list and i to i, while i is less than 10, adds the number to the result list. The if statement with the continue makes it so that if it is an even number, it is skipped and not put in the list

    def test_for_statement(self):
        phrase = ["fish", "and", "chips"]
        result = []
        for item in phrase:
            result.append(item.upper())
        self.assertEqual(["FISH", "AND", "CHIPS"], result)
        #.append takes each item in the list and adds them to the empty list called result and .upper makes them all upper case

    def test_for_statement_with_tuples(self):
        round_table = [
            ("Lancelot", "Blue"),
            ("Galahad", "I don't know!"),
            ("Robin", "Blue! I mean Green!"),
            ("Arthur", "Is that an African Swallow or European Swallow?")
        ]
        result = []
        for knight, answer in round_table:
            result.append("Contestant: '" + knight + "'   Answer: '" + answer + "'")

        text = "Contestant: 'Robin'   Answer: 'Blue! I mean Green!'"

        self.assertRegex(result[2], text)
        # takes the results from index 2 under round_table
        self.assertNotRegex(result[0], text)


        self.assertNotRegex(result[1], text)
        self.assertNotRegex(result[3], text)
