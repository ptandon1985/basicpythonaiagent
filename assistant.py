# library that allows Python code to communicate with Ollama Models - pip intall openai
from openai import OpenAI
# library that allows Python code to read configuration from .env file - pip install python-dotenv
from dotenv import load_dotenv
from planner import choose_tool
from tools import get_current_time, roll_dice, generate_password
# library is python os package that allows Python code to read environment variables
import os

# load configuration from .env file
load_dotenv()

# Create Chat client that communicates with Ollama API
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("="*80)
print("      Welcome to the AI Assistant")
print("="*80)

print("\nAI: Hello I am ready to help you")
print("Type 'exit' or 'quit' to end the conversation.\n")
user_messages = []
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the AI Assistant. Goodbye!")
        break
    
    tool_response = choose_tool(user_input)

    result = []

    if tool_response == "get_current_time":
        result = get_current_time()
    elif tool_response == "roll_dice":
        result = roll_dice()
    elif tool_response == "generate_password":
        result = generate_password()
    else:
        result = None


    prompt = f"""
User asked: {user_input}
Tool returned: {result}
Answer the user naturally and concisely.
"""

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[{"role": "user", "content": prompt}]  
    )

    print(f"AI: {response.choices[0].message.content}\n")