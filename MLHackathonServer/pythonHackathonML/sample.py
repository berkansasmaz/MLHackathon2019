import numpy as np # linear algebra
import pandas as pd 



data = pd.read_csv('hepsiBurada.csv',encoding ='utf-16', sep='|', error_bad_lines=False)
data.head()
data= data.dropna()
data['Duygu'] = 1
data.Duygu.iloc[222:] = 0





data.tail(10)

data.info()
data.describe()
def remove_stopwords(df_fon):
    stopwords = open('turkce-stop-words', 'r').read().split()
    df_fon['stopwords_removed'] = list(map(lambda doc:
        [word for word in doc if word not in stopwords], df_fon['Yorum']))

remove_stopwords(data)

x = data.Yorum.values

y = data.Duygu.values

print(x)
print(len(x))



from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=42)


veri = x.copy()

veri.shape


from nltk.corpus import stopwords
stop = stopwords.words("turkish")

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=5,stop_words=stop,ngram_range=(1,3))
vectorizer.fit(veri)


BoW = vectorizer.transform(veri)
repr(BoW)

feature_names = vectorizer.get_feature_names()
print("100 ile 110 arasındaki değerler:\n{}".format(feature_names[100:110]))

from sklearn.feature_extraction.text import TfidfVectorizer
for min_df in [1,2,3,4,5,6]:
    for n_gram in [(1,1),(1,2),(1,3),(2,3)]:
        tf_vectorizer = TfidfVectorizer(min_df=min_df, stop_words=stop,ngram_range=n_gram)
        veri1 = tf_vectorizer.fit_transform(veri)
        best = veri1.max(axis=0).toarray().ravel()
        sort_by_tfidf = best.argsort()
        feature_names = np.array(tf_vectorizer.get_feature_names())
        print("Vocabularies using min_df={} and n_gram={} with highest tfidf: \n{}".format(min_df, n_gram, feature_names[sort_by_tfidf[-20:]]))
        print("The number of vocabularies: {}".format(len(tf_vectorizer.vocabulary_)))
        sort_by_tfidf = np.argsort(tf_vectorizer.idf_)
        print("Vocabularies with lowest idf:\n{}".format(feature_names[sort_by_tfidf[:20]]))
        print('-----------------------------------')
        
        
        
        
        
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier




from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import f1_score



from sklearn.pipeline import Pipeline
LinearSVC_count = Pipeline([
    ('countvectorizer',CountVectorizer()),
    ('LinearSVC',LinearSVC(max_iter=1000))
])

LinearSVC_tfidf = Pipeline([
        ('tfidfvectorizer', TfidfVectorizer()),
        ('LinearSVC', LinearSVC(max_iter=1000))
])
    
    
LinearSVC_count = Pipeline([
    ('countvectorizer',CountVectorizer()),
    ('LinearSVC',LinearSVC(max_iter=1000))
])

LinearSVC_tfidf = Pipeline([
        ('tfidfvectorizer', TfidfVectorizer()),
        ('LinearSVC', LinearSVC(max_iter=1000))
])
    
    
    
    
Naive_count = Pipeline([
        ('countvectorizer', CountVectorizer()),
        ('multinomialnb', MultinomialNB())
])

Naive_tfidf = Pipeline([
        ('tfidfvectorizer', TfidfVectorizer()),
        ('multinomialnb', MultinomialNB())
])
    
  
Decision_count = Pipeline([
        ('countvectorizer', CountVectorizer()),
        ('decisiontreeclassifier', DecisionTreeClassifier())
])

Decision_tfidf = Pipeline([
        ('tfidfvectorizer', TfidfVectorizer()),
        ('decisiontreeclassifier', DecisionTreeClassifier())
])

RandomForest_count = Pipeline([
        ('countvectorizer', CountVectorizer()),
        ('randomforestclassifier', RandomForestClassifier(n_estimators=100))
])

RandomForest_tfidf = Pipeline([
        ('tfidfvectorizer', TfidfVectorizer()),
        ('randomforestclassifier', RandomForestClassifier(n_estimators=100))
])
    
    
parameters_of_svc_count = [ 
    {
        'LinearSVC__C': [0.01, 0.1, 1, 10, 100], 
        'countvectorizer__min_df': [1,3,5], 
        'countvectorizer__stop_words': [None, stop],
        'countvectorizer__ngram_range': [(1, 1), (1, 2), (1, 3), (2, 3)]
    } 
]


