# Sentiment Analyzer using IBM Watson AI

## Overview

This project demonstrates an AI-powered Python Flask application built with embeddable Watson AI libraries. The application leverages pre-installed Watson libraries for Natural Language Processing (NLP), text-to-speech, and speech-to-text functionalities.

The NLP library provides tools for sentiment analysis, emotion detection, language identification, and text classification. The speech-to-text library transcribes audio into written text, while the text-to-speech library generates lifelike audio from text. These libraries use pretrained AI models, readily available to all users.

This repository contains the core application code for this project.

## IBM Watson Embeddable AI Libraries

The embeddable libraries used in this project include:

- **NLP Library**: Performs tasks such as sentiment analysis, emotion recognition, and text classification.
- **Speech-to-Text Library**: Converts spoken audio into written text.
- **Text-to-Speech Library**: Converts written text into natural-sounding audio.

All functions in these libraries rely on pretrained models and can be easily accessed by making POST requests. There is no need for additional library installations since they are already integrated with the project.

For more details on accessing these libraries through your own systems, refer to the [Watson AI Library documentation](https://www.ibm.com/docs/en/watson-libraries?topic=watson-text-speech-library-embed-home).

## NLP Sentiment Analysis

Natural Language Processing (NLP) sentiment analysis allows computers to determine the sentiment or emotion in text data. It classifies text as positive, negative, or neutral, making it useful for understanding customer feedback, product reviews, and public sentiment.

This project applies IBM Watson's embedded AI libraries for sentiment analysis by sending POST requests to pre-trained models, which return sentiment results in real time.

## Text-to-Speech

IBM Watson's Text-to-Speech service converts written text into lifelike speech. The service supports multiple languages and dialects, providing male and female voices for several languages. Audio is returned with minimal delay. Learn more via the [API documentation](https://www.ibm.com/docs/en/watson-libraries?topic=watson-text-speech-library-embed-home).

## Speech-to-Text

IBM Watson’s Speech-to-Text service transcribes audio into text, supporting various languages and audio formats. It can also return detailed information about audio content. All responses are returned in JSON using UTF-8 encoding. More details can be found in the [API documentation](https://www.ibm.com/docs/en/watson-libraries?topic=watson-speech-text-library-embed-home).

## Sentiment Analysis with BERT

The pre-trained BERT models are used to classify sentiment in input text, predicting sentiment at the document, sentence, and target levels. For more information, refer to the [API documentation](https://www.ibm.com/docs/en/watson-libraries?topic=catalog-sentiment).

## Acknowledgments

This project is inspired by IBM Skills Network's code practice materials.

## App Screenshot

![image](https://github.com/user-attachments/assets/81940643-78c4-4831-a362-63a5af03d266)


