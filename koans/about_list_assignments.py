#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        self.assertEqual(["John", "Smith"], names)

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        self.assertEqual("John", first_name)
        self.assertEqual("Smith", last_name)
        #first_name is set to "John" and last_name is set to "Smith" based on being before and after the comma

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual("Sir", title)
        self.assertEqual(["Ricky", "Bobby"], first_names)
        self.assertEqual("Worthington", last_name)
        #same as above and the * takes the strings after and assigns it to first_name, but "Worthington" isn't included because last_name was added after

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(["Willie", "Rae"], first_name)
        self.assertEqual("Johnson", last_name)
        #the first_name is in a separate list so "Willie" and "Rae" are both the first_name

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        self.assertEqual("Rob", first_name)
        self.assertEqual("Roy", last_name)
        #the third equation switched the values of first_name and last_name
