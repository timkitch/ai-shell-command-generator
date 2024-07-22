from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate

def verify_langchain_openai():
    try:
        # Initialize ChatOpenAI with GPT-4 Turbo
        chat_model = ChatOpenAI(model_name="gpt-4o-mini")

        # Test the model with a simple query
        messages = [HumanMessage(content="Hello, GPT-4 Turbo via LangChain!")]
        response = chat_model(messages)

        print("LangChain integration with GPT-4 Turbo successful")
        print(f"Response: {response.content}")
    except Exception as e:
        print(f"Error testing LangChain integration with GPT-4 Turbo: {e}")
        raise

def get_shell_command(shell, task):
    chat_model = ChatOpenAI(model_name="gpt-4o-mini")
    
    prompt_template = PromptTemplate(
        input_variables=["shell", "task"],
        template="""Generate a {shell} command to {task}. 
        Ensure the command is syntactically correct for the {shell} environment.
        Return only the command, without any explanations, additional text, or code formatting."""
    )
    
    prompt = prompt_template.format(shell=shell, task=task)
    messages = [HumanMessage(content=prompt)]
    response = chat_model(messages)
    
    # Clean up the response
    cleaned_command = response.content.strip()
    # Remove any markdown code block formatting if present
    cleaned_command = cleaned_command.replace('```' + shell, '').replace('```', '').strip()
    # Remove any leading shell prompt characters if present
    cleaned_command = cleaned_command.lstrip('$ ').lstrip('> ').strip()
    
    return cleaned_command

def test_command_generation():
    test_cases = [
        ("bash", "list all files", "ls -la"),
        ("powershell", "get current directory", "Get-Location"),
        ("cmd", "create a new directory named 'test'", "mkdir test"),
    ]
    print("Note: The expected outputs are based on GPT-4 Turbo. Results may vary with gpt-4o-mini.")
    
    for shell, task, expected_output in test_cases:
        generated_command = get_shell_command(shell, task)
        print(f"Shell: {shell}")
        print(f"Task: {task}")
        print(f"Generated command: {generated_command}")
        print(f"Expected output: {expected_output}")
        print("Test passed" if generated_command.lower() == expected_output.lower() else "Test failed")
        print("---")

if __name__ == "__main__":
    print("Running Command Generation Engine tests...")
    test_command_generation()
