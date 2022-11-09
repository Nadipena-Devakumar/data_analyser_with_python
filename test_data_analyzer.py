import unittest
import data_analyzer

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.data = data_analyzer.answer_the_questions(print_data=False)
    def test_race_count(self):
        actual = dict(self.data['race_count'])
        expected = {'White': 27816, 'Black': 3124, 'Asian-Pac-Islander': 1039, 'Amer-Indian-Eskimo': 311, 'Other': 271}
        self.assertAlmostEqual(actual, expected, "Expected race count values to be {'White': 27816, 'Black': 3124, 'Asian-Pac-Islander': 1039, 'Amer-Indian-Eskimo': 311, 'Other': 271}")

    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 39.4
        self.assertAlmostEqual(actual, expected, "Expected different value for average age of men.")

    def test_bachelors_percentage(self):
        actual = self.data['bachelors_percentage']
        expected = 16.4
        self.assertAlmostEqual(actual, expected, "Expected different value for percentage with Bachelors degrees.")

    def test_perc_adv_education_above_50K(self):
        actual = self.data['perc_adv_education_above_50K']
        expected = 46.5
        self.assertAlmostEqual(actual, expected,"Expected different value for percentage with higher education that earn >50K.")

    def test_perc_low_education_above_50K(self):
        actual = self.data['perc_low_education_above_50K']
        expected = 17.4
        self.assertAlmostEqual(actual, expected,"Expected different value for percentage without higher education that earn >50K.")

    def test_min_working_hours_per_week(self):
        actual = self.data['min_working_hours_per_week']
        expected = 1
        self.assertAlmostEqual(actual, expected, "Expected different value for minimum work hours.")

    def test_perc_people_min_work_above_50K(self):
        actual = self.data['perc_people_min_work_above_50K']
        expected = 10.0
        self.assertAlmostEqual(actual, expected,"Expected different value for percentage of rich among those who work fewest hours.")

    def test_highest_earning_country(self):
        actual = self.data['highest_earning_country']
        expected = 'Iran'
        self.assertAlmostEqual(actual, expected, "Expected different value for highest earning country.")

    def test_highest_earning_country_percentage(self):
        actual = self.data['highest_earning_country_percentage']
        expected = 41.9
        self.assertAlmostEqual(actual, expected, "Expected different value for heighest earning country percentage.")

    def test_most_pop_occup_india(self):
        actual = self.data['most_pop_occup_india']
        expected = 'Prof-specialty'
        self.assertEqual(actual, expected, "Expected different value for top occupations in India.")

if __name__ == '__main__':
    unittest.main()
