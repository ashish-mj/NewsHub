#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:20:57 2020

@author: ashish
"""
from flask import Flask, render_template
from newsapi import NewsApiClient


app = Flask(__name__)

@app.route('/')
def home():
    newsapi = NewsApiClient(api_key='dcbd16c218ef4985a822b478b4f20f49')
    top_headlines = newsapi.get_top_headlines(
                                          category='sports',
                                          language='en',
                                          country='in')
    
    articles = top_headlines['articles']
    
    desc,news,img = [],[],[]
    
    for i in range(len(articles)):
        my_articles = articles[i]
        
        news.append(my_articles['title'])  
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])
        
    my_list = zip(desc, news, img)
    return render_template('home.html',my_list=my_list)

if __name__=="__main__": 
    app.run(debug='False')
        
    
