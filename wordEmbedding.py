import numpy as np

# Définition d'un vocabulaire de mots
vocab = {'apple', 'banana', 'orange', 'grape', 'kiwi'}

# Initialisation aléatoire des embeddings pour chaque mot
embedding_size = 5
word_embeddings = {}
for word in vocab:
    word_embeddings[word] = np.random.rand(embedding_size)

# Fonction de similarité cosinus
def cosine_similarity(embedding1, embedding2):
    dot_product = np.dot(embedding1, embedding2)
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)
    return dot_product / (norm1 * norm2)

# Fonction pour trouver les mots similaires
def find_similar_words(query_word, embeddings, top_n=3):
    query_embedding = embeddings[query_word]
    similarities = {}
    for word, embedding in embeddings.items():
        similarities[word] = cosine_similarity(query_embedding, embedding)
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    similar_words = [word for word, _ in sorted_similarities[1:top_n+1]]  # Exclude the query word itself
    return similar_words

# Test pour trouver les mots similaires à "apple"
query_word = 'apple'
similar_words = find_similar_words(query_word, word_embeddings)
print(word_embeddings)
print(f"Words similar to '{query_word}': {similar_words}")
