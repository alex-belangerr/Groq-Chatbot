# Chatbot with Flask and HTML Frontend

This project is a simple chatbot application built with **Flask** as the backend and a basic **HTML/CSS/JavaScript** frontend. The chatbot utilizes the **Groq API** for conversational responses. You can interact with the chatbot through a web interface.

---

## Features
- Web-based chat interface for interacting with the chatbot.
- Backend API built with Flask to process user inputs and fetch chatbot responses.
- Integration with the **Groq API** for generating responses.
- Conversation history management to maintain context.
- Easy-to-run locally for testing and development.

---

## Requirements

- **Python 3.6 or later**
- **Node.js** (optional, for advanced frontend development)
- **Groq API Key** (sign up at [Groq](https://groq.com/) to get your API key)

---

## Installation

1\. Clone the Repository
-----------------------------
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
2\. Set Up Python Environment
-----------------------------

1.  Install the required Python dependencies:

    bash

    CopyEdit

    `pip install -r requirements.txt`

2.  Create a `.env` file in the project directory and add your **Groq API Key**:

    dotenv

    CopyEdit

    `GROQ_API_KEY=your_groq_api_key_here`

* * * * *

3\. Run the Flask App
---------------------

Start the Flask backend by running:

bash

CopyEdit

`python app.py`

The Flask app will be available at `http://127.0.0.1:5000`.

* * * * *

4\. Open the Frontend in a Browser
----------------------------------

1.  Open the `index.html` file in your browser.
2.  Ensure your browser allows JavaScript execution for local files. (For Chrome, you may need to enable a flag for `file://` URLs.)
3.  Type a message into the chatbox and click **Send** (or press Enter) to test the chatbot.

