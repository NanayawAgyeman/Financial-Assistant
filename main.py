import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain_community.llms import OpenAI
import os
from dotenv import load_dotenv
import time


def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Set Streamlit page configuration
    st.set_page_config(page_title="Financial Adviser 📈")
    st.header("Financial Adviser 📈")

    # Allow the user to upload a CSV file
    user_csv = st.file_uploader("Upload your csv file", type="csv")

    # Proceed if a CSV file is uploaded
    if user_csv is not None:
        # Ask the user for a question related to the CSV
        user_question = st.text_input("Ask a question about the csv: ")

        # Initialize OpenAI language model and create CSV agent
        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, user_csv, verbose=True)

        # If the user question is provided
        if user_question is not None and user_question != "":
            # Set the number of retries for API calls
            retry_count = 3

            # Loop for retrying API calls in case of rate-limiting errors
            for attempt in range(retry_count):
                try:
                    with st.spinner(text="In progress..."):
                        # Make an API call to get a response
                        response = agent.run(user_question)

                    # Display the response
                    st.write(response)

                    # Break out of the loop if successful API call
                    break
                except Exception as e:
                    # Handle rate-limiting error
                    if "insufficient_quota" in str(e):
                        st.warning("API rate limit exceeded. Retrying...")
                        time.sleep(2)  # Add a delay before retrying
                    else:
                        # Display other errors and break out of the loop
                        st.error(f"Error: {e}")
                        break

            else:
                # Display an error message if retries are unsuccessful
                st.error("Failed to get a response. Please try again later.")


if __name__ == '__main__':
    # Run the main function if the script is executed
    main()
