import streamlit as st


st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")



st.header('المرجله تبي')

st.write('ابوعج خرق :')



st.write('من افضل لاعب بالعالم')

benz1 = st.checkbox('ابو ابراهيم')
benz2 = st.checkbox('البنز')
benz3 = st.checkbox('الحكومه')

if benz1:
     st.markdown("![Alt Text](https://media.giphy.com/media/4AMPEcnNSDhfzZE3EV/giphy.gif)")

if benz2: 
     st.markdown("![Alt Text](https://media.giphy.com/media/12WxFiMHBUl1RK/giphy.gif)")

if benz3:
     
     st.markdown("![Alt Text](https://media.giphy.com/media/AZ72S63Skv1306yyxQ/giphy.gif)")




