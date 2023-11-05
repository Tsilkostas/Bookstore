from django.shortcuts import render

import requests


# Create your views here.

url = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com",
        "X-RapidAPI-Key": "fbd9e893e9msh84b2f8e7d15bbc5p1f49ccjsnb89591fea9fa"
    }

response = requests.request("GET", url, headers=headers).json()

formatted_quote_content = response['content']
formatted_quote_originator = response['originator']['name']
formatted_quote = f'The quote for today is: {formatted_quote_content} by {formatted_quote_originator}'

