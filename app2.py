import streamlit as st
st.header("Word search")  
st.text("please select one")  
import json,requests
from pprint import pprint
keyword=input('plz give me a keyword')
import streamlit as st
keyword = st.radio("Words that...",('sound like', 'look like', 'are opposite to', 'are similar to'))
st.write('your word')

url1= 'https://api.datamuse.com/words?syn=' + keyword + '&max=4'
