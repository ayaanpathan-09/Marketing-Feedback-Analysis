from __future__ import annotations
import re
from collections import Counter

STOPWORDS = {
    "the","and","for","that","this","with","was","are","but","you","your","our","have",
    "had","has","from","they","them","its","very","not","too","can","could","would",
    "will","about","after","before","when","what","where","how","into","just","more",
    "than","then","there","their","product","campaign","service","marketing","because",
    "been","were","all","one","also","get","got","use","used","using","out","my","we",
    "it","is","to","of","in","on","a","an","i","me","at","as","if","so","do","did"
}

def top_keywords(texts, limit=15):
    words = []
    for text in texts:
        words.extend(re.findall(r"[a-zA-Z][a-zA-Z'-]{2,}", str(text).lower()))
    counts = Counter(w.strip("'-") for w in words if w not in STOPWORDS and len(w.strip("'-")) > 2)
    return counts.most_common(limit)
