# 🔍 Semantic Search Engine Using Sentence Embeddings

This project demonstrates a semantic search engine that compares the performance of traditional keyword-based retrieval (TF-IDF) with two transformer-based sentence embedding models — **Sentence-BERT** and **MiniLM**.

Users can upload a dataset (`.txt` or `.csv`) via a web interface and run queries. The app displays and compares the **top 5 most relevant documents** returned by each model, along with a bar chart visualization of similarity scores.

---

## 🚀 Features

- ✅ Parallel comparison of **TF-IDF**, **Sentence-BERT**, and **MiniLM**
- ✅ Upload support for `.txt` and `.csv` datasets
- ✅ Interactive query input
- ✅ Visual cosine similarity chart with `Result 1`, `Result 2`, etc.
- ✅ Easy-to-run Streamlit interface

---

## 🧠 Models Used

| Model          | Description |
|----------------|-------------|
| **TF-IDF**     | Traditional keyword-based vectorizer using term frequency and inverse document frequency |
| **Sentence-BERT** | Transformer model that generates context-aware sentence embeddings |
| **MiniLM**     | Lightweight, faster transformer model that maintains strong semantic understanding |

All models use **cosine similarity** for query-to-document ranking.

---

## 📂 Folder Structure

semantic-search-engine/
├── src/
│ ├── app.py # Main Streamlit app
│ ├── fetch_wikipedia.py # (Optional) script to scrape Wikipedia summaries
│ └── data/ # Place uploaded or preprocessed data here
├── README.md
└── requirements.txt

yaml
Copy code

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/semantic-search-engine.git
cd semantic-search-engine
Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
▶️ Usage
Run the Streamlit app:

bash
Copy code
streamlit run src/app.py
Then open the URL that appears (typically http://localhost:8501) in your browser.

📊 Sample Queries
Try queries like:

"impact of artificial intelligence on society"

"how to handle memory leak in Python"

"transfer learning for climate forecasting"

These help observe how semantic models outperform TF-IDF on abstract or complex queries.

📚 Datasets
You can use any .txt (one doc per line) or .csv file (select text column). Example sources:

Wikipedia summaries (fetch_wikipedia.py)

StackOverflow questions

Abstracts from academic papers

🧪 Evaluation Metrics (optional)
Cosine Similarity: Used to rank relevance of each document to query

Future work: Add Precision@K, Recall, or NDCG if labeled data is available

🙌 Authors
Sachin John — s.john@student.xu-university.de

Sooraj Manayath Mathew — s.mathew@student.xu-university.de

Melvin Mathew — m.mathew@student.xu-university.de

📜 License
This project is licensed for academic use under MIT License.

❤️ Contributions
Feel free to open issues or pull requests to suggest improvements, add features, or optimize performance.
