from tools import handle_tool_call, tools
from openai import OpenAI
import json
from artist import artist 
from talker import talker
from config import MODEL

system_message = """
You are a helpful assistant for an Airline called FlightAI.
Give short, courteous answers, no more than 1 sentence.
Always be accurate. If you don't know the answer, say so.
"""

# Initialize OpenAI instance (assuming openai_api_key is set in environment)
openai = OpenAI()

def chat(message, history):
    image = None
    conversation = [{"role": "system", "content": system_message}]
    
    for human, assistant in history:
        conversation.append({"role": "user", "content": human})
        conversation.append({"role": "assistant", "content": assistant})
    conversation.append({"role": "user", "content": message})

    response = openai.chat.completions.create(
        model=MODEL,
        messages=conversation,
        tools=tools
    )

    if response.choices[0].finish_reason == "tool_calls":
        message = tool_call = response.choices[0].message
        response, city = handle_tool_call(message)
        conversation.append(message)
        conversation.append(response)
        image = artist(city)
        response = openai.chat.completions.create(model=MODEL, messages=conversation)

    reply = response.choices[0].message.content
    talker(reply)
    return reply, image
