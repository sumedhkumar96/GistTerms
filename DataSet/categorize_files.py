import csv
import os
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

# Sample keywords for classification
RISK_KEYWORDS = {
    "Positive Point": [
        "we will not","encrypt user data", "we do not sell your data", "data anonymization practices",
        "user control over data", "right to access your data", "complies with GDPR",
        "allows data deletion upon request", "data breach notifications", 
        "transparent data processing policies", "we respect your privacy",
        "opt-in required for marketing", "offer secure communication",
        "protect your data with SSL", "third-party access is limited",
        "no sharing without user consent", "provide data portability options",
        "store data within secure facilities", "audit and compliance standards"
    ],
    "High Risk": [
        "share with third parties", "sell your data", "retain indefinitely", "no liability",
        "collect personal information", "may disclose your data", "at your own risk",
        "we are not responsible", "waive your rights", "binding arbitration",
        "unilateral termination", "subject to change without notice", "you agree to indemnify",
        "third-party advertising", "may use your data for marketing", "without your consent",
        "tracking your activity", "location tracking without permission", "no refunds",
        "transfer your data", "access your data for any purpose", "perpetual license",
        "automatic renewal of subscription", "user responsibility for data breaches"
    ],
    "Low Risk": [
        "may collect anonymized data", "use cookies to track", "may use your data",
        "data retention policy", "requires opt-out", "store usage data", 
        "contact us for data deletion", "share with affiliates", "may use analytics tools",
        "aggregated data may be shared", "data processed outside your country",
        "may send promotional emails", "retain data for compliance", "user-generated content",
        "data used for improving services", "your responsibility to review updates",
        "service disruptions", "no guarantees of service availability"
    ]
}

def classify_sentence(sentence):
    """
    Classify a sentence into High Risk, Low Risk, or Positive Points
    """
    sentence_lower = sentence.lower()
    for risk_level, keywords in RISK_KEYWORDS.items():
        if any(keyword in sentence_lower for keyword in keywords):
            return risk_level
    return None

def analyze_document(file_path):
    """
    Analyze a document and categorize sentences.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Tokenize into sentences
    sentences = sent_tokenize(text)
    
    # Categorize sentences
    results = []
    for sentence in sentences:
        # Avoid sentences that are too short or incorrectly split
        if len(sentence.split()) < 3:  
            continue
        category = classify_sentence(sentence)
        if category:  # Only include classified sentences
            results.append((sentence.strip(), category))
    
    return results

def process_corpus_to_csv(input_dir, output_csv):
    """
    Process all cleaned documents, classify sentences, and save them into a CSV file.
    Removes duplicate sentences across files.
    """
    seen_sentences = set()
    rows = []
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_dir, filename)
            classified_sentences = analyze_document(input_path)
            
            for sentence, label in classified_sentences:
                if sentence not in seen_sentences:  # Avoid duplicates
                    rows.append((sentence, label))
                    seen_sentences.add(sentence)
    
    # Write to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Sentence", "Label"])  # Header
        writer.writerows(rows)

def process_corpus_to_txt(input_dir, output_dir):
    """
    Process all cleaned documents and save categorized results.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            categorized = analyze_document(input_path)

            if categorized:
                high_risks = [sentence for sentence, category in categorized if category == "High Risk"]
                low_risks = [sentence for sentence, category in categorized if category == "Low Risk"]
                positive_points = [sentence for sentence, category in categorized if category == "Positive Point"]
                # Save categorized output
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(f"High Risk:\n")
                    for sentence in high_risks:
                        output_file.write(f"  - {sentence}\n")
                    output_file.write("\n")
                    output_file.write(f"Low Risk:\n")
                    for sentence in low_risks:
                        output_file.write(f"  - {sentence}\n")
                    output_file.write("\n")
                    output_file.write(f"Positive Point:\n")
                    for sentence in positive_points:
                        output_file.write(f"  - {sentence}\n")
                    output_file.write("\n")

# Example usage
input_directory = "cleaned_tos"
output_directory = "categorized_tos"
output_csv = "tos.csv"

process_corpus_to_csv(input_directory, output_csv)
process_corpus_to_txt(input_directory, output_directory)
print("Documents analyzed and categorized successfully.")
