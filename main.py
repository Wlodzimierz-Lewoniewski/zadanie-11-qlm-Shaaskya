import math
from collections import Counter

def tokenize(text):
    return text.lower().replace(',', '').replace('.', '').split()


def compute_smoothed_probability(doc_tokens, query_tokens, all_terms, lambda_):
    doc_count = Counter(doc_tokens)
    all_terms_size = len(all_terms)
    doc_length = len(doc_tokens)
    all_terms_count = Counter(token for doc in documents for token in tokenize(doc))

    probability = 0
    for token in query_tokens:
        word_prob = doc_count.get(token, 0) / doc_length
        all_terms_prob = all_terms_count.get(token, 0) / all_terms_size
        smoothing = lambda_ * all_terms_prob + (1 - lambda_) * word_prob
        probability += smoothing if smoothing > 0 else 0 
    return probability


def rank_documents(documents, query, lambda_):

    query_tokens = tokenize(query)
    all_terms = set(token for doc in documents for token in tokenize(doc))
    
    scores = []
    for idx, doc in enumerate(documents):
        doc_tokens = tokenize(doc)
        score = compute_smoothed_probability(doc_tokens, query_tokens, all_terms, lambda_)
        scores.append((idx, score))

    scores.sort(key=lambda x: (-x[1], x[0]))

    sorted_indices = [idx for idx, _ in scores]
    
    return sorted_indices


if __name__ == "__main__":

    n = int(input())
    documents = [input().strip() for _ in range(n)]
    query = input()
    ranked_documents = rank_documents(documents, query, lambda_=0.5)

    print(ranked_documents)
