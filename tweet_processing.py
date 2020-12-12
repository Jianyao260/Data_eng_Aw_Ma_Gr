import numpy as np
import string
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from gensim.parsing.preprocessing import remove_stopwords

def clean_tweets():

    df = pd.read_csv('tweets.csv')

    df_text = df.drop(columns=['Unnamed: 0','date','id','link','retweet','author']) 

    df_text['text_processed'] = df_text['text'].str.replace(r'@\S+', '')
    df_text['text_processed'] = df_text['text_processed'].str.replace(r'http\S+','')
    df_text['text_processed'] = df_text['text_processed'].str.replace(r'https\S+','')
    df_text['text_processed'] = df_text['text_processed'].str.replace(r'pic\S+','')
    df_text['text_processed'] = df_text['text_processed'].str.replace('[^a-zA-Z]',' ')
    df_text['text_processed'] = df_text['text_processed'].str.lower()
    df_text['text_processed'] = df_text['text_processed'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>1]))

    a = 0
    for i in df_text['text_processed']:
        df_text['text_processed'][a] = remove_stopwords(df_text['text_processed'][a])
        a += 1

    arr_og = df['text'].to_numpy()
    arr = df_text['text_processed'].to_numpy()

    pickle.dump(arr_og, open('arr_og.pkl', 'wb'))
    pickle.dump(arr, open('arr.pkl', 'wb'))

def similar_tweets(sentence, arr, arr_og):

    arr = np.append(arr, sentence)

    vectorizer = CountVectorizer().fit_transform(arr)
    vectors = vectorizer.toarray()

    sim = pd.DataFrame(columns = ['cosine', 'tweet'])

    for i in range(len(vectors) - 1):
        if consine_sim_vectors(vectors[i], vectors[len(vectors) - 1]) != 0:
            a = pd.DataFrame([[consine_sim_vectors(vectors[i], vectors[len(vectors) - 1]), arr_og[i]]], columns = ['cosine', 'tweet'])
            sim = sim.append(a)
    
    sim = sim.sort_values(by=['cosine'], ascending=False, ignore_index=True)
    return(sim.head(20))

def consine_sim_vectors(vec1, vec2):
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)

    return cosine_similarity(vec1, vec2)[0][0]

if __name__ == "__main__":
    clean_tweets()