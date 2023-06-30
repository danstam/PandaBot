import streamlit as st
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    st.title("PandaBot 🐼📊🤖")
    st.subheader("PandaBot empowers you to engage in dynamic conversations with your data, unlocking its hidden secrets and revolutionizing the way you analyze and interpret information")

    st.header("Prepare to Redefine Your Relationship with Data")

    # Allow the user to upload a CSV file
    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if csv_file is not None:
        st.write(f"🚀 Your data has landed!")

        # Read the uploaded CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Load the OpenAI API key from the environment variable
        openai_api_key = os.getenv("OPENAI_API_KEY")

        # Create an agent for interacting with the pandas DataFrame using OpenAI
        agent = create_pandas_dataframe_agent(OpenAI(temperature=0, openai_api_key=openai_api_key), df, verbose=True)

        st.header("Ask a Prompt about the CSV file")
        user_prompt = st.text_input("Enter your prompt")

        if user_prompt != "":
            with st.spinner(text="In progress..."):
                # Run the user's prompt against the agent to generate a response
                response = agent.run(user_prompt)
                st.write(response)

        st.header("Snapshot of Your Data")
        st.dataframe(df)

if __name__ == "__main__":
    main()
