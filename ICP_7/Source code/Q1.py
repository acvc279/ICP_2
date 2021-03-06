from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
twentytrain = fetch_20newsgroups(subset='train', shuffle=True)
#vectorizer
tfidf = TfidfVectorizer()
tfidf_V1 = TfidfVectorizer(ngram_range=(1, 2))
tfidf_V2 = TfidfVectorizer(stop_words='english')
#fit model testing
X_traintfidf = tfidf.fit_transform(twentytrain.data)
X_traintfidf1 = tfidf_V1.fit_transform(twentytrain.data)
X_traintfidf2 = tfidf_V2.fit_transform(twentytrain.data)
#MultinomialNB
c = MultinomialNB()
c.fit(X_traintfidf, twentytrain.target)
c1 = MultinomialNB()
c1.fit(X_traintfidf1, twentytrain.target)
c2 = MultinomialNB()
c2.fit(X_traintfidf2, twentytrain.target)
#Test Train
twentytest = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf.transform(twentytest.data)
pred = c.predict(X_test_tfidf)
#Finding MultinomialB accuracy
s = round(metrics.accuracy_score(twentytest.target, pred), 4)
print("MultinomialNB accuracy: ", s)
twentytest1 = fetch_20newsgroups(subset='test', shuffle=True)
X_testtfidf1 = tfidf_V1.transform(twentytest.data)
pred1 = c1.predict(X_testtfidf1)
#Finding MultinomialB accuracy when using bigram
s1 = round(metrics.accuracy_score(twentytest1.target, pred1), 4)
print("MultinomialNB accuracy on bigram: ", s1)
twentytest2 = fetch_20newsgroups(subset='test', shuffle=True)
X_testtfidf2 = tfidf_V2.transform(twentytest.data)
pred2 = c2.predict(X_testtfidf2)
#Finding MultinomialB accuracy when adding stopwords
s2 = round(metrics.accuracy_score(twentytest2.target, pred2), 4)
print("MultinomialNB accuracy when adding the stopwords: ", s2)
#Support vector Machine to see accuracy
svc = svm.SVC(kernel='linear')
svc.fit(X_traintfidf, twentytrain.target)
acc = svc.score(X_traintfidf, twentytrain.target)
print("SVC accuracy:", acc)
