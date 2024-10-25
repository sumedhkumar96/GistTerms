import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import os

# Download NLTK data files if not already downloaded
# nltk.download()
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Function to preprocess a single T&C document
def preprocess_text(text):
    # 1. Lowercasing
    text = text.lower()

    # 2. Preserving common abbreviations using regex
    abbreviations = r'(?:u\.s\.|u\.k\.|ltd\.|inc\.|e\.g\.|i\.e\.)'
    text = re.sub(abbreviations, lambda x: x.group(0).upper(), text)  # Temporarily uppercase them for protection

    # 3. Removing unwanted punctuation (except periods in abbreviations, commas, and dashes)
    text = re.sub(r'[^\w\s,.]', '', text)  # Keep only words, spaces, commas, and periods

    # 4. Tokenization
    tokens = word_tokenize(text)

    # 5. Removing stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # 6. Lemmatization (convert words to their base form)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # 7. Rejoining tokens into a cleaned string
    preprocessed_text = ' '.join(tokens)

    # 8. Restoring abbreviations (make them lowercase again)
    preprocessed_text = re.sub(r'(U\.S\.|U\.K\.|LTD\.|INC\.|E\.G\.|I\.E\.)', lambda x: x.group(0).lower(), preprocessed_text)

    return preprocessed_text

# Function to read from input file and write preprocessed data to a new file
def preprocess_file(input_file):
    # Get the base name and extension of the input file
    base_name, ext = os.path.splitext(input_file)
    
    # Define the output file name with "_processed" added before the file extension
    output_file = f"{base_name}_processed{ext}"
    
    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Preprocess the text
    processed_text = preprocess_text(text)

    # Write the processed text into a new file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(processed_text)
    
    print(f"Preprocessed text has been written to {output_file}")

# Example usage: Provide the input file name
# input_file = 'D:\Purdue docs\Courses\NLP\Project\DataSet\text\1Password_TermsofService.txt'  # Replace with your file
preprocess_file("ALCPU_PrivacyPolicy.txt")
