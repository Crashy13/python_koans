#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        self.assertEqual(0, len(empty_list))
        #using list() creates an empty list

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)

        nums.append(333)
        self.assertListEqual([1, 2, 333], nums)
        #https://www.programiz.com/python-programming/methods/list/append
        #append adds an item to the end of a list

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual('peanut', noms[0])
        self.assertEqual('jelly', noms[3])
        self.assertEqual('jelly', noms[-1])
        self.assertEqual('butter', noms[-3])
        #the number inside the square brackets is the index being called. A negative index starts at the end of the list and works backwards

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(['peanut'], noms[0:1])
        #starts at index 0 and goes up to but not including index 1
        self.assertEqual(['peanut', 'butter'], noms[0:2])
        #starts at index 0 and goes up to but not including index 2
        self.assertEqual([], noms[2:2])
        #starts at index 2 and since it stops at index 2, it is an empty list
        self.assertEqual(['and', 'jelly'], noms[2:20])
        #starts at index 2 and would go until index 20 is things are added to the list
        self.assertEqual([], noms[4:0])
        #empty array because there is no index 4 to start at
        self.assertEqual([], noms[4:100])
        #empty array because there is no index 4 to start at
        self.assertEqual([], noms[5:0])
        #empty array because there is no index 5 to start at
        #https://www.geeksforgeeks.org/python-list-slicing/

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(['and', 'jelly'], noms[2:])
        #starts at index 2 and goes to the end of the list
        self.assertEqual(['peanut', 'butter'], noms[:2])
        #starts at the beginning of the list and goes to but not including index 2

    def test_lists_and_ranges(self):
        self.assertEqual(range, type(range(5)))
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        self.assertEqual([0, 1, 2, 3, 4], list(range(5)))
        #starts at 0 and go up to index 5
        self.assertEqual([5, 6, 7, 8], list(range(5, 9)))
        #starts at 5 and go up to index 9

    def test_ranges_with_steps(self):
        self.assertEqual([5, 4], list(range(5, 3, -1)))
        #starts at 5 and goes backwards one at a time up until but not including 3
        self.assertEqual([0, 2, 4, 6], list(range(0, 8, 2)))
        #starts at 0 and goes up by 2 up to but not including 8
        self.assertEqual([1, 4, 7], list(range(1, 8, 3)))
        #starts at 1 and increases by 3 up to but not including 8
        self.assertEqual([5, 1, -3], list(range(5, -7, -4)))
        #starts at 5 and decreases by 4 up to but not including -7
        self.assertEqual([5, 1, -3, -7], list(range(5, -8, -4)))
        #starts at 5 and decreases by 4 up to but not including -8

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(['you', 'shall', 'not', 'pass'], knight)
        #insert adds the string of 'not' at the index indicated, in this case 2, insert mutates the original list

        knight.insert(0, 'Arthur')
        self.assertEqual(['Arthur', 'you', 'shall', 'not', 'pass'], knight)
        #insert adds the string 'Arthur' at the index indicated, in this case 0, insert mutates the original list
        #https://www.programiz.com/python-programming/methods/list/insert

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual([10, 20, 30, 40, 'last'], stack)
        #append adds the item in the () to the end of the list

        popped_value = stack.pop()
        self.assertEqual('last', popped_value)
        self.assertEqual([10, 20, 30, 40], stack)
        #pop removes the last item in a list if no index is supplied in the () and returns it, removing it from the original list

        popped_value = stack.pop(1)
        self.assertEqual(20, popped_value)
        self.assertEqual([10, 30, 40], stack)
        #pop removes the item at the index listed, removing it from the original list
        #https://www.programiz.com/python-programming/methods/list/pop

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

        self.assertEqual([1, 2, 'last'], queue)
        #append adds the item in the () to the end of the list

        popped_value = queue.pop(0)
        self.assertEqual(1, popped_value)
        self.assertEqual([2, 'last'], queue)
        #pop removes the item at the index listed, removing it from the original list

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.
