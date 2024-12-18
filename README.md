# Terms of Service Document Classifier

## Overview
The Terms of Service Document Classifier is an advanced Natural Language Processing (NLP) project designed to analyze Terms of Service (ToS) documents. It identifies and categorizes sentences based on their content and risk level:

- **Risk**: Statements that could be potentially harmful or unfavorable to the user.
- **Safe**: Statements that ensure user rights or are considered safe.
- **Information**: Neutral or informative statements.

This tool grades the overall document based on the number of risky and safe sentences, providing users with an intuitive service grade (A to F) to quickly assess the document.

---

## Features
- **Risk Categorization**: Automatically classifies sentences into Risk, Safe, or Information categories.
- **Document Grading**: Assigns an overall grade to the document based on risk and safety levels.
- **Confidence Filtering**: Filters out sentences with low classification confidence to ensure reliability.
- **Deduplication**: Removes duplicate sentences for accurate analysis.

---

## Tech Stack
- **Programming Languages**: Python
- **Libraries/Frameworks**:
  - Natural Language Processing: `nltk`, `transformers`
  - Machine Learning: `PyTorch`
- **Pre-trained Model**: [adeeteya/distilbert_base_uncased_finetuned_tos](https://huggingface.co/adeeteya/distilbert_base_uncased_finetuned_tos) (BERT-based model fine-tuned for ToS classification)
- **Dataset**: [adeeteya/termsofservice](https://huggingface.co/datasets/adeeteya/termsofservice)
- **Hardware Support**: Supports CUDA for GPU acceleration

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pallavibakale/CS-59000-NLP-Final-Project.git
   cd CS-59000-NLP-Final-Project
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the NLTK tokenizer:**
   ```bash
   python -m nltk.downloader punkt
   ```

---

## Usage

1. **Prepare the input document:**
   Ensure the ToS document is in `.txt` format and named `input.txt`.

2. **Run the classifier:**
   ```bash
   python final_program.py
   ```

3. **View the output:**
   The script will:
   - Print the categorized sentences (Risk, Safe, Information) with their confidence scores.
   - Display the overall grade of the document based on its risk level.

   Example output:
   ```plaintext
   Classified Sentences:

   Risk:
     - "The service reserves the right to terminate accounts without notice." (Confidence: 0.85)

   Safe:
     - "Users can request data deletion at any time." (Confidence: 0.90)

   Information:
     - "The service uses cookies to improve functionality." (Confidence: 0.75)

   Service Grade: B
   ```

---

## Alternate Usage

### Use the Model Directly

#### Using a Pipeline Helper
```python
from transformers import pipeline

pipe = pipeline("text-classification", model="adeeteya/distilbert_base_uncased_finetuned_tos")
result = pipe("Your sentence here.")
print(result)
```

#### Loading the Model and Tokenizer
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("adeeteya/distilbert_base_uncased_finetuned_tos")
model = AutoModelForSequenceClassification.from_pretrained("adeeteya/distilbert_base_uncased_finetuned_tos")

inputs = tokenizer("Your sentence here.", return_tensors="pt")
outputs = model(**inputs)
print(outputs)
```

---

## How It Works

1. **Sentence Tokenization**: The document is split into individual sentences using NLTK's tokenizer.
2. **Preprocessing**: Each sentence is tokenized and prepared for the BERT model.
3. **Classification**: Sentences are classified into Risk, Safe, or Information categories based on the fine-tuned BERT model.
4. **Grading**: The document is graded based on the count of Risk and Safe sentences.

---

## Roadmap
- [ ] Develop a user-friendly web interface for document uploads and visual results.
- [ ] Add support for additional file formats (e.g., PDF, DOCX).
- [ ] Improve classification accuracy by fine-tuning with larger datasets.
- [ ] Integrate real-time feedback for model improvements.

---

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch.
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes.
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch.
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
**Aditya Ramesh**  
[Email](mailto:adeeteya@gmail.com) | [GitHub](https://github.com/adeeteya)

**Sumedh Kumar**  
[Email](mailto:sumedhkumar96@gmail.com) | [GitHub](https://github.com/sumedhkumar96)

**Pallavi Bakale**  
[Email](mailto:pallavib0996@gmail.com) | [GitHub](https://github.com/pallavibakale)