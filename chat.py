import nltk
import re

import random
import string
import myP


from nltk.tokenize import word_tokenize

from string import punctuation

from PyQt5 import QtWidgets, uic

# descragar los modulos de stopwords de nltk
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('spanish'))


class Chat():
    conversation_history = []

    def __init__(self):
        pass

    def abrir_chat(self, user_input):

        # Tokenize the User Input
        user_input_tokenized = self.word_tokenizer(user_input)
        # quitar Stop Words
        user_input_nostops = self.remove_noise(user_input_tokenized)
        # proceso Query y generacion de respuesta

        chatbot_response = self.generate_response(
            user_input_nostops, user_input)
        # imprimir respuesta
        return chatbot_response
        # print('Chatbot:', chatbot_response)

    def sentence_tokenizer(self, data):
        #  Tokenizacion
        return nltk.sent_tokenize(data.lower())

    def word_tokenizer(self, data):
        # Function for Word Tokenization
        return nltk.word_tokenize(data.lower())

    def remove_noise(self, word_tokens):
        # funcion para remover stop words and punctuatcion
        cleaned_tokens = []
        for token in word_tokens:
            # token not in stop_words and
            if token not in punctuation:
                cleaned_tokens.append(token)
        return cleaned_tokens


# Function to generate response for the user input

    def generate_response(self, user_input_nostops, user_input):
        # Append User Input to chat history

        # Generate Random response

        # response = ' random.choice(response_definir(user_input))'
        cadenas = self.response_definir(cadenas=user_input_nostops)
        response = random.choice(cadenas[0])

        self.conversation_history.append({f"Tu: {user_input}" :f"ChatBot: {response}" })

        return response


# Main loop of chatbot

    def response_definir(self, cadenas):
        # print(cadenas)

        r = [response for pattern,
             response in myP.patrones if any(re.search(cadena, pattern) for cadena in cadenas)]

        if (len(r) == 0):
            r = [['Lo siento pero no puedo respoder la pregunta',
                  'Por favor, repite la pregunta nuevamente', 'No estoy seguro de tu pregunta.']]

        return r

        # return [response for pattern,
        #         response in patrones if re.search(cadenas, pattern)]
