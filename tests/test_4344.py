import unittest
from unittest import mock, TestCase
import io
import sys
from contextlib import contextmanager
from Baekjun.answer.answer_4344 import main, parse_input_string
from Baekjun.answer.answer_4344 import calculate_ratio, convert_float_to_string_format


class Problem4344SimpleTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # parse_input_string TEST ###########
    def test_parse_input_string_case_1(self):
        """
        input : '5 50 50 70 80 100'
        output : [5, 50, 50, 70, 80, 100]
        """
        test_input = '5 50 50 70 80 100'
        test_output = parse_input_string(test_input)
        test_answer = [5, 50, 50, 70, 80, 100]

        self.assertListEqual(test_output, test_answer)

    def test_parse_input_string_case_2(self):
        """
        input : '7 100 95 90 80 70 60 50'
        output : [7, 100, 95, 90, 80, 70, 60, 50]
        """
        test_input = '7 100 95 90 80 70 60 50'
        test_output = parse_input_string(test_input)
        test_answer = [7, 100, 95, 90, 80, 70, 60, 50]

        self.assertListEqual(test_output, test_answer)

    # calculate ratio TEST ###########
    def test_calculate_ratio_case_1(self):
        """
        input : [5, 50, 50, 70, 80, 100]
        output : 2/5
        """
        test_input = [5, 50, 50, 70, 80, 100]
        test_output = calculate_ratio(test_input)
        test_answer = 2 / 5

        self.assertAlmostEqual(test_answer, test_output, delta=1e-3)

    def test_calculate_ratio_case_2(self):
        """
        input : [7, 100, 95, 90, 80, 70, 60, 50]
        output : 4/7
        """
        test_input = [7, 100, 95, 90, 80, 70, 60, 50]
        test_output = calculate_ratio(test_input)
        test_answer = 4 / 7

        self.assertAlmostEqual(test_answer, test_output, delta=1e-3)

    # calculate ratio TEST ###########
    def test_convert_float_to_string_format_case_1(self):
        """
        input : 2/5
        output : 40.000%
        """
        test_input = 2 / 5
        test_output = convert_float_to_string_format(test_input)
        test_answer = '40.000%'

        self.assertEqual(test_answer, test_output)

    def test_convert_float_to_string_format_case_2(self):
        """
        input : 4/7
        output : 57.143%
        """
        test_input = 4 / 7
        test_output = convert_float_to_string_format(test_input)
        test_answer = '57.143%'

        self.assertEqual(test_answer, test_output)

    @mock.patch("Baekjun.answer.answer_4344.read_input",create=True)
    def test_main(self,mock_readline):
        mock_readline.side_effect = [
            "5",
            "5 50 50 70 80 100",
            "7 100 95 90 80 70 60 50",
            "3 70 90 80",
            "3 70 90 81",
            "9 100 99 98 97 96 95 94 93 91"
        ]
        test_answer ='''40.000%
57.143%
33.333%
66.667%
55.556%'''

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
