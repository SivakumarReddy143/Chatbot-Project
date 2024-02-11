import streamlit as st
import numpy as np
import pandas as pd
import os
from PIL import Image
import io
import plotly.express as px

class API:
    
    @staticmethod
    def verify_api():
            key = st.text_input("Enter OpenAI API key", type="password")
            if key is not None:
                if st.button("Verify"):
                    st.success("API is set")
                    return key
    
    @staticmethod
    def import_data():
        input_csv = st.file_uploader("Upload your CSV file", type=['csv'], accept_multiple_files=False)
        if input_csv is not None:
            try:
                df = pd.read_csv(input_csv, encoding= 'latin1')
                new_col = list(df.columns)
                df.columns = new_col
                return df
            except:
               try:
                   df = pd.read_csv(input_csv)
                   new_col = list(df.columns)
                   df.columns = new_col
                   return df
               except:
                   st.error("Please upload a valid CSV file")
    
    @staticmethod
    def import_another_data():
        another_csv = st.file_uploader("Upload Another CSV file", type=['csv'], accept_multiple_files=False)
        if another_csv is not None:
            try:
                df1 = pd.read_csv(another_csv, encoding= 'latin1')
                new_col1 = list(df1.columns)
                df1.columns = new_col1
                return df1
            except:
               try:
                   df1 = pd.read_csv(another_csv)
                   new_col1 = list(df1.columns)
                   df1.columns = new_col1
                   return df1
               except:
                   st.error("Please upload a valid CSV file")
    
    @staticmethod
    def remove_files():
        folder_path = "images"
        # Get a list of all files in the folder
        file_names = os.listdir(folder_path)
        # Remove each file
        for file_name in file_names:
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)
    
    @staticmethod
    def save_image(img_path):
        img = np.array(Image.open(img_path))
        img = Image.fromarray(img)
        # Convert PIL Image to bytes
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        # Create a download button
        st.download_button(label="Save Image", data=img_bytes, file_name='processed_image.png', mime='image/png', key=None)
    
    @staticmethod
    def save_to_original_file(df1):
        if df1 is not None:
            if st.button("Save To Original Dataframe"):
                st.session_state["data"] = df1

    
    @staticmethod
    def plot_hist():
        if st.session_state["data"] is not None:
            df = st.session_state["data"]
            col = list(df.select_dtypes(include=[np.number]).columns)
            chosen_col = st.selectbox("Select Column", col)

            # Check if a column is chosen
            if chosen_col:
                try:
                    # Create histogram using Plotly Express
                    bin = st.sidebar.slider("Bins", 5, 200, 10)
                    fig = px.histogram(df, 
                                       x=chosen_col,
                                       y = None, 
                                       title=f"{chosen_col} histogram", 
                                       nbins=bin, 
                                       template="plotly_dark", 
                                       color_discrete_sequence=px.colors.sequential.Plasma)

                    
                    # Display the plot
                    st.subheader(f"Histogram of {chosen_col}")
                    st.plotly_chart(fig)

                except Exception as e:
                    st.error(e)
    
    @staticmethod
    def plot_bar():
        if st.session_state["data"] is not None:
            df = st.session_state["data"]
            num_col = list(df.select_dtypes(include=[np.number]).columns)
            obj_col = list(df.select_dtypes(exclude=[np.number]).columns)
            chosen_num_col = st.sidebar.selectbox("Select Column", num_col)
            chosen_obj_col = st.sidebar.selectbox("Select Column", obj_col)

            # Check if a column is chosen
            if chosen_num_col and chosen_obj_col:
                try:
                    fig = px.bar(df, 
                                       x=chosen_obj_col,
                                       y = chosen_num_col, 
                                       title=f"{chosen_obj_col} vs {chosen_num_col}", 
                                       template="plotly_dark", 
                                       color_continuous_scale=px.colors.sequential.Plasma)

                    
                    # Display the plot
                    st.subheader(f"{chosen_obj_col} vs {chosen_num_col}")
                    st.plotly_chart(fig)

                except Exception as e:
                    st.error(e)
    @staticmethod
    def plot_scatter():
        if st.session_state["data"] is not None:
            df = st.session_state["data"]
            num_col1 = list(df.select_dtypes(include=[np.number]).columns)
            num_col2 = list(df.select_dtypes(include=[np.number]).columns)

            chosen_num_col1 = st.sidebar.selectbox("Select Column1", num_col1)
            chosen_num_col2 = st.sidebar.selectbox("Select Column2", num_col2)

            # Check if a column is chosen
            if chosen_num_col1 and chosen_num_col2:
                try:
                    fig = px.scatter(df, 
                                       x=chosen_num_col1,
                                       y = chosen_num_col2, 
                                       title=f"{chosen_num_col1} vs {chosen_num_col2}", 
                                       template="plotly_dark", 
                                       color_continuous_scale=px.colors.sequential.Plasma)

                    
                    # Display the plot
                    st.subheader(f"{chosen_num_col1} vs {chosen_num_col2}")
                    st.plotly_chart(fig)

                except Exception as e:
                    st.error(e)
    
    @staticmethod
    def plot_scatter3D():
        if st.session_state["data"] is not None:
            df = st.session_state["data"]
            col1 = list(df.columns)
            col2 = list(df.columns)
            col3 = list(df.columns)

            chosen_col1 = st.sidebar.selectbox("Select Column1", col1)
            chosen_col2 = st.sidebar.selectbox("Select Column2", col2)
            chosen_col3 = st.sidebar.selectbox("Select Column3", col2)

            # Check if a column is chosen
            if chosen_col1 and chosen_col2 and chosen_col3:
                try:
                    fig = px.scatter_3d(df, 
                                       x=chosen_col1,
                                       y = chosen_col2,
                                       z = chosen_col3, 
                                       title=f"{chosen_col1} vs {chosen_col2} vs {chosen_col3}", 
                                       template="plotly_dark", 
                                       color_continuous_scale=px.colors.sequential.Plasma)

                    
                    # Display the plot
                    st.subheader(f"{chosen_col1} vs {chosen_col2} vs {chosen_col3}")
                    st.plotly_chart(fig)

                except Exception as e:
                    st.error(e)
    
    @staticmethod
    def plot_line():
        if st.session_state["data"] is not None:
            df = st.session_state["data"]
            col1 = list(df.columns)
            col2 = list(df.columns)

            chosen_col1 = st.sidebar.selectbox("Select Column1", col1)
            chosen_col2 = st.sidebar.selectbox("Select Column2", col2)

            # Check if a column is chosen
            if chosen_col1 and chosen_col2:
                try:
                    fig = px.line(df, 
                                       x=chosen_col1,
                                       y = chosen_col2, 
                                       title=f"{chosen_col1} vs {chosen_col2}", 
                                       template="plotly_dark"
                                )

                    
                    # Display the plot
                    st.subheader(f"{chosen_col1} vs {chosen_col2}")
                    st.plotly_chart(fig)

                except Exception as e:
                    st.error(e)
        



