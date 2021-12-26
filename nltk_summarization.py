import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize , sent_tokenize
import heapq

nltk.download('stopwords')
nltk.download('punkt')

def nltk_summarizer(raw_text):
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequency = {}
    for word in nltk.word_tokenize(raw_text):
        if word not in stopwords:
            if word not in word_frequency.keys():
                word_frequency[word] = 1
            else :
                word_frequency[word] += 1
    
    maximum_frequency = max(word_frequency.values())

    for word in word_frequency.keys():
        word_frequency[word] = (word_frequency[word]/maximum_frequency)
    
    sentence_list = nltk.sent_tokenize(raw_text)
    sentence_scores = {}

    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequency.keys():
                if len(sent.split(' ')) < 30 :
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequency[word]
                    else : 
                        sentence_scores[sent] += word_frequency[word]
    
    summary_sentences = heapq.nlargest(7,sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    
    return summary
