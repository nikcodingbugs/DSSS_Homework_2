import unittest
from math_quiz import random_int, random_operator, calculation


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if the random choice is present in the container
        container = "+-*"
        for _ in range(1000):
            operator = random_operator()
            self.assertIn(operator, container)
        pass

    def test_calculation(self):
            # Test if expected problem and answer match with the calculated ones from the function
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 4, '-', '8 - 4', 4),
                (3, 7, '*', '3 * 7', 21)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                real_problem, real_answer = calculation(num1, num2, operator)
                self.assertEqual(expected_problem, real_problem)
                self.assertEqual(expected_answer, real_answer)
                pass

if __name__ == "__main__":
    unittest.main()
