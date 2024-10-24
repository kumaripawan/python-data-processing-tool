# Python Data Processing Tool

Description
This project is a Python-based tool for data cleaning, transformation, and statistical analysis. It is designed to process datasets by removing missing values, normalizing or standardizing the data, and computing essential statistics such as mean, median, and variance. The project includes automated unit tests written with pytest to ensure the correctness and reliability of the functions.

# Features
Data Cleaning: Removes rows with missing values from the dataset.
Data Transformation: Provides both normalization and standardization of data.
Statistical Computation: Calculates the mean, median, and variance for each column in the dataset.
Unit Testing: All functions are covered with tests using pytest.


## Getting Started

### Prerequisites

Ensure that Python 3.12 or higher is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kumaripawan/python-data-processing-tool.git
2. Navigate to the project directory:
   cd python-data-processing-tool
3. Install the required dependencies:
   pip install -r requirements.txt
   pip install pytest pandas


4. Usage
Running the Data Processing Functions:

The main script data_processing_tool.py includes the following functions:
read_csv(): Reads a CSV file into a Pandas DataFrame.
clean_data(): Removes rows with missing values from the DataFrame.
transform_data(): Transforms data by either normalizing or standardizing it.
compute_statistics(): Computes mean, median, and variance for each column.

You can run the script from the terminal:
python data_processing_tool.py
Running the Unit Tests:

5. To verify the correctness of the functions, run the unit tests using pytest:
python -m pytest

6. Project Structure
├── data_processing_tool.py        # Core Python script with data functions
├── test_data_processing_tool.py   # Unit tests for all functions
├── README.md                      # Project documentation
└── .github/
    └── workflows/
        └── python-app.yml         # GitHub Actions configuration for CI

7. Functions in Detail
read_csv(file): Reads a CSV file and returns it as a Pandas DataFrame.
clean_data(df): Cleans the DataFrame by removing rows with missing values.
transform_data(df, transformation_type): Normalizes or standardizes the data based on the transformation_type parameter.
compute_statistics(df): Returns the mean, median, and variance of the DataFrame columns.

8. Continuous Integration (CI)
This project uses GitHub Actions for continuous integration. Every push or pull request to the main branch triggers the CI pipeline, which automatically runs all unit tests. The CI configuration is located in .github/workflows/python-app.yml.

9. Workflow Description
This project utilizes GitHub Actions for automated testing. Each time changes are pushed to the main branch, tests run automatically to ensure the code quality.

9. Contributing
Contributions are welcome. If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request. Ensure that all changes are covered with unit tests before submitting.

10. Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.
11. License
This project is open source and available under the MIT License.

