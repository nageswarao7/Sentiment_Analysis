import pandas as pd
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.preprocessing import LabelEncoder
import pickle
import streamlit as st

# Load the dataset
data = pd.read_csv('movie_review.csv')
label_encoder = LabelEncoder()
data['sentiment'] = label_encoder.fit_transform(data['sentiment'])

# Initialize the tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Load the saved model and tokenizer (if necessary)
model_path = "bert_sentiment_analysis_model.pkl"
tokenizer_path = "bert_sentiment_analysis_tokenizer.pkl"

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(tokenizer_path, 'rb') as f:
    tokenizer = pickle.load(f)

# Function for making predictions
def predict_sentiment(text):
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        return_token_type_ids=False,
        padding='max_length',
        truncation=True,
        return_attention_mask=True,
        return_tensors='pt'
    )

    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        _, predicted = torch.max(outputs.logits, dim=1)

    sentiment = label_encoder.inverse_transform(predicted.numpy())
    return sentiment[0]

# Streamlit app layout
st.title("Movie Review Sentiment Analysis")
st.write("Enter a movie review to predict its sentiment (positive or negative):")

user_input = st.text_area("Review Text")

if st.button("Predict Sentiment"):
    if user_input:
        predicted_sentiment = predict_sentiment(user_input)
        st.success(f"Predicted Sentiment: {predicted_sentiment}")
    else:
        st.error("Please enter a review.")
