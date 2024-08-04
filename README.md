# Staff Internal Self Service Bot

This project is an  Internal Self Service Bot designed to answer internal staff questions of a company, the goal is to address staff questions as quickly as possible without having to go through several difficulties ,questions about policies , benefits departments etc. The project  leverages  LangChain with  Retrieval-Augmented Generation (RAG) concept to address staffs question from a prepared data( a dummy dataset generated ),also uses the  Groq API and googleAPI as alternates for large language model choice, a question endpoint was also developed using FastAPI to receive staff questions and return answers based on context using the chat history , and finally Streamlit for the UI.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Contact](#contact)

## Project Overview
The  Internal staff Self Service Bot is built to assist internal staff by providing quick and accurate answers to HR-related questions. The bot leverages the LangChain framework for language processing, integrates with the Groq API for advanced AI capabilities, uses Retrieval-Augmented Generation (RAG) for enhanced information retrieval, and provides an interactive UI using Streamlit. The bot also incorporates conversation history to maintain context across interactions.

## Features
- Interactive Q&A interface via streamit
- Natural language understanding and processing (LLM)
- Retrieval-Augmented Generation (RAG) for accurate information retrieval from dataset
- Conversation history for context-aware responses 


## Installation

### Prerequisites
- Python 3.7 or higher
- Virtualenv
- Groq api key


### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/Haggai-ik/RAG_AI_SELF_SERVICE_BOT.git
    cd hr-self-service-bot
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    
     

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Start the FastAPI server:
    ```bash
    uvicorn api.endpoint:app --reload
    ```

2. Run the Streamlit application:
    ```bash
    streamlit run Streamlit/app.py
    ```

3. Open your browser and go to `http://localhost:8501` to interact with the internal Self Service Bot.


## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.


## Contact
For any questions or feedback, please contact:
- Ike Haggai Reward
- Email: haggaiike@gmail.com
- GitHub: [Haggai-ik](https://github.com/Haggai-ik)  
