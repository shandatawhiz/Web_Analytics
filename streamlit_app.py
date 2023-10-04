pip install streamlit
import streamlit as st
import streamlit_analytics


with streamlit_analytics.track():
  st.text_input("Write your name")
  st.selectbox("Select your favorite", ["Practice","Makes","Succes"])
  st.button("Click me")
