from textblob import TextBlob
from typing import List

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    return word in text

def bubble_sort(lst):
    if type(lst) is not list:
        return None 
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if type(lst[j]) not in [int, float] or type(lst[j+1]) not in [int, float]:
                    return None
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst