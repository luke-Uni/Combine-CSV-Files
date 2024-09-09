# CSV File Combiner

This script combines multiple CSV files from a specified directory into a single CSV file using Python and pandas.

## Features

- Automatically searches for all CSV files in a given directory.
- Skips the header row (first row) in each CSV file.
- Combines the content of all CSV files into a single pandas DataFrame.
- Exports the combined DataFrame to a new CSV file called `combined_data.csv`.

## Installation

1. Clone the repository or download the script.
2. Install the required Python package using pip:

    ```bash
    pip install pandas
    ```

## Usage

1. Set the `csv_dir` variable to the path where your CSV files are located:

    ```python
    csv_dir = "Path to directory containing CSV files"
    ```

2. Run the script:

    ```bash
    python combine_csv.py
    ```

3. After running the script, a new file `combined_data.csv` will be created in the same directory where the script is located.
