import streamlit as st
import pandas

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
