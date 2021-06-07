#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutTuples(Koan):
    def test_creating_a_tuple(self):
        count_of_three =  (1, 2, 5)
        self.assertEqual(5, count_of_three[2])

    def test_tuples_are_immutable_so_item_assignment_is_not_possible(self):

        count_of_three = (1, 2, 5)
        try:
            count_of_three[2] = "three"
        except TypeError as ex:
            msg = ex.args[0]

        # Note, assertRegex() uses regular expression pattern matching,
        # so you don't have to copy the whole message.

        self.assertRegex(msg, "'tuple' object does not support item assignment")

    def test_tuples_are_immutable_so_appending_is_not_possible(self):
        count_of_three =  (1, 2, 5)
        with self.assertRaises(Exception): count_of_three.append("boom")
        #https://www.geeksforgeeks.org/test-if-a-function-throws-an-exception-in-python/

        # Tuples are less flexible than lists, but faster.

    def test_tuples_can_only_be_changed_through_replacement(self):
        count_of_three = (1, 2, 5)

        list_count = list(count_of_three)
        list_count.append("boom")
        count_of_three = tuple(list_count)

        self.assertEqual((1, 2, 5, "boom"), count_of_three)
        #https://www.programiz.com/python-programming/tuple
        #tuple is a list that can't be changed. The original list was appended with "boom" and then made into a tuple

    def test_tuples_of_one_look_peculiar(self):
        self.assertEqual(int, (1).__class__)
        #1 is an integer
        self.assertEqual(tuple, (1,).__class__)
        #adding the comma makes this a tuple
        self.assertEqual(tuple, ("I'm a tuple",).__class__)
        #the comma inside the () makes this a tuple
        self.assertEqual(str, ("Not a tuple").__class__)
        #no comma so this is a string

    def test_tuple_constructor_can_be_surprising(self):
        self.assertEqual(('S', 'u', 'r', 'p', 'r', 'i', 's', 'e', '!'), tuple("Surprise!"))
        #https://www.programiz.com/python-programming/methods/built-in/tuple
        #using the tuple() turns the string into a tuple, separating each character into it's own string

    def test_creating_empty_tuples(self):
        self.assertEqual(() , ())
        self.assertEqual(() , tuple()) #Sometimes less confusing
        #empty tuples are just empty ()

    def test_tuples_can_be_embedded(self):
        lat = (37, 14, 6, 'N')
        lon = (115, 48, 40, 'W')
        place = ('Area 51', lat, lon)
        self.assertEqual(('Area 51', (37, 14, 6, 'N'), (115, 48, 40, 'W')), place)
        #lat and lon are still there own tuples but have been nested into a larger tuple

    def test_tuples_are_good_for_representing_records(self):
        locations = [
            ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
            ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
        ]

        locations.append( ("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W')) )

        self.assertEqual("Cthulu", locations[2][0])
        #the append added the 3 tuple in so it was index 2 and index 0 of that tuple was "Cthulu"
        self.assertEqual(15.56, locations[0][1][2])
        #Illuminati HQ is index 0 of the main list then index 1 is the first set of coordinates and 15.56 is at index 2 in that
