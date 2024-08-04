# GeminiTerminal

GeminiTerminal is an intelligent terminal assistant for macOS, leveraging the Google Gemini API to enhance user experience by automating system commands and integrating various apps for improved productivity.

## Features

1. **Command Execution:** Proposes, seeks approval for, and executes system commands, providing the output to the user.
2. **App Integration Example - News Summarization:** Fetches top news articles via NewsAPI and summarizes them using the Gemini API. This demonstrates the potential for integrating various apps into the OS.
3. **Dynamic Interaction:** Maintains a chat session, dynamically processing user inputs and responding using the Gemini API's capabilities.

## Prerequisites

- Python
- Google Gemini API key
- NewsAPI key

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/GeminiTerminal.git
   cd GeminiTerminal

## Install Required Libraries

pip install google-generativeai requests

## Add API Keys

Gemini API Key: Replace 'your_gemini_api_key' with your actual Gemini API key in the following line:
genai.configure(api_key='your_gemini_api_key')

## NewsAPI Key
Replace 'your_newsapi_key' with your actual NewsAPI key in the news_articles_app function:
newsapi_url = "your_newsapi_key"(use tthis link for generating your key- https://newsapi.org)

## Run the App
Execute the script in your terminal:
python Gemini_terminal.py
