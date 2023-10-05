from logging import exception
from re import template
from unittest import result
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from .models import movie
from datetime import datetime
import os
from collections import ChainMap
def news(request):
    template =loader.get_template('movie/news.html')
    try:
        key_news=os.environ.get("newsapi")
        url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}".format(key_news)
        response=requests.get(url)
        data= response.json()
        data=data['articles']
        print(data)
        context={
            "news_data":data
        }
    except:
         context={
            
        }
    return HttpResponse(template.render(context,request))

# Create your views here.
def search(request):
  

    template = loader.get_template('movie/result.html')
    if request.method =='POST':
        
        formdata=request.POST.dict()
        movie_name = request.POST["Movie_Name"]
        movieapi=os.environ.get('moviesapi')
        baseurl="http://www.omdbapi.com/?t={}&apikey={}".format(movie_name,movieapi)
        
        response=requests.get(baseurl)
        result=response.json()
        try:
            movie_data=movie(**result)
            movie_data.save()
            # print(movie_data)
        except:
            pass
        
        context={
            'result':result,
           
        }
    else:

        context={
            
        }
    
    
    return HttpResponse(template.render(context,request))

def info_n(names):
    news=[]
    for items in names:
        try:
            key_news=os.environ.get("newsapi")
            url="https://newsapi.org/v2/everything?q={}&from=2022-06-16&sortBy=popularity&apiKey={}".format(items,key_news)
            response=requests.get(url)
            data= response.json()
            data=data['articles'][1]
            news.append(data)
        
        except:
            pass
    
    return news


def home(request):
    template = loader.get_template('movie/home.html')
    list_movies = movie.objects.all().order_by('imdbRating')[:4].values()
    movie_names =movie.objects.values_list('Title')
    movie_values=info_n(movie_names)
    context={
        "data":list_movies,
        "movie": movie_values
    }
    return HttpResponse(template.render(context, request))