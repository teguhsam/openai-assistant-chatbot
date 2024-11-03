import json
from config import openai

# Ticket price lookup table
ticket_prices = {"london": "$799", "paris": "$899", "tokyo": "$1400", "berlin": "$499"}

def get_ticket_price(destination_city):
    city = destination_city.lower()
    return ticket_prices.get(city, "Unknown")

def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)
    city = arguments.get('destination_city')
    price = get_ticket_price(city)
    response = {
        "role": "tool",
        "content": json.dumps({"destination_city": city, "price": price}),
        "tool_call_id": message.tool_calls[0].id
    }
    return response, city

# Tool definition to use in the chatbot
PRICE_FUNCTION_DESC = """
Get the price of a return ticket to the destination city. Call this whenever you need to know the ticket price, 
for example when a customer asks 'How much is a ticket to this city'
"""
price_function = {
    "name": "get_ticket_price",
    "description": PRICE_FUNCTION_DESC,
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False
    }
}

tools = [{"type": "function", "function": price_function}]
