import streamlit as st
from langchain.agents import create_csv_agent
from landchain.llms import OpenAI
from dotenv import load_dotenv

def main():

    load_dotenv()
    
    st.set_page_config(page_title="Financial Advicer 📈")
    st.header("Financial Advicer 📈")

    user_csv = st.file_uploader("upload your csv file", type="csv")

    if user_csv is not None:
        user_question = st.text_input("Ask a question about the csv: ")


if __name__  == '__main__':
    main()