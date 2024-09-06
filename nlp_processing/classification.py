from transformers import pipeline

def classify_disaster(text):
    classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')
    labels = ['flood', 'earthquake', 'wildfire', 'hurricane', 'pandemic','funny']
    result = classifier(text, candidate_labels=labels)
    return result
