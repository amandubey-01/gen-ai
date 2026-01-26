# Streaming.
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def stream_chat_completion(prompt):
    """
    Stream a chat completion from OpenAI's API.
    Args: 
        prompt (str): The user's prompt/question
    """

    print ("Assistant")
    # Create a streaming chat completion.
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a poetic assistant"},
            {"role": "user", "content": prompt}
        ],
        stream=True # Enable streaming, default is false.
    )

    # Process the stream.
    full_response = ""
    for chunk in stream:
        print
        # Extract the content from chunk
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
            full_response += content
            
    print("\n")# new line after completion
    return full_response

stream_chat_completion("Write a short haiku about a rainy evening.")