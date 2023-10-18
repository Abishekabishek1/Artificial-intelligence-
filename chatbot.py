
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

file_path = 'Data.txt'
pattern_responses = {}

try:
    with open(file_path, 'r') as file:
        for line in file:
            pattern, response = line.strip().split('\t')
            pattern_responses[re.compile(r'\b' + re.escape(pattern) + r'\b')] = response
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()
except PermissionError:
    print(f"Error: You don't have permission to access '{file_path}'.")
    exit()
except Exception as e:
    print(f"Error: An unexpected error occurred - {e}")
    exit()

def preprocess_input(input_text):
    words = word_tokenize(input_text.lower())
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    filtered_words = [ps.stem(word) for word in words if word.isalnum() and word not in stop_words]
    processed_input = ' '.join(filtered_words)
    return processed_input

def generate_response(user_input):
    processed_input = preprocess_input(user_input)
    response = "I'm sorry, I don't understand that."
    for pattern in pattern_responses.keys():
        if pattern.search(processed_input):
            response = pattern_responses[pattern]
            break
    return response

while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    else:
        bot_response = generate_response(user_input)
        print("Chatbot:", bot_response)
