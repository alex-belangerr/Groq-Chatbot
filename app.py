import os
from flask import Flask, request, jsonify
from groq import Groq
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variable
groq_api_key = os.getenv("GROQ_API_KEY")

# Check if the API key is loaded
if not groq_api_key:
    raise ValueError("API key not found. Please set the GROQ_API_KEY environment variable.")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Initialize Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Initialize conversation history
conversation_history = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]

# API endpoint for chatbot
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Parse user message from the request JSON
        data = request.json
        user_message = data.get('message')

        if not user_message:
            return jsonify({'error': 'Message field is required'}), 400

        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Execute chat completion with Groq API
        chat_completion = client.chat.completions.create(
            messages=conversation_history,
            model="gemma2-9b-it",
            temperature=0.7,
            max_tokens=100
        )

        # Get assistant's response
        assistant_response = chat_completion.choices[0].message.content

        # Add assistant response to history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_response
        })

        # Limit conversation history to prevent token overload
        max_history_length = 10
        if len(conversation_history) > max_history_length:
            conversation_history[:] = conversation_history[-max_history_length:]

        # Return the assistant's response
        return jsonify({'response': assistant_response})

    except Exception as e:
        print(f"Error: {e}")  # Log error for debugging
        return jsonify({'error': str(e)}), 500


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