parameters_general_count = [ 
    {
        'countvectorizer__min_df': [1,3,5], 
        'countvectorizer__stop_words': [None, stop],
        'countvectorizer__ngram_range': [(1, 1), (1, 2), (1, 3), (2, 3)]
    }
]

parameters_of_svc_tfidf = [ 
    {
        'LinearSVC__C': [0.01, 0.1, 1, 10, 100], 
        'tfidfvectorizer__min_df': [1,3,5], 
        'tfidfvectorizer__stop_words': [stop],
        'tfidfvectorizer__ngram_range': [(1, 1), (1, 2), (1, 3), (2, 3)]
    } 
]

parameters_of_general_tfidf = [ 
    {
        'tfidfvectorizer__min_df': [1,3,5], 
        'tfidfvectorizer__stop_words': [stop],
        'tfidfvectorizer__ngram_range': [(1, 1), (1, 2), (1, 3), (2, 3)]
    }
]

x_train.shape




for models, parameters, name in zip([LinearSVC_count, Naive_count, Decision_count, RandomForest_count],
                                    [parameters_of_svc_count, parameters_general_count, parameters_general_count, parameters_general_count],
                                    ["LinearSVC","Multinomial NB","Decision Tree","Random Forest"]):

    grid = GridSearchCV(models, parameters, cv=5)
    grid.fit(x_train, y_train)
    print("Model ismi: "+ name)
    print("En iyi cross-validation score: {:.2f}".format(grid.best_score_ * 100))
    print("En iyi parametreler: ", grid.best_params_)
    
    y_train_pred = grid.predict(x_train)
    print(confusion_matrix(y_train, y_train_pred))

    
    final_model = grid.best_estimator_
    final_test_prediction = final_model.score(x_test, y_test)
    print("Test score: {:.2f}%".format(final_test_prediction * 100))    
    print("--------------------------")
    
    
    
    
    
    
    
for models, parameters, name in zip([LinearSVC_tfidf, Naive_tfidf, Decision_tfidf, RandomForest_tfidf],
                                    [parameters_of_svc_tfidf, parameters_of_general_tfidf, parameters_of_general_tfidf, parameters_of_general_tfidf],
                                    ["LinearSVC","Multinomial Naive Bayes","Decision Tree","Random Forest"]):

    grid = GridSearchCV(models, parameters, cv=5)
    grid.fit(x_train, y_train)
    print("Model ismi: "+ name)
    print("En iyi cross-validation score: {:.2f}".format(grid.best_score_ * 100))
    print("En iyi parametreler: ", grid.best_params_)
    
    y_train_pred = grid.predict(x_train)
    print(confusion_matrix(y_train, y_train_pred))
    
    final_model = grid.best_estimator_
    final_test_prediction = final_model.score(x_test, y_test)
    print("Test score: {:.2f}%".format(final_test_prediction * 100))    
    print("--------------------------")
    
    
    
    # En iyi sonuç veren parametrelerimizi de yapının içerisine ekliyoruz.
best_pipeline = Pipeline([
    ('tfidfvectorizer', TfidfVectorizer(min_df=1,stop_words=stop,ngram_range=(1,2))),
    ('LinearSVC', LinearSVC(C=10,max_iter=1000))
])
    
    
best_pipeline.fit(x_train,y_train)
    
best_pipeline.steps

final_test_prediction = best_pipeline.score(x_test,y_test)
print("Final test score:",final_test_prediction)

y_test_pred = best_pipeline.predict(x_test)
print("Confusion matrix\n",confusion_matrix(y_test,y_test_pred))




from sklearn.externals import joblib

joblib.dump(best_pipeline,"latest_model.pkl")



best_model = joblib.load("latest_model.pkl")
final_test_prediction = best_model.score(x_test,y_test)
print("Final Test Score:",final_test_prediction)


best_model.predict(["bataryası çok fazla gidiyor","kamerası çok iyi ","fakat şarjı çok hızlı bitiyor","güzel ürün","beğenmedim tavsiye etmem"])



def analiz(inp):
    print(inp[0])
    
    sonuc=best_model.predict([inp[0]])
    print(sonuc)
    print("tahmin",sonuc)

    if sonuc==[0]:
        return 0
    else:
        return 1
    
analiz(["bataryası çok fazla gidiyor"])

