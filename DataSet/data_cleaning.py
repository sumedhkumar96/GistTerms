import os
import re

def clean_terms_of_service(file_path):
    """
    Cleans the text document to retain only the Terms of Service content.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Remove common irrelevant sections (e.g., menus, headers, navigation links)
    text = re.sub(r"(Subscribe|Sign In|Navigation|Menu|Home|Create an Account|FAQs).*", "", text, flags=re.IGNORECASE)
    
    # Remove HTML tags and entities
    text = re.sub(r"<[^>]+>", " ", text)  # Remove HTML tags
    text = re.sub(r"&[a-z]+;", " ", text)  # Remove HTML entities
    
    # Remove special characters and unnecessary whitespace
    text = re.sub(r"[^\w\s.,?!@'\"-]", " ", text)  # Non-alphanumeric except common punctuation
    text = re.sub(r"\s+", " ", text)  # Collapse multiple spaces
    
    # Remove redundant lines
    lines = text.splitlines()
    clean_lines = []
    seen_lines = set()
    for line in lines:
        line = line.strip()
        if line and line.lower() not in seen_lines:
            clean_lines.append(line)
            seen_lines.add(line.lower())  # Normalize to avoid duplicates
    
    # Join cleaned lines
    return "\n".join(clean_lines)

def process_corpus(input_dir, output_dir):
    """
    Process all text files in a directory to clean them and save cleaned versions.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            cleaned_text = clean_terms_of_service(input_path)
            
            # Save the cleaned content
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(cleaned_text)

# Example usage
input_directory = "tos"
output_directory = "cleaned_tos"

process_corpus(input_directory, output_directory)
print("Corpus cleaned and saved successfully.")