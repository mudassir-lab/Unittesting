""" Testing for matches won per team per season"""
import unittest
from csv import DictReader
import task2

# matches = open("mock_matches.csv", "r", encoding='utf-8')
# matches_data = DictReader(matches)

# out_of_calculate = task1.calculate(matches_data)


class Task2(unittest.TestCase):

    def setUp(self):
        self.matches_file = open("mock_matches.csv", "r", encoding='utf-8')
        self.matches_data = DictReader(self.matches_file)

        self.output_of_calculate = task2.calculate(self.matches_data)
        self.matches_file.close()

    def test_calculate(self):
        """This function test calculate function"""
        actual_result = self.output_of_calculate
        correct_result = {'Kolkata Knight Riders': {'2015': 1, '2016': 1},
                          'Rajasthan Royals': {'2015': 1, '2016': 0}}
        self.assertEqual(actual_result, correct_result)

    def test_transform(self):
        """This function test transform function"""
        actual_result = task2.transform(self.output_of_calculate)
        correct_result = [[1, 1], [1, 0]]
        self.assertEqual(actual_result, correct_result)
