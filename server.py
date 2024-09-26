"""
Sentiment Analyzer Flask Application.

This module creates a simple web application to analyze the sentiment of
text provided by the user. The application uses a sentiment analysis
function to classify the sentiment and returns the label and score.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initialize the Flask application
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Endpoint to analyze the sentiment of provided text.
    Retrieves the text from request arguments and processes it.
    Returns the sentiment label and score.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."

    # Return a formatted string with the sentiment label and score
    return f"The given text has been identified as {label.split('_')[1]} " \
           f"with a score of {score}."

@app.route("/")
def render_index_page():
    """
    Renders the index page where the user can input text for sentiment analysis.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
