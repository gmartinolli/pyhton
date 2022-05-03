import streamlit as st
from gtts import gTTS
import IPython.display as ipd  
from googletrans import Translator
translator = Translator()

text = st.text_input("type a text",'some text')
lang = st.text_input("choose a language", 'en')
detectedLanguage = translator.detect(text)
st.write(detectedLanguage.lang)
transTodest = translator.translate(text=text, src=detectedLanguage.lang, dest=lang)
st.write(transTodest.text)

tts1=gTTS(transTodest.text,lang)
tts1.save('audio.mp3')
st.audio(tts1, format="audio/wav",start_time=0)


