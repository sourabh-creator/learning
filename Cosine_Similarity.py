#!pip install pandas scikit-learn numpy

# Install necessary libraries
#!pip install pandas numpy scikit-learn seaborn matplotlib openpyxl
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

# Function to calculate cosine similarity
def calculate_cosine_similarity(sheet):
    column1 = sheet.iloc[:, 0].fillna('')
    column2 = sheet.iloc[:, 1].fillna('')
    combined_corpus = column1.tolist() + column2.tolist()
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(combined_corpus)
    cosine_sim_matrix = cosine_similarity(tfidf_matrix[:len(column1)], tfidf_matrix[len(column1):])
    return cosine_sim_matrix

# Function to update Excel file and generate heatmaps
def update_excel_with_cosine_similarity(input_path, output_path):
    excel_data = pd.ExcelFile(input_path)
    sheet_names = excel_data.sheet_names
    updated_sheets = {}
    
    for sheet_name in sheet_names:
        sheet_data = pd.read_excel(excel_data, sheet_name=sheet_name)
        cosine_sim_matrix = calculate_cosine_similarity(sheet_data)
        # Calculate diagonal similarities
        diagonal_similarities = np.diag(cosine_sim_matrix)
        # Adding a new column 'Cosine Similarity'
        sheet_data['Cosine Similarity'] = diagonal_similarities
        updated_sheets[sheet_name] = sheet_data
        
        # Plot heatmap for the cosine similarity matrix
        plt.figure(figsize=(16, 14))  # Increase the figure size
        ax = sns.heatmap(cosine_sim_matrix, annot=True, fmt=".2f", cmap='coolwarm', 
                         cbar_kws={'label': 'Cosine Similarity'}, annot_kws={"size": 8})  # Adjust annotation size
        ax.set_title(f'Cosine Similarity Heatmap - {sheet_name}', fontsize=20)  # Larger title
        ax.set_xlabel('Generated Responses', fontsize=16)  # Larger x-axis label
        ax.set_ylabel('Ground Truth', fontsize=16)  # Larger y-axis label
        plt.xticks(ticks=np.arange(0, len(sheet_data), step=len(sheet_data)//10), rotation=45, ha='right', fontsize=12)  # Larger x-axis ticks
        plt.yticks(ticks=np.arange(0, len(sheet_data), step=len(sheet_data)//10), fontsize=12)  # Larger y-axis ticks
        plt.tight_layout()
        plt.savefig(f'{output_path.split(".xlsx")[0]}_{sheet_name}_Cosine_Similarity_Heatmap.png')
        plt.close()
    
    with pd.ExcelWriter(output_path) as writer:
        for sheet_name, data in updated_sheets.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)

# Specify the path to your input and output Excel files
input_file_path = '/Users/sourabhchaturvedi/Desktop/data/Precesion_Recall_Evalutaion_Sheet_RAG_v1.xlsx'
output_file_path = '/Users/sourabhchaturvedi/Desktop/data/Cosine_Similarity_RAG_Sheet.xlsx'

# Call the function to process the file
update_excel_with_cosine_similarity(input_file_path, output_file_path)




