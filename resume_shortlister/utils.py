import fitz
import spacy

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = " ".join(page.get_text() for page in doc)
    
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    filtered_tokens = [token.lemma_ for token in doc if token.is_alpha]
    return " ".join(filtered_tokens)

def chunk_text(text, size=800):
    return [text[i:i+size] for i in range(0, len(text), size)]
