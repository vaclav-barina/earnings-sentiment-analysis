import docx
import re
import nltk
from nltk.tokenize import sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import csv

nltk.download('punkt')

path_doc1, path_doc2, path_doc3, path_doc4 = [
    r"C:\Users\Vaclav Barina\Documents\3. Study\2. Data Science\1. Fun Projects\2023_Earnings Transcript Sentiment\1. BYND Data and Analysis\1. Raw Data\2019 Q4_BYND Earnings Transcript.docx",
    r"C:\Users\Vaclav Barina\Documents\3. Study\2. Data Science\1. Fun Projects\2023_Earnings Transcript Sentiment\1. BYND Data and Analysis\1. Raw Data\2020 Q4_BYND Earnings Transcript.docx",
    r"C:\Users\Vaclav Barina\Documents\3. Study\2. Data Science\1. Fun Projects\2023_Earnings Transcript Sentiment\1. BYND Data and Analysis\1. Raw Data\2021 Q4_BYND Earnings Transcript.docx",
    r"C:\Users\Vaclav Barina\Documents\3. Study\2. Data Science\1. Fun Projects\2023_Earnings Transcript Sentiment\1. BYND Data and Analysis\1. Raw Data\2022 Q4_BYND Earnings Transcript.docx"
]

all_doc_paths = [path_doc1, path_doc2, path_doc3, path_doc4]
document_scores = []

for file_path in all_doc_paths:
    doc = docx.Document(file_path)
    year = file_path.split("\\")[-1].split()[0] # Extract the year of analysis from file path

    # Create a list of sentences from the raw transcript
    text = '\n'.join([para.text for para in doc.paragraphs]) 
    sentences = sent_tokenize(text)

    analyzer = SentimentIntensityAnalyzer() # NLTK sentiment init

    # Sentiment analysis. Calc sentence scores
    sentiment_scores = []
    for sentence in sentences:
        scores = analyzer.polarity_scores(sentence)
        score_tuple = (sentence, scores['compound'])
        sentiment_scores.append(score_tuple)

    # Sort the list of sentiment scores by the sentiment score
    sorted_scores = sorted(sentiment_scores, key=lambda x: x[1])

    # Start with exporting the output
    output_directory = r"C:\Users\Vaclav Barina\Documents\3. Study\2. Data Science\1. Fun Projects\2023_Earnings Transcript Sentiment\1. BYND Data and Analysis\3. Output"
    output_csv = output_directory + f"\{year}_sentence_sentiment_scores.csv" # Adds year to file path for clarity

    # Write the sorted_scores list to the CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['sentence', 'score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows({'sentence': sentence, 'score': score} for sentence, score in sorted_scores)

    print("CSV file exported successfully.")