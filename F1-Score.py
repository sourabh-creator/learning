# # Load the data from Excel files
# ground_truth = pd.read_excel('/Users/sourabhchaturvedi/Desktop/data/SLR4CloudEvaluation.xlsx', index_col='id')  # Adjust path as necessary
# responses = pd.read_excel('/Users/sourabhchaturvedi/Desktop/data/all_results.xlsx', index_col='id')        # Adjust path as necessary

import pandas as pd
from sklearn.metrics import f1_score

# Load the data
ground_truth_path = '/Users/sourabhchaturvedi/Desktop/data/SLR4CloudEvaluation.xlsx'
response_path = '/Users/sourabhchaturvedi/Desktop/data/all_results.xlsx'
ground_truth_data = pd.read_excel(ground_truth_path)
response_data = pd.read_excel(response_path)

# Ensure column names are aligned
response_data.columns = ground_truth_data.columns

# Initialize a DataFrame to store the comparison results
comparison_results = pd.DataFrame()

# Loop through each column to compare each cell
for column in ground_truth_data.columns:
    # Normalize data by converting to strings, making it lowercase, and stripping whitespace
    truth = ground_truth_data[column].astype(str).str.lower().str.strip()
    response = response_data[column].astype(str).str.lower().str.strip()

    # Create binary labels for comparison: 1 if match, 0 if no match
    matches = (truth == response).astype(int)

    # Calculate F1 score for each column based on matches
    f1 = f1_score([1] * len(matches), matches, zero_division=1)  # Ideal response is all matches (all 1s)
    
    # Store F1 scores and the comparison in a DataFrame
    comparison_results[column] = matches  # Storing the comparison result per cell
    comparison_results[column + ' F1 Score'] = [f1] * len(matches)  # Repeating F1 score for visibility per cell

# Transpose DataFrame for better visibility if needed
comparison_results_transposed = comparison_results.T

# Save the results to an Excel file
output_path = '/Users/sourabhchaturvedi/Desktop/data/f1_scores_detailed_final.xlsx'
comparison_results.to_excel(output_path)

# Print the DataFrame with comparison results
print(comparison_results_transposed)
