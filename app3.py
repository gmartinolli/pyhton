import streamlit as st
from googletrans import Translator
translator = Translator()
st.header("Google translator")  
keyword1 = st.text_input("translate")  
keyword2 = st.text_input("into which language?", value="en")
word= keyword1 
abc = translator.translate(word,dest= keyword2)
st.write('the given word is in:', abc.src)
st.write('in', keyword2, 'your word means:', abc.text)
