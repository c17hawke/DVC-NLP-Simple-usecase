## REFERENCE https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html


from sklearn.feature_extraction.text import CountVectorizer
# corpus = [
#     "Zebra apple ball cat cat",
#     "ball cat dog elephant",
#     "very very unique"
# ]

corpus = [
    "apple ball cat",
    "ball cat dog",
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
# print(vectorizer.get_feature_names_out())


# print(X.toarray())

max_features = 100 ## no of words you want to consider 
ngrams = 3 ## pair of words you want to consider

vectorizer2 = CountVectorizer(max_features=max_features, ngram_range=(1, ngrams))
X2 = vectorizer2.fit_transform(corpus)

print(vectorizer2.get_feature_names_out())

print(X2.toarray())

# vectorizer2 = CountVectorizer(stop_words="english", max_features=max_features, ngram_range=(1, ngrams))
# X2 = vectorizer2.fit_transform(corpus)

# print(vectorizer2.get_feature_names_out())

# print(X2.toarray())