import pandas as pd
from typing import Dict
from pandas.errors import EmptyDataError


# Function to read CSV file
def read_csv(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns a pandas DataFrame.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found.")
    except EmptyDataError:
        raise EmptyDataError(f"File {file_path} is empty or corrupt.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")


# Function to clean data (e.g., removing missing values)
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the DataFrame by removing rows with missing values.
    """
    if df.empty:
        raise ValueError("The input DataFrame is empty.")
    df_cleaned = df.dropna(how='any')
    return df_cleaned


# Function to transform data (e.g., normalization or standardization)
def transform_data(df: pd.DataFrame, transformation: str) -> pd.DataFrame:
    """
    Transforms the data by normalizing or standardizing it.

    Args:
        df (pd.DataFrame): The DataFrame to transform.
        transformation (str): 'normalize' or 'standardize'.

    Returns:
        pd.DataFrame: The transformed DataFrame.
    """
    if df.empty:
        raise ValueError("The input DataFrame is empty.")
    if transformation == 'normalize':
        range_values = df.max() - df.min()
        range_values.replace(0, 1, inplace=True)
        return (df - df.min()) / range_values
    elif transformation == 'standardize':
        std_values = df.std()
        std_values.replace(0, 1, inplace=True)
        return (df - df.mean()) / std_values
    else:
        raise ValueError("Unknown transformation type")


# Function to compute statistics (mean, median, variance, etc.)
def compute_statistics(df: pd.DataFrame) -> Dict[str, float]:
    """
    Computes basic statistics (mean, median, variance) for the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to compute statistics on.

    Returns:
        Dict[str, float]: A dictionary containing mean, median, and variance.
    """
    stats = {
        'mean': df.mean().to_dict(),
        'median': df.median().to_dict(),
        # Replace NaN with 0 for variance
        'variance': df.var().fillna(0).to_dict()
    }

    return stats


def example_usage():
    data = {'A': [1, 2, None], 'B': [4, None, 6], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)
    print("Original Data:")
    print(df)

    clean_df = clean_data(df)
    print("Cleaned Data:")
    print(clean_df)

    transformed_df = transform_data(clean_df, 'normalize')
    print("Transformed Data (Normalized):")
    print(transformed_df)

    stats = compute_statistics(transformed_df)
    print("Statistics:")
    print(stats)


if __name__ == "__main__":
    example_usage()  # pragma: no cover

    print("This is a test change to trigger GitHub Actions.")
