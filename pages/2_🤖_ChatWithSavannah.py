import streamlit as st
from openai import OpenAI
from API import API

st.set_page_config(page_title="Chat With Savannah", page_icon="🤖")

st.title("Talk With Savannah🤖")

if "openai" not in st.session_state:
    st.session_state["openai"] = None

if st.session_state["openai"] is None:
    st.session_state["openai"] = API.verify_api()

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi I am Savannah. How can I help you?"}]

if st.session_state["openai"] is not None:
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What Is Up?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        
        st.session_state["messages"].append({"role": "user", "content": prompt})
        
        with st.chat_message("assistant"):
            try:
                box = st.empty()
                full_response = ""
                client = OpenAI(api_key=st.session_state["openai"])
                response = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=st.session_state["messages"]
                )
                full_response += response.choices[0].message.content

                box.markdown(full_response)
            
                st.session_state["messages"].append({"role": "assistant", "content": full_response})

            except Exception as e:
                st.error(e)

    if st.session_state["openai"] is not None:
        if st.button("reset"):
            st.session_state["messages"] = [{"role": "assistant", "content": "Hi I am Savannah. How can I help you?"}]
            
            





