import fasttext
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
# import nltk
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize
import streamlit as st

FASTTEXT_MODEL_PATH = "./cc.en.300.bin"

class FastTextSimilarity:
    def __init__(self):
        """
        Initialize the loader with the path to the FastText model.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.model_path = os.path.join(current_dir, "fine_tuned_model.bin")
        self.model = self.load_model()

    def load_model(self):
        """
        Load the pre-trained FastText model.
        """
        try:
            return fasttext.load_model(self.model_path)
        except Exception as e:
            raise ValueError(f"Failed to load FastText model: {str(e)}")

    def find_most_similar(self, target_word, word_list):
        """
        Find the most similar word to the target word from a list of words.

        :param target_word: The word for which similarity is calculated.
        :param word_list: List of words to compare.
        :return: Most similar word and its similarity score.
        """
        # Tokenize the target word
        tokens = target_word.split(' ')
        
        # Initialize variables to store the most similar word and highest similarity
        most_similar_word = None
        highest_similarity = -1

        for token in tokens[0]:
            target_vector = self.model.get_word_vector(token)
            word_vectors = [self.model.get_word_vector(word) for word in word_list]

            # Calculate cosine similarities
            similarities = cosine_similarity([target_vector], word_vectors)[0]

            # Find the word with the highest similarity for this token
            max_index = np.argmax(similarities)
            token_most_similar_word = word_list[max_index]
            token_highest_similarity = similarities[max_index]

            # Update the most similar word and highest similarity if this token's similarity is higher
            if token_highest_similarity > highest_similarity:
                most_similar_word = token_most_similar_word
                highest_similarity = token_highest_similarity

        return most_similar_word, highest_similarity
