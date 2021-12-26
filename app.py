from os import link
from nltk import text
import streamlit as st
from textblob import TextBlob
from nltk_summarization import nltk_summarizer
from gensim_summarization import gensim_summarize
from url import url_text

def get_text():
    uploaded_file = st.file_uploader("Add text file!",type='txt')

    if uploaded_file :
        text = ''
        for line in uploaded_file:
            line = line.decode('utf8').replace("\r", "").replace("\n", "")
            text = text+line
        return text

def main():
    st.title("Text Summarization")
    
    Summarizer = st.radio('',options = ['Extractive Summarization', 'Abstractive Summarization'])
    st.write('<style>div.row-widget.stRadio > div { flex-direction : row;}</style>',unsafe_allow_html = True)
    if (Summarizer == 'Extractive Summarization'):

        options = st.selectbox("Type of file",['Text','File','URL'])

        if options == 'Text':
            st.subheader("Summarize your text")
            message = st.text_area("Enter your text")
            if st.button("Summarize"):
                nlp_result = nltk_summarizer(message)
                st.success("Summary:   \n"+nlp_result)
        elif options == 'File':
            try:
                text = get_text()
                message = st.subheader("Your text")
                st.info(text)
                if st.button("Summarize"):
                    result = nltk_summarizer(text)
                    st.success("Summary:   \n"+result)
            except:
                pass    
        elif options == 'URL':
            try:
                link = st.text_input("Enter the URL")
                text = url_text(link)
                message = st.subheader("Your text")
                st.info(text)
                if st.button("Summarize"):
                    result = nltk_summarizer(text)
                    st.success("Summary:   \n"+result)
            except:
                pass
       
    else:
        st.success("")





if __name__ == '__main__':
    main()