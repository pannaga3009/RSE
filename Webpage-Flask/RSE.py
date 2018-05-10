import pickle
import numpy as np
import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
import json

test_file = '../data/test/10.json'
summaries_file = '../data/test/summaries.json'
model_lr = '../models/LR.dat'
vectorizer_file = '../models/vectorFunction.sav'

clf = pickle.load(open(model_lr, 'rb'))
vectorizer =  pickle.load(open(vectorizer_file, 'rb'))


"""
1. For Each Restaurant in Test Json
    2. For each Reviews:
       3. v = vectorizer.transform(review[i])
       4. if clf.predict(v): 
            pos += 1
          else:
            neg += 1
    6. overall_rating = pos/(pos+neg) 
    7. res.summary = lookup(overall_rating)
"""


def summary_lookup(for_rating):
    with open(summaries_file,'r') as json_file:    
        d = json.load(json_file)
    if for_rating > 0.9:
        return d['summaries'][0]['Rank_1']
    elif 0.9 > for_rating >=0.8  :
        return d['summaries'][1]['Rank_2']
    elif 0.8>for_rating >= 0.7:
        return d['summaries'][2]['Rank_3']
    elif 0.7>for_rating >= 0.5:
        return d['summaries'][3]['Rank_4']
    elif 0.5>for_rating >= 0.4:
        return d['summaries'][4]['Rank_5']
    else:
        return d['summaries'][5]['Rank_6']

print(summary_lookup(.5))


class Restaurant():
    
    def __init__(self, business_id="", name="", reviews=[]):
        # Each rocket has an (x,y) position.
        self.bid = business_id
        self.name = name
        self.reviews = reviews
        self.pos = 0.0
        self.neg = 0.0
        self.predict()
        self.get_overall_rating()
        self.summary = summary_lookup(self.overall)
       
    def predict(self):
        for r in self.reviews:
            if clf.predict(vectorizer.transform([str(r)])):
                self.pos += 1.0
            else:
                self.neg += 1.0
        
    def get_overall_rating(self):
        self.overall = self.pos/(self.pos + self.neg)


    def print_summary(self):
        print("-------------------------")
        print("Business ID", self.bid)
        print("Over All Rating %f", self.overall)
        print("Summary", self.summary)
        print("-------------------------\n\n")



def get_output():
    with open(test_file,'r') as json_file:
        data = json.load(json_file)
    res = []
    for restaurant in data["yelp"]:
        res.append(Restaurant(business_id=restaurant["_id"], reviews=restaurant["reviews"]))
    return res

res = get_output()
for r in res:
    r.print_summary()

