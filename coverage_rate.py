import pandas as pd

def calculate_coverage(gt_row, response_row):
    # Count matching items and total items for coverage calculation
    total_columns = len(gt_row)
    matches = sum(1 for gt_item, response_item in zip(gt_row, response_row) if gt_item == response_item)
    return matches / total_columns if total_columns > 0 else 0

def load_data(ground_truth_path, response_path):
    # Load data from Excel
    ground_truth_df = pd.read_excel(ground_truth_path)
    response_df = pd.read_excel(response_path)
    return ground_truth_df, response_df

def add_coverage_rates(ground_truth_df, response_df):
    # Calculate coverage rates for each row
    coverage_rates = [calculate_coverage(gt_row, response_row) 
                      for gt_row, response_row in zip(ground_truth_df.values, response_df.values)]
    response_df['Coverage Rate'] = coverage_rates
    return response_df

# Specify the paths to your ground truth and response Excel files
ground_truth_path = '/Users/sourabhchaturvedi/Desktop/data/SLR4CloudEvaluation.xlsx'
response_path = '/Users/sourabhchaturvedi/Desktop/data/all_results.xlsx'

# Load the ground truth and response data
ground_truth_df, response_df = load_data(ground_truth_path, response_path)

# Add coverage rates to the response DataFrame
response_df_with_coverage = add_coverage_rates(ground_truth_df, response_df)

# Save the updated DataFrame to a new Excel file
response_df_with_coverage.to_excel('/Users/sourabhchaturvedi/Desktop/data/response_with_coverage_rates.xlsx', index=False)

print("Coverage rates added and file saved as 'response_with_coverage_rates.xlsx'")
