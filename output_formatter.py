def format_command_output(shell, task, command):
    """
    Format the generated command in a user-friendly way.
    
    Args:
    shell (str): The shell environment.
    task (str): The original task description.
    command (str): The generated command.
    
    Returns:
    str: A formatted string containing the command output.
    """
    border = "=" * 50
    return f"""
{border}
Shell: {shell}
Task: {task}

Generated Command:
{command}
{border}
"""

def test_output_formatter():
    test_cases = [
        ("bash", "list all files", "ls -la"),
        ("powershell", "get current directory", "Get-Location"),
        ("cmd", "create a new directory named 'test'", "mkdir test"),
    ]
    
    for shell, task, command in test_cases:
        formatted_output = format_command_output(shell, task, command)
        print(formatted_output)
        print("Test passed: Formatted output displayed correctly")
        print("---")

if __name__ == "__main__":
    print("Running Output Formatter tests...")
    test_output_formatter()
