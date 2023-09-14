# Scholarship Database Cleaning and Transformation Documentation

## Introduction
This Python script is designed to clean and transform a scholarship database from a CSV file named "scholarshipdatabase.csv." It performs data cleaning operations to handle missing data and restructures the dataset for further analysis. The cleaned dataset is then saved as "scholarship_df.csv."

## Libraries Used
- `numpy` for numerical operations.
- `pandas` for data manipulation and DataFrame operations.
- `matplotlib` for data visualization (not explicitly used in this code).

## Usage

### Data Loading
1. The script loads the scholarship dataset from "scholarshipdatabase.csv" into a Pandas DataFrame (`df`).

### Data Exploration
1. Displays the first few rows of the dataset using `df.head()`.
2. Retrieves information about the dataset using `df.info()`.

### Data Cleaning - Handling Missing Data
1. Identifies missing data in the dataset using `df.isnull().sum()`.
2. Creates a new DataFrame (`data`) with selected features: 'Name,' 'Area of specialisation,' 'Country,' and 'Level needed.'
3. Splits the 'Area of specialisation' column into separate rows using `,` as a delimiter.
4. Splits the 'Country' column into separate rows using `,` as a delimiter.
5. Splits the 'Level needed' column into separate rows using `,` as a delimiter.
6. Resets the index of the DataFrame to have unique index labels.

### Data Cleaning - Handling Missing Data (Continued)
1. Further identifies missing data in the cleaned dataset using `data.isnull().sum()`.
2. Drops rows with missing values in the 'Name' column using `data.dropna(subset=['Name'], inplace=True)`.

### Data Cleaning - Handling Missing Data (Continued)
1. Fills remaining missing values with empty strings using `data.fillna('', inplace=True)`.

### Data Saving
1. Saves the cleaned and transformed dataset as "scholarship_df.csv" using `data.to_csv('scholarship_df.csv', index=False)`.

## Customization
- You can modify the list of selected features in the 'features' variable to include or exclude specific columns from the cleaned dataset.
- The script assumes that the input dataset is in the format provided in "scholarshipdatabase.csv." Adjustments may be necessary if the dataset format differs.

## Limitations
- The script handles missing data by either dropping rows with missing 'Name' values or filling missing values with empty strings. Consider alternative strategies for handling missing data based on the specific dataset and analysis goals.

## Conclusion
This script provides a data cleaning and transformation process for scholarship data, making it suitable for further analysis and exploration. The cleaned dataset is saved as "scholarship_df.csv" for future use.
