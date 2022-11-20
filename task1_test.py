import unittest
import task1
from csv import DictReader

# matches = open("mock_matches.csv", "r", encoding='utf-8')
# matches_data = DictReader(matches)

# out_of_calculate = task1.calculate(matches_data)


class Task1(unittest.TestCase):

    def setUp(self):
        self.matches_file = open("mock_matches.csv", "r", encoding='utf-8')
        self.matches_data = DictReader(self.matches_file)

        self.output_of_calculate = task1.calculate(self.matches_data)
        self.matches_file.close()

    def test_calculate(self):
        """This function test calculate function"""
        actual_result = self.output_of_calculate
        correct_result = {'2015': 2, '2016': 1}
        self.assertEqual(actual_result, correct_result)

    def test_transform(self):
        """This function test transform function"""
        actual_result = task1.transform(self.output_of_calculate)
        correct_result = (['2015', '2016'], [2, 1])
        self.assertEqual(actual_result, correct_result)
