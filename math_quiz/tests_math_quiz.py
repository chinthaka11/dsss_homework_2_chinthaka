import unittest
from math_quiz import generate_random_integer, generate_random_operator, create_math_problem

class TestMathQuiz(unittest.TestCase):

    def test_generate_random_integer(self):
        """Test if generate_random_integer returns a number within the given range."""
        min_value = 1
        max_value = 10
        for _ in range(100):  # Run multiple times to cover the range
            rand_num = generate_random_integer(min_value, max_value)
            self.assertTrue(min_value <= rand_num <= max_value, f"Random integer {rand_num} is out of range.")

    def test_generate_random_operator(self):
        """Test if generate_random_operator returns one of the specified operators."""
        operators = ['+', '-', '*']
        for _ in range(100):  # Run multiple times to ensure consistency
            operator = generate_random_operator()
            self.assertIn(operator, operators, f"Operator {operator} is not valid.")

    def test_create_math_problem(self):
        """Test if create_math_problem returns the correct problem string and answer."""
        test_cases = [
            (5, 3, '+', '5 + 3', 8),
            (10, 2, '-', '10 - 2', 8),
            (4, 6, '*', '4 * 6', 24),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Expected problem: {expected_problem}, got: {problem}")
            self.assertEqual(answer, expected_answer, f"Expected answer: {expected_answer}, got: {answer}")

if __name__ == "__main__":
    unittest.main()
