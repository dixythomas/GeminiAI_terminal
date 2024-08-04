import google.generativeai as genai
import subprocess
import re
import os
import requests

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

# Configure the Google Gemini API client
genai.configure(api_key='your_gemini_api_key')

def execute_command(command:str):
    """Executes a system command with user confirmation."""
    print(f"Proposed command to execute: {command}")
    while True:
        approval = input("Do you approve execution? (yes/no): ").strip().lower()
        if approval in ['yes', 'y']:
            try:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                print(result.stdout)
                if result.stderr:
                    print(result.stderr)
                return result.stdout
            except subprocess.CalledProcessError as e:
                print(f"Command failed with error code {e.returncode}")
                print(e.output)
                return f"An error occurred: {e}"
        elif approval in ['no', 'n']:
            print("Command execution cancelled.")
            return None
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def news_articles_app():
    # Fetch Top News from NewsAPI,this is an example of app integration into the Gemini OS
    # Configure the NewsAPI client
    newsapi_url = "your_newsapi_key"
    response = requests.get(newsapi_url)
    data = response.json()
    # Get the content of the top 100 news articles
    contents = [article['content'] for article in data['articles'] if article['content']][:100]
    return contents

#The instructions are for mac os but you can change that to linux,also the news_articles_app can be described as an example for app integrations,user can add customized functions  
#like weather app function,or any functions that can be accesible to the computer,and we can ask Gemini to perform customs tasks on top of it
instruction='you are an AI model inside a mac terminal executing taks requested by the user,you also summarize news articles in 10 points',
# Initialize the Gemini model with the function declaration
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    tools=[execute_command,news_articles_app],
    system_instruction=instruction
)

while True:
    user_input = input("You: ")

    # Start chat session with automatic function calling enabled
    chat = model.start_chat(enable_automatic_function_calling=True)

    # Send message to Gemini and get response
    response = chat.send_message(user_input)

    # Extract the text from the response
    gemini_response = ''.join([part.text for part in response.parts]) if response.parts else ""
    print(f"Gemini: {gemini_response}")

    # Improved command extraction and execution
    match = re.search(r"Execute this command: `(.*)`", gemini_response)
    if match:
        command = match.group(1)
        output = execute_command(command)
        if output:
            print(output)