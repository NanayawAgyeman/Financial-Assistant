import streamlit as st

def main():
    st.set_page_config(page_title="Financial Advicer 📈")
    st.header("Financial Advicer 📈")

    user_csv = st.file_uploader("upload your csv file", type=csv)


if __name__  == '__main__'":
    main()