import numpy as np
import itertools

def f_228(data_list):
    """
    Unzips a list of tuples and calculates the mean of the numeric values for 
    each position.

    The function accepts a list of tuples, where each tuple consists of 
    alphanumeric values. It unzips the tuples, and calculates the mean of 
    numeric values at each position using numpy, where non numeric values are
    ignores. If all values at a position are non numeric, the mean at this
    position is set to be np.nan.
    If the provided tuples have different number of entries, missing values are 
    treated as zeros.

    Parameters:
    - data_list (list of tuples): The data to process, structured as a list of tuples. Each tuple can contain alphanumeric values.

    Returns:
    - list: A list of mean values for each numeric position across the tuples. Non-numeric positions are ignored.
            An empty list is returned if the input list (data_list) is empty.

    Requirements:
    - numpy
    - itertools

    Example:
    >>> f_228([('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)])
    [nan, 3.0, 4.0]
    >>> f_228([(1, 'a', 2), ('a', 3, 5), ('c', 1, -2)])
    [1.0, 2.0, 1.6666666666666667]
    """
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = [np.nanmean([val for val in column if isinstance(val, (int, float))]) for column in unzipped_data]
    return mean_values

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_regular_input(self):
        # Test with regular input data
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        expected_result = [np.nan, 3.0, 4.0]  # Expected mean values
        result = f_228(data_list)
        np.testing.assert_almost_equal(result, expected_result)
    def test_non_numeric_values(self):
        # Test with non-numeric values in the tuples
        data_list = [('a', 'x', 2), ('b', 2, 3), ('c', 'y', 4), ('d', 4, 'z'), ('e', 'k', 6)]
        expected_result = [np.nan, 3.0, 3.75]  # Expected mean values, non-numeric items are ignored
        result = f_228(data_list)
        np.testing.assert_equal(result, expected_result)
    def test_uneven_tuples(self):
        # Test with uneven tuple lengths
        data_list = [('a', 1), ('b', 2, 3), ('c',), ('d', 4, 5, 6), ('e', 5, 6)]
        expected_result = [np.nan, 3.0, 4.66666666, 6.0]  # Expected mean values
        result = f_228(data_list)
        np.testing.assert_almost_equal(result, expected_result)
    def test_all_non_numeric(self):
        # Test where all elements are non-numeric
        data_list = [('a', 'x'), ('b', 'y'), ('c', 'z'), ('d', 'k'), ('e', 'l')]
        expected_result = [np.nan, np.nan]  # No numeric data to calculate the mean
        result = f_228(data_list)
        np.testing.assert_equal(result, expected_result)
    def test_empty_input(self):
        # Test with an empty input list
        data_list = []
        expected_result = []  # No data to process
        result = f_228(data_list)
        self.assertEqual(result, expected_result)