#import nltk
#nltk.download('punkt')
import pandas as pd
from nltk.translate.bleu_score import sentence_bleu
from nltk import word_tokenize
import nltk

# Setting the nltk data directory if not automatically detected
nltk.data.path.append('/Users/sourabhchaturvedi/nltk_data')

def calculate_bleu_score(sheet):
    column1 = sheet.iloc[:, 0].fillna('')
    column2 = sheet.iloc[:, 1].fillna('')
    bleu_scores = []
    
    for text1, text2 in zip(column1, column2):
        reference = word_tokenize(text1.lower())
        candidate = word_tokenize(text2.lower())
        score = sentence_bleu([reference], candidate, weights=(0.25, 0.25, 0.25, 0.25))
        bleu_scores.append(score)
    
    return bleu_scores

def update_excel_with_bleu_score(input_path, output_path):
    excel_data = pd.ExcelFile(input_path)
    sheet_names = excel_data.sheet_names
    updated_sheets = {}
    
    for sheet_name in sheet_names:
        sheet_data = pd.read_excel(excel_data, sheet_name=sheet_name)
        bleu_scores = calculate_bleu_score(sheet_data)
        sheet_data['BLEU Score'] = bleu_scores
        updated_sheets[sheet_name] = sheet_data
    
    with pd.ExcelWriter(output_path) as writer:
        for sheet_name, data in updated_sheets.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)

# Specify the path to your input and output Excel files
input_file_path = '/Users/sourabhchaturvedi/Desktop/data/Precesion_Recall_Evalutaion_Sheet_RAG.xlsx'
output_file_path = '/Users/sourabhchaturvedi/Desktop/data/BLEU_Precesion_Recall_Evaluation_Sheet_RAG.xlsx'

# Call the function to process the file
update_excel_with_bleu_score(input_file_path, output_file_path)
