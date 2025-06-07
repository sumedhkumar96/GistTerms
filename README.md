# 📄 GistTerms - Terms of Service Document Classifier

## 🔍 Overview  
**GistTerms** is an advanced **Natural Language Processing (NLP)** tool that analyzes Terms of Service (ToS) documents and classifies their contents into meaningful risk categories:

- 🔴 **Risk**: Potentially harmful or unfavorable to the user  
- 🟢 **Safe**: User-beneficial and protective statements  
- 🔵 **Information**: Neutral or purely informative content  

💡 The tool also assigns a **grade (A–F)** to the document based on its sentence classifications, making it easier for users to quickly assess service agreements.

---

## ✨ Features

- 🚩 **Risk Categorization** – Tags each sentence as **Risk**, **Safe**, or **Information**
- 🧮 **Document Grading** – Assigns an A–F score based on the ratio of risky to safe content
- 🧠 **Confidence Filtering** – Ignores low-confidence predictions to improve accuracy
- ♻️ **Deduplication** – Removes repetitive sentences for clean analysis

---

## 🛠️ Tech Stack

- **Language**: Python  
- **Libraries**:
  - NLP: `nltk`, `transformers`  
  - ML: `PyTorch`
- **Dataset**: [adeeteya/termsofservice](https://huggingface.co/datasets/adeeteya/termsofservice)  
- **Hardware**: CUDA support for GPU acceleration

---

## 🚀 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/sumedhkumar96/GistTerms.git
   cd GistTerms
   ```

2. **Create virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK tokenizer**  
   ```bash
   python -m nltk.downloader punkt
   ```

---

## 🧪 Usage

1. **Add your ToS document**  
   - Save your `.txt` file as `input.txt` in the project directory

2. **Run the classifier**  
   ```bash
   python final_program.py
   ```

3. **Get results in terminal**  
   Example output:  
   ```plaintext
   Classified Sentences:

   🔴 Risk:
     - "The service reserves the right to terminate accounts without notice." (Confidence: 0.85)

   🟢 Safe:
     - "Users can request data deletion at any time." (Confidence: 0.90)

   🔵 Information:
     - "The service uses cookies to improve functionality." (Confidence: 0.75)

   🏅 Service Grade: B
   ```

---

## ⚙️ How It Works

1. **Sentence Tokenization** – Splits input using NLTK  
2. **Preprocessing** – Tokenizes and formats sentences for model input  
3. **Classification** – Uses fine-tuned BERT to categorize content  
4. **Grading** – Computes document grade based on sentence types  

---

## 🛤️ Roadmap

- [ ] 🌐 Build a web UI for document upload and visual results  
- [ ] 📄 Add support for PDF and DOCX formats  
- [ ] 🤖 Improve accuracy via larger datasets  
- [ ] 📊 Integrate feedback system for live improvements  

---

## 🤝 Contributing

We welcome contributions!  

1. Fork the repo  
2. Create a new branch  
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes  
   ```bash
   git commit -m "Add new feature"
   ```
4. Push and open a PR  
   ```bash
   git push origin feature-name
   ```

---

## 📜 License  
Licensed under the [MIT License](LICENSE).
