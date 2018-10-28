import unittest
from unittest import mock, TestCase
import io
import sys
from contextlib import contextmanager
sys.path.append("../")
from answer.answer_11051 import main, solve_binomial_coefficient


class Problem11051SimpleTest(TestCase):
    def test_solve_binomial_coefficient_when_n_is_2_and_k_is_1(self):
        test_output = solve_binomial_coefficient(2, 1)
        test_answer = 2
        self.assertEqual(test_answer, test_output)

    def test_solve_binomial_coefficient_when_n_is_3_and_k_is_1(self):
        test_output = solve_binomial_coefficient(3, 1)
        test_answer = 3
        self.assertEqual(test_answer, test_output)

    def test_solve_binomial_coefficient_when_n_is_3_and_k_is_2(self):
        test_output = solve_binomial_coefficient(3, 2)
        test_answer = 3
        self.assertEqual(test_answer, test_output)

    def test_solve_binomial_coefficient_when_n_is_5_and_k_is_2(self):
        test_output = solve_binomial_coefficient(5, 2)
        test_answer = 10
        self.assertEqual(test_answer, test_output)

    def test_solve_binomial_coefficient_when_n_is_5_and_k_is_3(self):
        test_output = solve_binomial_coefficient(5, 3)
        test_answer = 10
        self.assertEqual(test_answer, test_output)

    def test_solve_binomial_coefficient_when_n_is_10_and_k_is_2(self):
        test_output = solve_binomial_coefficient(10, 2)
        test_answer = 45
        self.assertEqual(test_answer, test_output)


    @mock.patch("answer.answer_11051.read_input",create=True)
    def test_main(self,mock_readline):
        mock_readline.return_value = '5 2'
        test_answer = "10"
        with captured_output() as (out, err):
            main()
        output = out.getvalue().strip()

        self.assertEqual(test_answer, output)


@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


if __name__ == "__main__":
    unittest.main()
