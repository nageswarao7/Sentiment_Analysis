# Sentiment Analysis Using BERT

## Sentiment Analysis API

This project provides a Flask-based API for sentiment analysis using a pre-trained BERT model. It predicts the sentiment of movie reviews (positive or negative) based on input text.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)

## Features

- Uses BERT for sequence classification to predict sentiments.
- Supports input of text via a RESTful API.
- Returns predicted sentiment as a JSON response.

## Requirements

- Python
- Flask
- Pandas
- PyTorch
- Transformers
- Scikit-learn

## Sentiment Analysis for Streamlit App

The project includes a Streamlit application that provides a user-friendly interface for sentiment analysis. Users can enter movie reviews directly into the app, and it will display the predicted sentiment in real-time. The app leverages the same BERT model used in the Flask API, allowing for seamless integration and testing of the sentiment analysis capabilities.

## Requirements

- Python
- Streamlit
- Pandas
- PyTorch
- Transformers
- Scikit-learn

You can install the required packages using pip:

pip install flask pandas torch transformers scikit-learn
