import sys
from openai import OpenAI
import os
from langchain_integration import verify_langchain_openai

def verify_python_version():
    print(f"Python version: {sys.version}")
    assert sys.version_info >= (3, 11), "Python version should be 3.11 or higher"

def verify_langchain():
    import langchain
    print(f"LangChain version: {langchain.__version__}")
    print("LangChain community package is installed and imported successfully.")

def verify_openai_api():
    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Hello, GPT-4o mini!"}],
            max_tokens=10
        )
        print("OpenAI API test successful")
        print(f"Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"Error testing OpenAI API: {e}")
        raise

if __name__ == "__main__":
    print("Verifying development environment setup...")
    
    verify_python_version()
    verify_langchain()
    verify_openai_api()
    verify_langchain_openai()
    
    print("All verifications passed successfully!")
