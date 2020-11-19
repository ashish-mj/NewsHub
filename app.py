#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:20:57 2020

@author: ashish
"""
from flask import Flask, render_template
from newsapi import NewsApiClient


app = Flask(__name__)

def extract(articles):
    desc,news,img,url = [],[],[],[]
    
    for i in range(len(articles)):
        my_articles = articles[i]
        
        news.append(my_articles['title'])  
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])
        url.append(my_articles['url'])
        
    my_list = zip(desc, news, img, url)
    return my_list
    

@app.route('/')
@app.route('/sports')
def home():
    newsapi = NewsApiClient(api_key='dcbd16c218ef4985a822b478b4f20f49')
    top_headlines = newsapi.get_top_headlines(
                                          category='sports',
                                          language='en',
                                          country='in')
    
    articles = top_headlines['articles']
    my_list = extract(articles)
    return render_template('home.html',my_list=my_list)

@app.route('/entertainment')
def entertainment():
    newsapi = NewsApiClient(api_key='dcbd16c218ef4985a822b478b4f20f49')
    top_headlines = newsapi.get_top_headlines(
                                          category='entertainment',
                                          language='en',
                                          country='in')
    
    articles = top_headlines['articles']
    my_list = extract(articles)
    return render_template('home.html',my_list=my_list)

@app.route('/science')
def science():
    newsapi = NewsApiClient(api_key='dcbd16c218ef4985a822b478b4f20f49')
    top_headlines = newsapi.get_top_headlines(
                                          category='science',
                                          language='en',
                                          country='in')
    
    articles = top_headlines['articles']
    my_list = extract(articles)
    return render_template('home.html',my_list=my_list)


@app.route('/business')
def business():
    newsapi = NewsApiClient(api_key='dcbd16c218ef4985a822b478b4f20f49')
    top_headlines = newsapi.get_top_headlines(
                                          category='business',
                                          language='en',
                                          country='in')
    
    articles = top_headlines['articles']
    my_list = extract(articles)
    return render_template('home.html',my_list=my_list)

@app.route('/health')
def health():
    newsapi = NewsApiClient(api_key='dcbd16c218ef4985a822b478b4f20f49')
    top_headlines = newsapi.get_top_headlines(
                                          category='health',
                                          language='en',
                                          country='in')
    
    articles = top_headlines['articles']
    my_list = extract(articles)
    return render_template('home.html',my_list=my_list)


if __name__=="__main__": 
    app.run(debug='False')
        
    
