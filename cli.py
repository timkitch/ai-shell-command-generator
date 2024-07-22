import argparse
import sys
import pyperclip
from query_processor import process_input, format_for_llm
from langchain_integration import get_shell_command
from output_formatter import format_command_output

def copy_to_clipboard(text):
    """Copy the given text to the clipboard and inform the user."""
    pyperclip.copy(text)
    print("Command copied to clipboard.")

def get_shell_environment():
    """Prompt user to select the shell environment from a list of valid options."""
    valid_shells = ["cmd", "powershell", "bash"]
    print("Please select your shell environment:")
    for i, shell in enumerate(valid_shells, 1):
        print(f"{i}. {shell}")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(valid_shells):
                return valid_shells[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

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
        
        # Send query to LLM and get response
        generated_command = get_shell_command(processed_input['shell'], processed_input['task'])
        formatted_output = format_command_output(processed_input['shell'], processed_input['task'], generated_command)
        print(formatted_output)
        
        # Ask user if they want to copy the command
        copy_choice = input("Would you like to copy the command to clipboard? (yes/no): ").strip().lower()
        if copy_choice == 'yes':
            copy_to_clipboard(generated_command)
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while processing the query: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
