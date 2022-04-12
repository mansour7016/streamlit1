import streamlit as st

st.write('divine player lol :')



st.write('Goodbye')

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')

from PIL import Image
image = Image.open('sunrise.jpg')

st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
