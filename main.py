# Copyright (c) 2024 Melodiz
# Licensed under the MIT License

import os
from parse_code import extract_user_text
from translation import translate_russian_to_english
from classification import classify_prompt

# How we deal with warnings and errors? Surely:
# Disable parallelism in tokenizers to avoid warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def process_prompt(prompt):
    # Extract user text from code
    prompt = extract_user_text(prompt)
    # Translate Russian text to English
    prompt = translate_russian_to_english(prompt)
    # Classify the prompt
    label, score = classify_prompt(prompt)
    return label, score