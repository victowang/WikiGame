import spacy
nlp = spacy.load('en_core_web_lg')

def getSimilarity(current, end):
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

if __name__ == "__main__":
    print(getSimilarity("International Standard Book Number", "Cat"))