import argparse
import sys
from query_processor import process_input, format_for_llm

def get_shell_environment():
    """Prompt user to specify the shell environment."""
    shell = input("Please specify your shell environment (e.g., bash, zsh, powershell): ").strip().lower()
    return shell

def get_task_description():
    """Prompt user to describe the task in natural language."""
    task = input("Please describe the task you want to perform: ").strip()
    return task

def main():
    parser = argparse.ArgumentParser(description="CLI for shell task automation")
    parser.add_argument('--shell', help='Specify the shell environment')
    parser.add_argument('--task', help='Describe the task to perform')
    
    args = parser.parse_args()

    if not args.shell:
        args.shell = get_shell_environment()
    
    if not args.task:
        args.task = get_task_description()
    
    try:
        processed_input = process_input(args.shell, args.task)
        llm_query = format_for_llm(processed_input)
        print("Processed input:", processed_input)
        print("Formatted LLM query:", llm_query)
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
