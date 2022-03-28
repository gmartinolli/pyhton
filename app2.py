import streamlit as st
st.header("Word search")  
st.text("please select one")  
import json,requests
from pprint import pprint
keyword = st.text_input("choose a word")
search = st.selectbox("now choose what you are most interested in",('sounds like', 'looks like', 'is opposite to', 'is similar to'))
st.write('your word')
url1= 'https://api.datamuse.com/words?sl=' + keyword + '&max=10'
response1 = requests.get(url1)  
dataFromDatamuse1 = json.loads(response1.text)
url2= 'https://api.datamuse.com/words?ml=' + keyword + '&max=10'
response2 = requests.get(url2)  
dataFromDatamuse2 = json.loads(response2.text)
url3= 'https://api.datamuse.com/words?rel_ant=' + keyword + '&max=10'
response3 = requests.get(url3)  
dataFromDatamuse3 = json.loads(response3.text)
url4= 'https://api.datamuse.com/words?rel_syn=' + keyword + '&max=10'
response4 = requests.get(url4)  
dataFromDatamuse4 = json.loads(response4.text)
if search == 'sounds like':
     st.write('Your word sounds like',dataFromDatamuse1)
if search == 'looks like':
     st.write('Your word looks like',dataFromDatamuse2)
if search == 'is opposite to':
     st.write('Your word is the opposite of',dataFromDatamuse3)
if search == 'is similar to':
     st.write('Your word is similar to',dataFromDatamuse4)


