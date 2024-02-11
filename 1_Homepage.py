""""Here All the buttons are there to navigate to different pages"""
import streamlit as st
from API import API

st.set_page_config(page_title="Homepage", page_icon=":bar_chart:")
st.title("Homepage")

API.remove_files()


st.header("Instructions")
st.markdown("Welcome to the ChatBots")
st.markdown("Enter your OpenAI API key and select the model you want to use")
st.markdown("Click on the 'Verify' button to verify the API key")
st.markdown("Click on the 'Chat With Savannah' button to start the chat")
st.markdown("Click on the 'Chat With Lana' button to start the chat with CSV data")
st.markdown("Click on the 'Chat With Jessa' button to start the chat with Two CSV data")
st.markdown("Click on the 'Chat With Megan' button to clean, generate features and plot the graph")
