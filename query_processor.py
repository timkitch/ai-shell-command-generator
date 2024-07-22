import re

def process_input(shell, task):
    """
    Process and validate user inputs.
    
    Args:
    shell (str): The shell environment specified by the user.
    task (str): The task description provided by the user.
    
    Returns:
    dict: A dictionary containing the processed inputs.
    """
    # Validate shell input
    valid_shells = ['cmd', 'powershell', 'bash']
    if shell.lower() not in valid_shells:
        raise ValueError(f"Invalid shell. Please choose from {', '.join(valid_shells)}")
    
    # Clean and validate task input
    cleaned_task = clean_task_input(task)
    if not cleaned_task:
        raise ValueError("Task description cannot be empty")
    
    return {
        "shell": shell.lower(),
        "task": cleaned_task
    }

def clean_task_input(task):
    """Clean the task input by removing extra whitespace and special characters."""
    # Remove leading/trailing whitespace and convert to lowercase
    cleaned = task.strip().lower()
    # Remove special characters except spaces and alphanumeric
    cleaned = re.sub(r'[^a-z0-9\s]', '', cleaned)
    # Replace multiple spaces with a single space
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned

def format_for_llm(processed_input):
    """
    Format the processed input for LLM query.
    
    Args:
    processed_input (dict): The dictionary containing processed inputs.
    
    Returns:
    str: A formatted string for LLM query.
    """
    return f"Generate a {processed_input['shell']} command to {processed_input['task']}"

# Basic tests
def run_tests():
    # Test 1: Valid input
    try:
        result = process_input("bash", "list all files")
        assert result == {"shell": "bash", "task": "list all files"}, "Test 1 failed"
        print("Test 1 passed")
    except Exception as e:
        print(f"Test 1 failed: {str(e)}")

    # Test 2: Invalid shell
    try:
        process_input("invalid_shell", "list all files")
        print("Test 2 failed: Should have raised ValueError")
    except ValueError:
        print("Test 2 passed")

    # Test 3: Empty task
    try:
        process_input("bash", "   ")
        print("Test 3 failed: Should have raised ValueError")
    except ValueError:
        print("Test 3 passed")

    # Test 4: LLM formatting
    try:
        formatted = format_for_llm({"shell": "powershell", "task": "create a new directory"})
        assert formatted == "Generate a powershell command to create a new directory", "Test 4 failed"
        print("Test 4 passed")
    except Exception as e:
        print(f"Test 4 failed: {str(e)}")

if __name__ == "__main__":
    run_tests()
