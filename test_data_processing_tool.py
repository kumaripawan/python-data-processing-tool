from pandas.errors import EmptyDataError
import pytest
import pandas as pd
from io import StringIO
from unittest import mock  # Add mock for example_usage testing
from data_processing_tool import (
    read_csv,
    clean_data,
    transform_data,
    compute_statistics,
    example_usage  # Import example_usage for the test
)


# Test for reading CSV
def test_read_csv():
    csv_data = StringIO("A,B,C\n1,2,3\n4,5,6\n7,8,9")
    df = read_csv(csv_data)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)  # Check if it has 3 rows and 3 columns


# Test for cleaning data
def test_clean_data():
    data = {'A': [1, None, 3], 'B': [4, 5, None], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)
    clean_df = clean_data(df)
    assert clean_df.isnull().sum().sum() == 0  # No missing values
    assert clean_df.shape == (1, 3)  # Only one row without missing values


# Test for transforming data (normalize)
def test_transform_data_normalize():
    data = {'A': [1, 2, 3], 'B': [2, 4, 6], 'C': [3, 6, 9]}
    df = pd.DataFrame(data)
    transformed_df = transform_data(df, 'normalize')
    assert transformed_df.min().min() == 0  # Minimum value should be 0
    assert transformed_df.max().max() == 1  # Maximum value should be 1


# Test for transforming data (standardize)
def test_transform_data_standardize():
    data = {'A': [1, 2, 3], 'B': [2, 4, 6], 'C': [3, 6, 9]}
    df = pd.DataFrame(data)
    transformed_df = transform_data(df, 'standardize')
    assert round(transformed_df.mean().mean(), 2) == 0  # Mean ~ 0
    assert round(transformed_df.std().mean(), 2) == 1   # Std dev ~ 1


# Test for computing statistics
def test_compute_statistics():
    data = {'A': [1, 2, 3], 'B': [2, 2, 2], 'C': [3, 4, 5]}
    df = pd.DataFrame(data)
    stats = compute_statistics(df)
    expected_keys = {'mean', 'median', 'variance'}
    assert expected_keys.issubset(stats.keys())  # Check for all statistics
    assert stats['mean']['A'] == 2
    assert stats['median']['B'] == 2
    assert stats['variance']['C'] == 1


# Test for error handling in transform_data
def test_transform_data_invalid():
    data = {'A': [1, 2, 3]}
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        transform_data(df, 'invalid_transformation')


# Edge Case: Test cleaning data with missing values
def test_clean_data_with_missing_values():
    data = {'A': [1, None, 3], 'B': [4, 5, None], 'C': [7, None, 9]}
    df = pd.DataFrame(data)
    clean_df = clean_data(df)
    assert clean_df.isnull().sum().sum() == 0  # Ensure no missing values
    assert clean_df.shape == (1, 3)  # Only one row left after cleaning


# Edge Case: Test transforming data with zero variance column
def test_transform_data_with_zero_variance():
    data = {'A': [1, 1, 1], 'B': [2, 4, 6], 'C': [3, 6, 9]}
    df = pd.DataFrame(data)
    transformed_df = transform_data(df, 'normalize')
    assert transformed_df['A'].min() == 0  # Zero variance min check
    assert transformed_df['A'].max() == 0  # Zero variance max check


# Edge Case: Test with empty DataFrame
def test_empty_dataset():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="The input DataFrame is empty."):
        clean_data(df)


# Integration Test: Full workflow test
def test_integration_workflow():
    data = {'A': [1, None, 3], 'B': [4, 5, None], 'C': [7, None, 9]}
    df = pd.DataFrame(data)

    clean_df = clean_data(df)
    transformed_df = transform_data(clean_df, 'normalize')
    stats = compute_statistics(transformed_df)

    assert clean_df.shape == (1, 3)  # Only one row left after cleaning
    assert transformed_df.min().min() == 0  # Check normalization
    assert 'mean' in stats  # Ensure statistics were calculated
    assert 'variance' in stats


# Test for FileNotFoundError in read_csv
def test_read_csv_file_not_found():
    with pytest.raises(FileNotFoundError, match="File .* not found."):
        read_csv("non_existent_file.csv")


# Test for EmptyDataError in read_csv
def test_read_csv_empty_file():
    empty_csv = StringIO("")  # Simulating an empty CSV
    with pytest.raises(EmptyDataError, match="File .* is empty or corrupt."):
        read_csv(empty_csv)


# Test for General Exception in read_csv
def test_read_csv_general_exception():
    with pytest.raises(Exception, match="An error occurred: .*"):
        read_csv(None)  # Passing None to trigger a general exception


# Test for Empty DataFrame in clean_data
def test_clean_data_empty_df():
    df = pd.DataFrame()  # Creating an empty DataFrame
    with pytest.raises(ValueError, match="The input DataFrame is empty."):
        clean_data(df)


# Test for Empty DataFrame in transform_data
def test_transform_data_empty_df():
    df = pd.DataFrame()  # Creating an empty DataFrame
    with pytest.raises(ValueError, match="The input DataFrame is empty."):
        transform_data(df, 'normalize')


# Test for Unknown Transformation Type in transform_data
def test_transform_data_invalid_transformation():
    df = pd.DataFrame({'A': [1, 2, 3]})
    with pytest.raises(ValueError, match="Unknown transformation type"):
        transform_data(df, 'invalid')


# Test for example_usage function
def test_example_usage():
    with mock.patch('builtins.print') as mocked_print:
        example_usage()
        assert mocked_print.call_count > 0  # Ensure print was called
