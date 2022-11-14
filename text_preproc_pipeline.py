import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import datetime as dt
import string



def to_lower(series):
    return str(series).lower()

def remove_numbers(series):
    text = re.sub(r'\d+', "", str(series))
    return text

def remove_punct(series):
    avoid = string.punctuation+'’'+"”"+"“"+"\n"+"•"+";"
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    return series.translate(translator)

def to_tokens(series):
    stop = stopwords.words('english')
    return ' '.join([item for item in word_tokenize(series) if item not in stop])

def lemmatize(series):
    lemmatizer = WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(w) for w in word_tokenize(series)])

def preproc(series):
    return lemmatize(to_tokens(remove_punct(remove_numbers(to_lower(series)))))