import streamlit as st
from transformers import pipeline


def classify(sequence):
   # DistilBertForSequenceClassification(default model)
    nlp_cls = pipeline('sentiment-analysis')
    return nlp_cls(sequence)


def main():
    st.title("Sentiment Analyser using BERT Transformer model")
    st.subheader(
        "Hi this is Vishwajith, This is my first transformer app")
    st.subheader(
        "This is a simple Sentiment Analysis app using Hugging Face Transformer pretrained model")
    st.subheader("This model predicts the sentiment of review given with a polarity score, Since the BERT model is pretrained on a large text corpora retraining time is saved and model complexity and bias is reduced.")

    st.subheader(
        "The model is served through streamlit --> docker and deployed on Heroku")

    st.subheader("Submit review below and click Analyse")
    message = st.text_area("Enter your text here")
    if st.button("Analyse"):
        CS = classify(message)
        st.text('Review Sentiment and Score')
        st.json(CS)


if __name__ == '__main__':
    main()
