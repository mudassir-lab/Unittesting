import unittest
from csv import DictReader
import task3

# matches = open("mock_matches.csv", "r", encoding='utf-8')
# matches_data = DictReader(matches)

# out_of_calculate = task1.calculate(matches_data)


class Task3(unittest.TestCase):

    def setUp(self):
        self.matches_file = open("mock_matches.csv", "r", encoding='utf-8')
        self.matches_data = DictReader(self.matches_file)

        self.deliveries_file = open(
            "mock_deliveries.csv", "r", encoding='utf-8')
        self.deliveries_data = DictReader(self.deliveries_file)

        self.output_of_calculate = task3.calculate(
            self.matches_data, self.deliveries_data)
        self.matches_file.close()
        self.deliveries_file.close()

    def test_calculate(self):
        """This function test calculate function"""
        actual_result = self.output_of_calculate
        correct_result = {'Sunrisers Hyderabad': 2}
        self.assertEqual(actual_result, correct_result)

    def test_transform(self):
        """This function test transform function"""
        actual_result = task3.transform(self.output_of_calculate)
        correct_result = (['Sunrisers Hyderabad'], [2])
        self.assertEqual(actual_result, correct_result)
