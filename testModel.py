import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

documents = [
    'inviting viewers to participate in immersive experiences that transcend the limitations of physical space',
    'urging us to confront the complexities of our shared humanity',
    'Contemporary artists grapple with pressing socio-political issues', 'inviting us to explore',
    'interactive sculptures',
    'a symphony of diverse voices and perspectives converges to create a rich and nuanced narrative that mirrors the complexities of our modern existence',
    'where tradition and innovation engage in a perpetual dance', 'artists navigate a spectrum of styles',
    'embracing new mediums and technologies that propel creative expression into uncharted territories',
    'and appreciate the boundless possibilities that arise when creativity knows no limits',
    'The kaleidoscopic array of styles', 'In the vast tapestry of contemporary art',
    'each a unique brushstroke contributing to the canvas of cultural evolution', 'In this ever-evolving dialogue',
    'addressing themes of identity', 'and digital art redefine the boundaries of the traditional gallery',
    'As the global landscape shifts', 'inequality',
    'The democratization of art through online platforms and social media further amplifies the reach and impact of artistic endeavors',
    'question', 'so too does the language of art', 'mediums', 'pushing boundaries and challenging preconceptions',
    'The art world serves as a dynamic crucible',
    'fostering a global conversation that transcends geographical confines', 'and empathy',
    'and messages converges to form a vibrant tapestry that speaks to the multifaceted nature of the human experience',
    'art becomes a powerful catalyst for reflection',
    'From the visceral strokes of abstract expressionism to the meticulous details of hyperrealism', 'provocation',
    'Virtual reality installations', 'and environmental stewardship']
# Tokenize and encode the documents
document_embeddings = []
for document in documents:
    inputs = tokenizer(document, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    document_embedding = outputs.last_hidden_state.mean(dim=1)  # Average over tokens
    document_embeddings.append(document_embedding)
document_embeddings = torch.cat(document_embeddings)

user_query = "Encouraging observers to engage in interactive encounters that go beyond the constraints of the physical environment, providing an opportunity for a deeply involving and expansive experience that extends beyond the conventional boundaries of space."

user_query_inputs = tokenizer(user_query, return_tensors="pt", padding=True, truncation=True)
user_query_outputs = model(**user_query_inputs)
user_query_embedding = user_query_outputs.last_hidden_state.mean(dim=1)

# Calculate cosine similarity between the user query and all documents
similarities = cosine_similarity(user_query_embedding.detach().numpy(), document_embeddings.detach().numpy())

# Find the index of the most similar document
most_similar_document_index = similarities.argmax()

most_similar_document = documents[most_similar_document_index]
print("Most similar document:", most_similar_document)
