import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = word_tokenize(text)

    text = [i for i in text if i.isalnum()]
    text = [i for i in text if i not in stopwords.words('english')]

    text = [ps.stem(i) for i in text]

    return " ".join(text)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Page Title and Description
st.set_page_config(page_title="Email/SMS Spam Classifier", page_icon="📧")
st.title("Email/SMS Spam Classifier")
st.markdown("---")
st.markdown("Welcome to the Email/SMS Spam Classifier! Enter a message and click the 'Predict' button to classify it as "
            "spam or not spam.")

# User Input and Prediction
input_sms = st.text_area("Enter the message")
predict_button = st.button("Predict")

if predict_button:
    if not input_sms.strip():
        st.error("Please enter a message.")
    else:
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        result = model.predict(vector_input)[0]

        st.markdown("---")
        st.subheader("Input Message:")
        st.write(input_sms)

        st.subheader("Classification Result:")
        if result == 1:
            st.error("Spam")
        else:
            st.success("Not Spam")

# Footer
st.markdown("---")
st.markdown("Created by Anuj Sharma, Harshwardhan Sangat, Riya Agarwal")
