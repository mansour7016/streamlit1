import streamlit as st

st.write('divine player lol :')



st.write('Goodbye')

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')


st.markdown("![Alt Text](https://external-preview.redd.it/1wo-03XQUXf9UbS40C_OFt9QVV7y5vDZxhfX2_EmevY.gif?format=mp4&s=a677f5c4f3cd7c0da5b12fa0a56dc89de5fde651)")
