# Email/SMS Spam Classifier

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)

The Email/SMS Spam Classifier is an intelligent system that accurately identifies and filters out spam messages, enhancing communication efficiency and reducing the impact of unwanted messages.

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)

## Introduction

Spam messages are a common nuisance in today's digital world. This project aims to address the issue of unwanted messages by developing a reliable classifier that distinguishes between spam and non-spam messages. The classifier is built using machine learning algorithms and natural language processing techniques.

## Methodology

The project follows the following methodology:
1. Data Collection: Curate a diverse dataset of labeled email and SMS messages, including both spam and non-spam examples.
2. Preprocessing: Perform text normalization, tokenization, and stop word removal to prepare the data for analysis.
3. Feature Extraction: Utilize the TF-IDF technique to represent text data numerically, capturing the importance of each word.
4. Model Training: Employ the Multinomial Naive Bayes algorithm to train the spam classifier using the preprocessed data.
5. User Interface: Develop an interactive user interface using Streamlit for easy message input and real-time classification.


