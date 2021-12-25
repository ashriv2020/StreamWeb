import streamlit as st
import pandas
from datetime import datetime as dt

data= {
  'Series_1':[1,3,5,7,9],
  'Series_2':[10,30,50,70,90],
}

st.title('Another py web')
st.subheader('Welcome to my website!')
st.write(''' Here you can learn how to build website using python.
Great Journey need to start early!!
Let's Start....
''')
df = pandas.DataFrame(data)
st.subheader('adding pandas dataframe!')
st.write(df);
st.subheader('here is chart...')
st.line_chart(df)
st.subheader('area chart...')
st.area_chart(df)

st.subheader('Time to add an intracting app...')
st.write("you can convert celcius to fahrenheit....")
myslider = st.slider('Celcius')
st.write(myslider, 'in Fahrneheit is', myslider * 9/5 + 32)
st.write("cool!! isn't it.....")

st.subheader('Age Calculator')
now= dt.now()
birth_date =st.date_input("When's your Birthday?")
st.write("your birhday is:", birth_date)
st.write("You're :", str(now.year - birth_date.year)+ ' years ' + str(now.month - birth_date.month) + ' months ' + str(now.day - birth_date.day) + ' days Old')

genders = [ 'Female','Male', 'Others']
st.subheader('Some more Fun!')
gender = st.radio('what is your gender?', genders)
st.write('You are ', gender)