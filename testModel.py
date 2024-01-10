import torch
from transformers import BertTokenizer, BertModel

# loading the model with vocabulary
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


text = "Here is the sentence I want embeddings for."
marked_text = "[CLS] " + text + " [SEP]"

# tokenizing the text
tokenized_text = tokenizer.tokenize(marked_text)
print(tokenized_text)

