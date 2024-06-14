# Install packages if needed
# pip install openai
# pip install python-dotenv

from openai import OpenAI
import os

# Create an instruction for our bot
conversation = [{"role": "system", "content": "You are an assistant."}]

def ask_question(inputquestion, api_key):
    # Initialize the OpenAI client with the provided API key
    client = OpenAI(api_key=api_key)

    # Append the user's question to the conversation array
    conversation.append({"role": "user", "content": inputquestion})

    # Request gpt-3.5-turbo for chat completion or a response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Access the response from the API to display it
    assistant_response = response.choices[0].message.content

    return assistant_response