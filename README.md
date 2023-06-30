# PandaBot

PandaBot is an interactive web application that empowers you to engage in dynamic conversations with your data, unlocking its hidden secrets and revolutionizing the way you analyze and interpret information.

## Introduction

PandaBot combines the power of Langchain and Pandas DataFrame to provide an innovative way of generating Python code based on the conversations you have with your data. By utilizing the Langchain Pandas DataFrame Agent, you can ask questions and prompt PandaBot to generate Python code snippets (LLM generated) that manipulate and analyze the uploaded CSV file.

## Getting Started

To use PandaBot, follow these steps:

1. Install the required dependencies by running the following command:

   ```bash
   pip install streamlit pandas langchain python-dotenv

2. Create a new file named .env in the root directory of your project.
3. Open the .env file and add the following line, replacing YOUR OPENAI API KEY with your actual OpenAI API key:
   
   ```bash
   OPENAI_API_KEY="YOUR OPENAI API KEY"
5. Save the .env file.
6. Open the terminal in the project directory and run:
   
   ```bash
   streamlit run main.py

7. The application will start, and you can access it through your web browser.




