import os
import json
import re
import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

def create_phrase_dictionary(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

        # Split the text into phrases using periods and commas
        phrases = re.split(r'[.,]', text)

        # Remove leading and trailing whitespace from each phrase
        phrases = [phrase.strip() for phrase in phrases if phrase.strip()]

        # Check if there are any phrases before creating the dictionary
        if not phrases:
            print("No phrases found in the text.")
            return {}

        return phrases
    except Exception as e:
        print(f"Error reading the file: {str(e)}")
        return {}

def get_document(data):
    settings = data["settings"]
    path = settings.get("path", "")
    document = settings.get("documents", "")
    file_path = os.path.join(path, document)
    result = create_phrase_dictionary(file_path)
    return result

def process_form_data_with_model(data):
    documents = get_document(data)

    if not documents:
        print("Error: No valid documents to process.")
        return

    try:
        tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        model = BertModel.from_pretrained("bert-base-uncased")

        # Tokenize and encode the documents
        document_embeddings = []
        for document in documents:
            inputs = tokenizer(document, return_tensors="pt", padding=True, truncation=True)
            outputs = model(**inputs)
            document_embedding = outputs.last_hidden_state.mean(dim=1)  # Average over tokens
            document_embeddings.append(document_embedding)
        document_embeddings = torch.cat(document_embeddings)

        user_query = data["word"]

        user_query_inputs = tokenizer(user_query, return_tensors="pt", padding=True, truncation=True)
        user_query_outputs = model(**user_query_inputs)
        user_query_embedding = user_query_outputs.last_hidden_state.mean(dim=1)

        # Calculate cosine similarity between the user query and all documents
        similarities = cosine_similarity(user_query_embedding.detach().numpy(), document_embeddings.detach().numpy())

        # Find the index of the most similar document
        most_similar_document_index = similarities.argmax()

        most_similar_document = documents[most_similar_document_index]
        print(documents)
        print("Most similar document:", most_similar_document)
    except Exception as e:
        print(f"Error processing data with the model: {str(e)}")

if __name__ == "__main__":
    try:
        data2 = {
            'word': "Amidst the expansive canvas of modern art,",
            'settings': {
                'path': r"C:\Users\seqqal\Documents\GitHub\Projects\MoteurRecherche",
                'documents': "artical.txt"
            }
        }
        # Process the form data
        process_form_data_with_model(data2)

        # Optionally, print a success message
        print("Form Data Processing Successful")

    except Exception as e:
        # Handle errors
        print("Error:", str(e))
