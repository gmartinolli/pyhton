import streamlit as st
st.header("hello world")  
st.text("from Brixen")  
import streamlit as st
title = st.text_input('Gimme a nice movie title', 'lorem ipsum')
st.write('The current movie title is', title)

import streamlit as st
genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")

     
     
import json, requests 
APIkey = "e8d8bf91c4a17c3cd68e16fc49886d0b"
import streamlit as st
location = st.radio("What's the weather in",('London', 'Madrid', 'Sydney'))
st.write('the weather for today')
st.write('The temperatures of', location)
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
response = requests.get(url)
weatherData = json.loads(response.text)
st.write('max temperature:', weatherData['main']['temp_max'])
st.write('min temperature:', weatherData['main']['temp_min'])
st.write('weather:', weatherData['weather'][0]['description'])
