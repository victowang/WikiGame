import spacy
nlp = spacy.load('en_core_web_lg')

def getMaxSimilarity(current, end):
    tokens1 = nlp(end)
    tokens2 = nlp(current)

    max_similarity = 0
    for token1 in tokens1:
        for token2 in tokens2:
            similarity = token1.similarity(token2)
            #print(">>>", token1.text, token2.text, similarity)
            if similarity >= max_similarity:
                max_similarity = similarity
    return max_similarity

def getMeanSimilarity(current, end):
    tokens1 = nlp(end)
    tokens2 = nlp(current)

    similarity = 0
    i = 0
    for token1 in tokens1:
        for token2 in tokens2:
            i += 1
            similarity += token1.similarity(token2)
    return similarity/i

if __name__ == "__main__":
    print(getSimilarity("International Standard Book Number", "Cat"))