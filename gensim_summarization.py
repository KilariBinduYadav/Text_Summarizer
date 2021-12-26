from gensim.summarization import summarize

def gensim_summarize(raw_text):
    final_text = summarize(raw_text)
    result = 	result = '\nGensim Summary:{}\n'.format(final_text)
    return result
