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
    
    # Process and validate task input
    processed_task = clean_task_input(task)
    if not processed_task:
        raise ValueError("Task description cannot be empty")
    
    return {
        "shell": shell.lower(),
        "task": processed_task
    }

def clean_task_input(task):
    """Clean the task input while preserving special characters."""
    # Remove leading/trailing whitespace and replace multiple spaces with a single space
    cleaned = ' '.join(task.split())
    return cleaned

def format_for_llm(processed_input):
    """
    Format the processed input for LLM query.
    
    Args:
    processed_input (dict): The dictionary containing processed inputs.
    
    Returns:
    str: A formatted string for LLM query.
    """
    return f"Generate a {processed_input['shell']} command to {processed_input['task']}. Preserve the exact case and special characters for any terms in quotes."

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

    # Test 5: Preserving hyphens and quoted content
    try:
        result = process_input("bash", 'search for "GPT-4o" and create-directory')
        assert result == {"shell": "bash", "task": 'search for "GPT-4o" and create-directory'}, "Test 5 failed"
        print("Test 5 passed")
    except Exception as e:
        print(f"Test 5 failed: {str(e)}")

if __name__ == "__main__":
    run_tests()
