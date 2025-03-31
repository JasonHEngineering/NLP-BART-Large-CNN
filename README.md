# NLP-BART-Large-CNN

This is a simple python script that utilizes facebook/bart-large-cnn model (https://huggingface.co/facebook/bart-large-cnn) to summarize a transcipt contained in .xlsx file.

This script will run through an archived transcript:
sample transcript is from https://www.mof.gov.sg/news-publications/speeches/transcript-of-speech-by-second-minister-for-finance-indranee-rajah-for-the-substantive-motion-on-public-finances-at-the-parliament-7-february-2024
which was copied to excel - save as "Transcript.xlsx"

The transcript constst of 102 recorded statements across 180 rows.
If the length of words in the cell was found to be less than 50 words; skip and move to next cell instead.

Both sample transcript and output file are also archived here for reference.

# Dependencies
This script requires installation of PyTorch and Hugging Face (transformers) in addition to Pandas.

# Caveat
As in any NLP technique, mistakes is possible. Please note that the original transcript before any processing shall remain as source of truth. Output summarization from this technique cannot be referenced reliably. 
