"""
Sentiment Analyzer Module.

This module provides a function to analyze the sentiment of a given text by
sending a POST request to a sentiment analysis API and returning the
sentiment label and score.
"""

import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    Analyzes the sentiment of the provided text using an external API.
    
    Parameters:
        text_to_analyse (str): The text to be analyzed for sentiment.
    
    Returns:
        dict: A dictionary containing the sentiment label and score, or
              None if the request fails.
    """
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/' \
          'watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Create the payload with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyse}}

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    try:
        # Make a POST request to the API with the payload and headers, include a timeout
        response = requests.post(url, json=myobj, headers=header, timeout=10)
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        # If the response status code is 200, extract the label and score
        if response.status_code == 200:
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']
        else:
            label = None
            score = None
    except requests.RequestException:
        # Handle network errors
        label = None
        score = None

    # Return the label and score in a dictionary
    return {'label': label, 'score': score}
