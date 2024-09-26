# sentiment-analyzer-ibm-watsonai

## About Embeddable Watson AI libraries

In this project, I'll be using embeddable libraries to create an AI powered Python Flask application.

Embeddable Watson AI libraries include the NLP library, the text-to-speech library and the speech-to-text library. These libraries can be embedded and distributed as part of this application. These libraries have been pre-installed in this project. This repo is for keeping the code only.

The NLP library includes functions for sentiment analysis, emotion detection, text classification, language detection, etc. among others. The speech-to-text library contains functions that perform the transcription service and generates written text from spoken audio. The text-to-speech library generates natural sounding audio from written text. All available functions, in each of these libraries, calls pretrained AI models that are all available to all users for free.

These libraries may also be accessed through your personal systems. The guidelines for the same are available on the Watson AI library page.

## What is NLP Sentiment Analysis
NLP sentiment analysis is the practice of using computers to recognize sentiment or emotion expressed in a text. Through NLP, sentiment analysis categorizes words as positive, negative or neutral.

Sentiment analysis is often performed on textual data to help businesses monitor brand and product sentiment in customer feedback, and understanding customer needs. It helps attain the attitude and mood of the wider public which can then help gather insightful information about the context.

For creating the sentiment analysis application, we'll be making use of the Watson Embedded AI Libraries. Since the functions of these libraries are already deployed on the IDE, there is no need of importing these libraries to our code. Instead, we need to send a POST request to the relevant model with the required text and the model will send the appropriate response.

## Text-To-Speech
The IBM Watson Text to Speech service provides APIs that use IBM's speech-synthesis capabilities to synthesize text into natural-sounding speech in a variety of languages, dialects, and voices. The service supports at least one male or female voice, sometimes both, for each language. The audio is streamed back to the client with minimal delay. Open API Docs: https://www.ibm.com/docs/en/watson-libraries?topic=watson-text-speech-library-embed-home

## Speech-To-Text
The IBM Watson™ Speech to Text service provides APIs that use IBM's speech-recognition capabilities to produce transcripts of spoken audio. The service can transcribe speech from various languages and audio formats. In addition to basic transcription, the service can produce detailed information about many different aspects of the audio. It returns all JSON response content in the UTF-8 character set.
Open API Docs: https://www.ibm.com/docs/en/watson-libraries?topic=watson-speech-text-library-embed-home

## Sentiment - BERT
The Sentiment models are pre-trained classification models for classifying the sentiment of the input text. It can predict the document sentiment, each sentence's sentiment, and each target's sentiment. Using the BERT Model.
Open API Docs: https://www.ibm.com/docs/en/watson-libraries?topic=catalog-sentiment
