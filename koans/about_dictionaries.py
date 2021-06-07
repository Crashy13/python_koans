#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutHashes in the Ruby Koans
#

from runner.koan import *

class AboutDictionaries(Koan):
    def test_creating_dictionaries(self):
        empty_dict = dict()
        self.assertEqual(dict, type(empty_dict))
        self.assertDictEqual({}, empty_dict)
        self.assertEqual(0, len(empty_dict))
        #nothing in the empty_dict

    def test_dictionary_literals(self):
        empty_dict = {}
        self.assertEqual(dict, type(empty_dict))
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual(2, len(babel_fish))
        #2 items in the dictionary of babel_fish

    def test_accessing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual('uno', babel_fish['one'])
        self.assertEqual('dos', babel_fish['two'])
        #keys are on the right and values are on the left of the colons

    def test_changing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        babel_fish['one'] = 'eins'

        expected = { 'two': 'dos', 'one': 'eins' }
        self.assertDictEqual(expected, babel_fish)
        #replaced the value of one with eins instead of uno

    def test_dictionary_is_unordered(self):
        dict1 = { 'one': 'uno', 'two': 'dos' }
        dict2 = { 'two': 'dos', 'one': 'uno' }

        self.assertEqual({ 'one': 'uno', 'two': 'dos' } == { 'two': 'dos', 'one': 'uno' }, dict1 == dict2)
        #the dictionaries are the same because the keys and values match in both, eventhough they are in a different order

    def test_dictionary_keys_and_values(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(2, len(babel_fish.keys()))
        #there are 2 keys in the dict
        self.assertEqual(2, len(babel_fish.values()))
        #there are 2 values in the dict
        self.assertEqual(True, 'one' in babel_fish.keys())
        #one is a key
        self.assertEqual(False, 'two' in babel_fish.values())
        #two is not a value, it's a key
        self.assertEqual(False, 'uno' in babel_fish.keys())
        #uno is not a key, it's a value
        self.assertEqual(True, 'dos' in babel_fish.values())
        #dos is a value

    def test_making_a_dictionary_from_a_sequence_of_keys(self):
        cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf', 'confused looking zebra'), 42)

        self.assertEqual(5, len(cards))
        self.assertEqual(42, cards['green elf'])
        self.assertEqual(42, cards['yellow dwarf'])
        #fromkeys sets the value of all key to 42
        #https://www.programiz.com/python-programming/methods/dictionary/fromkeys
