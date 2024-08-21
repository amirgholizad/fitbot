# Fitbot

Fitbot is a conversational chatbot designed to provide personalized advice on fitness programs, workout plans, diets, and nutrition. It leverages the power of GPT-3.5-turbo for natural language understanding and FastAPI for a robust backend.

## Features

- **Personalized Fitness Advice**: Get tailored workout plans based on your fitness level and goals.
- **Nutritional Guidance**: Receive recommendations for diet plans, meal suggestions, and tips on maintaining a balanced diet.
- **Conversational Interface**: Engage in natural, human-like conversations with Fitbot.
- **Scalable Backend**: Powered by FastAPI, ensuring quick responses and easy deployment.

## Installation

To get started with Fitbot, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/fitbot.git
    cd fitbot
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    Create a `.env` file in the root directory with the following content:
    ```plaintext
    OPENAI_API_KEY=your-openai-api-key
    ```

4. **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```

5. **Access Fitbot**:
    Open your web browser and go to `http://localhost:8000` to start interacting with Fitbot.

## Usage

Once Fitbot is up and running, you can ask it various questions related to fitness and nutrition, such as:

- "What's a good workout plan for building muscle?"
- "Can you suggest a diet for weight loss?"
- "How many calories should I eat per day?"

## Project Structure

```
fitbot/
│
├── bot.py               # The main FastAPI back-end and GPT3.5-turbo app
├── config.py            # Confiuration file
├── static/              # Static files (CSS, JS, etc.)
├── templates/           # HTML templates
├── data.txt             # Data-set fit to GPT3.5-turbo
└── README.md            # Project documentation
```

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.


## Acknowledgements

- [OpenAI](https://openai.com) for providing the GPT-3.5-turbo API.
- [FastAPI](https://fastapi.tiangolo.com) for the excellent web framework.
```
