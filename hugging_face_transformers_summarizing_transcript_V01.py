# -*- coding: utf-8 -*-
"""
Summarizes the given text using a Hugging Face transformer model.

:param text: The input text to summarize.
:param max_length: The maximum length of the summary.
:param min_length: The minimum length of the summary.
:return: A summarized version of the input text.

"""

import plotly.io as pio
import pandas as pd
import time
from transformers import BartTokenizer, pipeline
import logging

pio.renderers.default='browser'

# sample transcript is from https://www.mof.gov.sg/news-publications/speeches/transcript-of-speech-by-second-minister-for-finance-indranee-rajah-for-the-substantive-motion-on-public-finances-at-the-parliament-7-february-2024
# copied to excel - save as Transcript.xlsx

file_to_summarize = "Transcript"
i = 0
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
min_words = 50

def truncate_text(text, max_tokens=1012):
    """Ensure input does not exceed model limits."""
    tokens = tokenizer.encode(text, truncation=True, max_length=max_tokens)
    return tokenizer.decode(tokens)

def summarize_text(text, max_length=150, min_length=50):

    global i

    try:
        
        # start timer here
        start_time = time.perf_counter()

        original_word_count = len(text.split())

        # Skip summarization if text is too short
        if original_word_count < min_words:
            print(f"Skipping summarization (word count: {original_word_count})")
            # end timer here
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            i=i+1
            print(str(i) + " : " + str(elapsed_time))

            return text, original_word_count, original_word_count, elapsed_time
        
        summarizer = pipeline("summarization", model=model_name, framework="pt")
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']


        summary_word_count = len(summary.split())

        # end timer here
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        i=i+1
        print(str(i) + " : " + str(elapsed_time))

        return summary, original_word_count, summary_word_count, elapsed_time

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        i=i+1
        return " ", " ", " ", " "

df = pd.read_excel(open(file_to_summarize + '.xlsx', 'rb'),sheet_name='Sheet1')

# Truncate text in case of more than 1012 tokens
df["Event Text"]= df["Event Text"].apply(lambda x: pd.Series(truncate_text(x)))


# Apply summarization function to each row and store results in new columns
df[["event summary", "original_word_count", "summary_word_count", "elapse time (s)"]] = df["Event Text"].apply(
    lambda x: pd.Series(summarize_text(x))
)

# save to CSV
df.to_csv("summarized_result.csv", index=None)
