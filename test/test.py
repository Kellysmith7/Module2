import unittest
from unittest import mock

from format_output import average_score_2
import unittest.mock


def test_average(self):
    with mock.patch('builtins.input', side_effect=[85, 90, 95]):
        assert average_score_2.average(scores) == 90


if __name__ == '__main__':
    unittest.main()
