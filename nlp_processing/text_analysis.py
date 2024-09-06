import nltk
from transformers import pipeline

nltk.download('punkt')

def extract_named_entities(text):
    # Pre-trained BERT model for Named Entity Recognition (NER)
    ner_pipeline = pipeline("ner")
    entities = ner_pipeline(text)
    return entities

def sentiment_analysis(text):
    # Using a pre-trained sentiment analysis model
    sentiment_pipeline = pipeline("sentiment-analysis")
    return sentiment_pipeline(text)
