import re

def tokenize_sentence(text):
    return re.split(r'(?<![А-Я]\.[А-Я]\.)(?<=[.?!\u2026)\u2048"\'])\s+(?=[А-Я"\u2014])', text)

def tokenize_word(sentence):
    return list(filter(lambda x : x, re.split(r'[\s.,–\-:;"‘`«»()!?]+', sentence)))






