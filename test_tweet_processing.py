import unittest
import pickle
import pandas as pd
from tweet_processing import clean_tweets, similar_tweets
from flask import Flask, request, jsonify

class TestProcessing(unittest.TestCase):

    #Testing type of the input
    def test_type(self):
        a = clean_tweets(pd.DataFrame(data = [[0,'Oct 7',784609194234306560,'/realDonaldTrump/status/784609194234306560','False','Here is my statement.pic.twitter.com/WAZiGoQqMQ','DonaldTrump']], columns = ['Unnamed: 0', 'date', 'id', 'link', 'retweet', 'text', 'author']))
        self.assertEqual(type(a[0]), type(''))
    
    #Testing if picture links are deleted
    def test_format1(self):
        a = clean_tweets(pd.DataFrame(data = [[0,'Oct 7',784609194234306560,'/realDonaldTrump/status/784609194234306560','False','Hello pic.twitter.com/WAZiGoQqMQ','DonaldTrump']], columns = ['Unnamed: 0', 'date', 'id', 'link', 'retweet', 'text', 'author']))
        self.assertEqual(a[0], 'hello')

    #Testing if URLs are deleted
    def test_format2(self):
        a = clean_tweets(pd.DataFrame([[0,'Oct 7',784609194234306560,'/realDonaldTrump/status/784609194234306560','False','http://google.com https://facebook.com','DonaldTrump']], columns = ['Unnamed: 0', 'date', 'id', 'link', 'retweet', 'text', 'author']))
        self.assertEqual(a[0], '')

    #Testing lowercasing
    def test_format3(self):
        a = clean_tweets(pd.DataFrame([[0,'Oct 7',784609194234306560,'/realDonaldTrump/status/784609194234306560','False','DONALD TRUMP','DonaldTrump']], columns = ['Unnamed: 0', 'date', 'id', 'link', 'retweet', 'text', 'author']))
        self.assertEqual(a[0], 'donald trump')
    
    #Testing single letters deletion
    def test_format4(self):
        a = clean_tweets(pd.DataFrame([[0,'Oct 7',784609194234306560,'/realDonaldTrump/status/784609194234306560','False','donald a b c','DonaldTrump']], columns = ['Unnamed: 0', 'date', 'id', 'link', 'retweet', 'text', 'author']))
        self.assertEqual(a[0], 'donald')
    
    #Testing usernames deletion
    def test_format5(self):
        a = clean_tweets(pd.DataFrame([[0,'Oct 7',784609194234306560,'/realDonaldTrump/status/784609194234306560','False','@DonaldTrump testing','DonaldTrump']], columns = ['Unnamed: 0', 'date', 'id', 'link', 'retweet', 'text', 'author']))
        self.assertEqual(a[0], 'testing')

    #Testing non alphanumeric characters deletion
    def test_format6(self):
        a = clean_tweets(pd.DataFrame([[0,'Oct 7',784609194234306560,'/realDonaldTrump/status/784609194234306560','False',':) :D','DonaldTrump']], columns = ['Unnamed: 0', 'date', 'id', 'link', 'retweet', 'text', 'author']))
        self.assertEqual(a[0], '')
    
    #Testing cosine similarity for a given tweet
    def test_cosinesim(self):
        arr = pickle.load(open('arr.pkl', 'rb'))
        arr_og = pickle.load(open('arr_og.pkl', 'rb'))
        a = similar_tweets('Police', arr, arr_og)

        self.assertEqual(a['tweet'][0], '#TeamTrump. Police and law enforcement seem to have killed one of the California shooters and are in a shootout with the others. Go police')

