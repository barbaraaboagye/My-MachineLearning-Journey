# Scholarship Database Cleaning and Scholarship Recommender System

This repository contains two Python scripts for working with scholarship data: one for cleaning and transforming a scholarship database([Data processing](https://github.com/barbaraaboagye/My-MachineLearning-Journey/blob/1e19a3a7caf86f8b0603ed100144ff94d536a769/Projects/Scholarship%20recommender%20system/Data_processing.ipynb)) and the other for recommending scholarships([Scholarship recommender system](https://github.com/barbaraaboagye/My-MachineLearning-Journey/blob/341290ad75417f9f04a2b5ee7628721e343afa05/Projects/Scholarship%20recommender%20system/Scholarship%20recommender%20system.ipynb)) based on a user's area of specialization. Below are details on how to use each script.

### 1. Scholarship Database Cleaning 

### Introduction
The Scholarship Database Cleaning script cleans and transforms a scholarship database from a CSV file named "scholarshipdatabase.csv." It handles missing data and restructures the dataset for analysis.

### Libraries Used
- `numpy` for numerical operations.
- `pandas` for data manipulation and DataFrame operations.

### Usage
1. **Data Loading**: The script loads the scholarship dataset from "scholarshipdatabase.csv" into a Pandas DataFrame.

2. **Data Exploration**:
   - Displays the first few rows of the dataset.
   - Retrieves information about the dataset.

3. **Data Cleaning - Handling Missing Data**:
   - Identifies missing data in the dataset.
   - Creates a new DataFrame with selected features.
   - Splits certain columns into separate rows.
   - Resets the index for unique labels.

4. **Data Cleaning - Handling Missing Data (Continued)**:
   - Further identifies missing data in the cleaned dataset.
   - Drops rows with missing 'Name' values.
   - Fills remaining missing values with empty strings.

5. **Data Saving**:
   - Saves the cleaned dataset as "scholarship_df.csv."

### Customization
- You can modify the list of selected features in the 'features' variable to include or exclude specific columns from the cleaned dataset.
- Ensure your input dataset follows a similar format to "scholarshipdatabase.csv" for successful cleaning and transformation.

## Conclusion
This script provides a data cleaning and transformation process for scholarship data, making it suitable for further analysis and exploration. The cleaned dataset is saved as "scholarship_df.csv" for future use.

## 2. Scholarship Recommender System

### Introduction
The Scholarship Recommender script allows users to find relevant scholarships or universities based on their area of specialization or interest. It utilizes fuzzy string matching to identify similar specializations in a given dataset of scholarships.

### Libraries Used
- `pandas` for data manipulation and DataFrame operations.
- `fuzzywuzzy` for fuzzy string matching.

### Usage
1. **Input**: Run the script, and it will prompt you to enter your area of specialization.

2. **Data Loading**: The script loads scholarship data from a CSV file named "scholarship_df.csv" into a Pandas DataFrame.

3. **Data Preprocessing**:
   - Converts the 'Area of Specialisation' column in the DataFrame to lowercase for case-insensitive matching.
   - Creates a list of unique specializations from the DataFrame.

4. **Similarity Scoring**:
   - Initializes a dictionary to store similarity scores between the user's input and specializations.
   - Calculates similarity scores using fuzzy string matching for each specialization in the dataset.
   - Sorts the specializations by similarity score in descending order.
   - Extracts matched specializations based on a similarity score threshold (adjustable).

5. **Recommendation**:
   - Filters scholarships based on matched specializations.
   - Removes duplicate scholarships based on their names.
   - Provides a list of recommended scholarships/universities.

### Customization
- You can adjust the similarity score threshold to control the level of similarity between the user's input and recommended specializations.
- Ensure your dataset is in the same format with a column named 'Area of Specialisation' for best results.

### Conclusion
This script offers a simple scholarship recommendation system based on user input and fuzzy string matching. It can be customized and extended to handle larger datasets and provide more advanced recommendation features.

