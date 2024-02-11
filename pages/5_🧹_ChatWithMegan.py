import streamlit as st
from API import API
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

st.set_page_config(page_title="Chat With Megan", page_icon="🧼", layout= "wide")
st.title("Clean Your Data🧼")

if "openai" not in st.session_state:
    st.session_state["openai"] = None

if st.session_state["openai"] is None:
    st.session_state["openai"] = API.verify_api()

if "data" not in st.session_state:
    st.session_state["data"] = None

if st.session_state["data"] is None:
    st.session_state["data"] = API.import_data()

if "clean_data" not in st.session_state:
    st.session_state["clean_data"] = None

if "input_missing_value" not in st.session_state:
    st.session_state["input_missing_value"] = None

if "generate features" not in st.session_state:
    st.session_state["generate features"] = None

if "plot" not in st.session_state:
    st.session_state["plot"] = None

if st.session_state["openai"] is not None and st.session_state["data"] is not None:
    col1, col2, col3 = st.columns([4,2, 4])

    with col1:
            with st.expander("🔎 Dataframe Preview"):
                st.dataframe(st.session_state["data"], use_container_width=True)
    
    with col2:
        if st.button("Clean Data"):
            llm = OpenAI(api_token=st.session_state["openai"])
            df = SmartDataframe(st.session_state["data"], config={"llm": llm})
            col1 = list(df.columns)
            M = df.clean_data()
            d = M.to_dict()
            st.session_state["clean_data"] = pd.DataFrame(d, columns=col1)
            # Save cleaned data
            API.save_to_original_file(st.session_state["clean_data"])
            st.success("Data Cleaned")
        
        if st.button("Impute missing values"):
            # Impute missing values
            llm = OpenAI(api_token=st.session_state["openai"])
            df = SmartDataframe(st.session_state["data"], config={"llm": llm})
            st.session_state["input_missing_value"] = df.impute_missing_values()
           
            API.save_to_original_file(st.session_state["input_missing_value"])
        
        # Generate features
        if st.button("Generate features"):
            llm = OpenAI(api_token=st.session_state["openai"])
            df = SmartDataframe(st.session_state["data"], config={"llm": llm})
            st.session_state["generate features"] = df.generate_features()
            API.save_to_original_file(st.session_state["generate features"])
        
        # Plot histogram
        if st.button("Plot histogram"):
            st.session_state['plot'] = 'hist'
        
        if st.button("Plot Bar Chart"):
            st.session_state['plot'] = 'bar'
        
        if st.button("Scatter Plot"):
            st.session_state['plot'] = 'scatter'
        
        if st.button("Scatter3D Plot"):
            st.session_state['plot'] = 'scatter3D'
        
        if st.button("Line Plot"):
            st.session_state['plot'] = 'line'
            
    with col3:

        if st.session_state["clean_data"] is not None:
            with st.expander("🔎 Clean Dataframe Preview"):
                st.dataframe(st.session_state["clean_data"], use_container_width=True)

        if st.session_state["input_missing_value"] is not None:
            with st.expander("Missing Data Imputed Preview"):
                st.dataframe(st.session_state["input_missing_value"], use_container_width=True)
        
        if st.session_state["generate features"] is not None:
            with st.expander("Generated Features Preview"):
                st.dataframe(st.session_state["generate features"], use_container_width=True)
        
        if st.session_state["plot"] is not None:
            with st.expander("Plot Preview"):
                folder_path = "images"
                if st.session_state["plot"] == 'hist':
                    API.plot_hist()
                
                if st.session_state["plot"] == 'bar':
                    API.plot_bar()
                
                if st.session_state["plot"] == 'scatter':
                    API.plot_scatter()
                
                if st.session_state["plot"] == 'scatter3D':
                    API.plot_scatter3D()
                
                if st.session_state["plot"] == 'line':
                    API.plot_line()
                
    
    
    if st.button("reset"):
        st.session_state["data"] = None
        st.session_state["clean_data"] = None
        st.session_state["messages"] = [{"role": "assistant", "content": "Hi I am Megan. How can I help you?"}]