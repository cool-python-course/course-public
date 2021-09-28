import unittest
from parameterized import parameterized
from quadratic import solve

class TestQuadraticSolver(unittest.TestCase):
    """
    Discussion:
     - Order of Arguments in Assert Functions. Actual, Expected or Expected, Actual. Pros/Cons?
     - Given-When-Then Pattern
     - Black Box Testing Technique
     - Type Hinting vs Type Checking. Hinting does not check in Run Time!
    """

    def test_solve_happy_path_two_real_solutions(self):
        # given
        a = 1.0
        b = -1.0
        c = -6.0
        expected_x1 = +3.0
        expected_x2 = -2.0
        # when
        actual_x1 ,actual_x2 = solve(a,b,c)
        # then
        self.assertAlmostEqual(actual_x1,expected_x1)
        self.assertAlmostEqual(actual_x2,expected_x2)

    def test_solve_happy_path_single_real_solution(self):
        # given
        a = 1.0
        b = 4.0
        c = 4.0
        expected = -2.0
        # when
        actual = solve(a,b,c)
        # then
        self.assertAlmostEqual(actual, expected)

    def test_solve_happy_path_no_real_solution(self):
        # given
        a = 1.0
        b = 0.0
        c = 1.0
        # when
        actual = solve(a,b,c)
        # then
        self.assertIsNone(actual)

    def test_solve_should_raise_value_error_if_a_coefficient_is_zero(self):
        # given
        a = 0.0
        b = 1.0
        c = 1.0
        # when then
        self.assertRaises(ValueError, solve, a, b,c)


    @parameterized.expand([
        # String
        ('a',0,0),
        (1,'a',0),
        (1,0,'a'),
        # Complex Number
        (1j,1,1),
        (1,1j,1),
        (1,1,1j),
        # Boolean
        (True,1,1),
        (1,True,1),
        (1,1,True),
        (False,1,1),
        (1,False,1),
        (1,1,False)
    ])
    def test_solve_should_raise_type_error_if_any_coefficient_is_not_float(self, a, b, c):
        # given
        # when then
        self.assertRaises(TypeError, solve, a,b,c)

    def test_further_tasks(self):
        """
        Task:
         - Test the solve_with_tuple implementation.
         - Test Happy Path and Edge Cases
         - Test against ValueError and TypeError
         - Add the Tests Firsts then Implement the solve_with_tuple function.
        :return:
        """
        self.assertTrue(True)