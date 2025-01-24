# Prerequisites:
# - A Groq account and API key (https://groq.com/)
# - Python 3.6 or later
# - groq library: pip install groq

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variable
groq_api_key = os.getenv("GROQ_API_KEY")

# Check if the API key is loaded
if not groq_api_key:
    raise ValueError("API key not found. Please set the GROQ_API_KEY environment variable.")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Example query
# Get user input
# Initialize conversation history
conversation_history = [
    {
        "role": "system",
        "content": "you are a helpful assistant."
    }
]

while True:
    user_question = input("Please enter your question (or 'quit' to exit): ")
    
    if user_question.lower() == 'quit':
        break
        
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_question
    })

    # Execute chat completion with temperature and max_tokens
    chat_completion = client.chat.completions.create(
        messages=conversation_history,
        model="llama-3.3-70b-versatile",
        temperature=0.7,  # Adjust temperature for randomness
        max_tokens=100    # Adjust max tokens for response length
    )

    # Get assistant's response
    assistant_response = chat_completion.choices[0].message.content
    
    # Add assistant response to history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_response
    })

    # Print the response
    print("\nAssistant:", assistant_response, "\n")
