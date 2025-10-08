from flask import Flask, request, render_template, redirect
import pandas as pd
from sentence_transformers import SentenceTransformer, util
from datasets import load_dataset
from collections import Counter
import csv
import os

app = Flask(__name__)

# Load SBERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load Amazon product data (5% for speed)
dataset = load_dataset("Ateeqq/Amazon-Product-Description", split="train[:5%]")
df = dataset.to_pandas()[['TITLE', 'DESCRIPTION']].dropna().reset_index(drop=True)
df['DESCRIPTION'] = df['DESCRIPTION'].astype(str)
df['embeddings'] = df['DESCRIPTION'].map(lambda x: model.encode(x, convert_to_tensor=True))

# Load user feedback
def load_feedback():
    if not os.path.exists('feedback.csv'):
        return Counter()
    feedback_df = pd.read_csv('feedback.csv', header=None, names=['TITLE', 'DESCRIPTION', 'VOTE'])
    score_map = Counter()
    for _, row in feedback_df.iterrows():
        score_map[row['TITLE']] += 1 if row['VOTE'] == 'up' else -1
    return score_map

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        query_emb = model.encode(query, convert_to_tensor=True)
        sims = [util.cos_sim(query_emb, emb).item() for emb in df['embeddings']]
        df['similarity'] = sims

        score_map = load_feedback()
        df['adjusted_similarity'] = df.apply(
            lambda row: row['similarity'] + 0.05 * score_map.get(row['TITLE'], 0), axis=1
        )

        top_matches = df.sort_values('adjusted_similarity', ascending=False).head(5)
        results = top_matches[['TITLE', 'DESCRIPTION', 'similarity']].to_dict(orient='records')

    return render_template('index.html', results=results)

@app.route('/feedback', methods=['POST'])
def feedback():
    title = request.form['title']
    desc = request.form['description']
    vote = request.form['vote']  # 'up' or 'down'

    with open('feedback.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([title, desc, vote])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)