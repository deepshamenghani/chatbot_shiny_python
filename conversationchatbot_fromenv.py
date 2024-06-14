# Install packages if needed
# pip install openai
# pip install python-dotenv

from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
# Load your API key from an environment variable
client = OpenAI(api_key=os.getenv('OPENAI_API'))

# Create an instruction for our bot
conversation = [{"role": "system", "content": "You are an assistant."}]

def ask_question(inputquestion):
    # Append the user's question to the conversation array
    conversation.append({"role": "system","content": inputquestion})

    # Request gpt-3.5-turbo for chat completion or a response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Access the response from the API to display it
    assistant_response = response.choices[0].message.content

    return assistant_response
