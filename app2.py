import streamlit as st
st.header("Word search")  
st.text("please select one")  
import json,requests
from pprint import pprint
st.text_input("choose a word")

keyword = st.radio("now choose what you are most interested in",('sounds like', 'looks like', 'is opposite to', 'is similar to'))
st.write('your word')
if keyword == 'sounds like':
     st.write('Your word sounds like'dataFromDatamuse1,)
if keyword == 'looks like':
     st.write('Your word looks like')
if keyword == 'is opposite to':
     st.write('Your word is the opposite of')
if keyword == 'is similar to':
     st.write('Your word is similar to')
url1= 'https://api.datamuse.com/words?sl=' + keyword + '&max=10'
response1 = requests.get(url)  
dataFromDatamuse1 = json.loads(response1.text)
