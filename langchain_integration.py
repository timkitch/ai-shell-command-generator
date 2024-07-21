from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

def verify_langchain_openai():
    try:
        # Initialize ChatOpenAI with GPT-4 Turbo
        chat_model = ChatOpenAI(model_name="gpt-4-turbo-preview")

        # Test the model with a simple query
        messages = [HumanMessage(content="Hello, GPT-4 Turbo via LangChain!")]
        response = chat_model(messages)

        print("LangChain integration with GPT-4 Turbo successful")
        print(f"Response: {response.content}")
    except Exception as e:
        print(f"Error testing LangChain integration with GPT-4 Turbo: {e}")
        raise

def get_shell_command(shell, task):
    chat_model = ChatOpenAI(model_name="gpt-4-turbo-preview")
    messages = [HumanMessage(content=f"Generate a {shell} command to {task}")]
    response = chat_model(messages)
    return response.content
