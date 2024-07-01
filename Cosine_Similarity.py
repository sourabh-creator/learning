#!pip install pandas scikit-learn numpy
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def calculate_cosine_similarity(sheet):
    column1 = sheet.iloc[:, 0].fillna('')
    column2 = sheet.iloc[:, 1].fillna('')
    combined_corpus = column1.tolist() + column2.tolist()
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(combined_corpus)
    cosine_sim_matrix = cosine_similarity(tfidf_matrix[:len(column1)], tfidf_matrix[len(column1):])
    return np.diag(cosine_sim_matrix)

def update_excel_with_cosine_similarity(input_path, output_path):
    excel_data = pd.ExcelFile(input_path)
    sheet_names = excel_data.sheet_names
    updated_sheets = {}
    
    for sheet_name in sheet_names:
        sheet_data = pd.read_excel(excel_data, sheet_name=sheet_name)
        similarities = calculate_cosine_similarity(sheet_data)
        # Adding a new column 'Cosine Similarity'
        sheet_data['Cosine Similarity'] = similarities
        updated_sheets[sheet_name] = sheet_data
    
    with pd.ExcelWriter(output_path) as writer:
        for sheet_name, data in updated_sheets.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)

# Specify the path to your input and output Excel files
input_file_path = '/Users/sourabhchaturvedi/Desktop/data/Precesion_Recall_Evalutaion_Sheet_RAG_v1.xlsx'
output_file_path = '/Users/sourabhchaturvedi/Desktop/data/Cosine_Similarity_Precesion_Recall_Evalutaion_Sheet_RAG.xlsx'

# Call the function to process the file
update_excel_with_cosine_similarity(input_file_path, output_file_path)


#  Exporting the DataFrame to an Excel file
#output_excel_path = '/Users/sourabhchaturvedi/Desktop/data/Precesion_Recall_Evalutaion_Sheet_RAG.xlsx'





