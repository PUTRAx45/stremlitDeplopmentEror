
import streamlit as st
import pandas as pd
import streamlit as st
import streamlit as st
df = pd.DataFrame({
'c1':[1,2,3,4,5],
'c2':[10,20,30,40,50],
})

st.table(data=df)
st.balloons()
st.write("HAI SAYANG")
st.text("This is text\n[and more text](that's not a Markdown link).")