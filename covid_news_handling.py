
import requests
import json
import logging
import flask


def news_API_request(covid_terms='Covid, COVID-19, coronavirus') -> dict:

    key_terms = 'Covid, COVID-19, coronavirus'
    f = open('config.json')
    config_dict = json.load(f)
    api_key = config_dict["api_key"]

    try:
        main_url = 'https://newsapi.org/v2/everything?q=' + \
            key_terms + "&apiKey=" + api_key
        news = requests.get(main_url).json()
        articles = news['articles']
    # For the instance someone has incorrect URL parameters the config file incorrectly
    except ValueError:
        logging.exception('Invalid API URL')
        main_url = 'https://newsapi.org/v2/everything?q=' + \
            covid_terms + "&apiKey=" + api_key
        news = requests.get(main_url).json()
        articles = news['articles']
    else:
        logging.info('News API Called')

    return articles
