import streamlit as st

st.write('divine player lol :')



st.write('Goodbye')

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')


st.markdown("![Alt Text](https://giphy.com/gifs/reaction-seinfeld-kramer-ie4fEHT4krdDO)")
