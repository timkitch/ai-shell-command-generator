# Shell Command Generator

## Description

This application is a CLI tool that generates shell commands based on natural language task descriptions. It supports multiple shell environments (Windows Command Prompt, PowerShell, and Bash) and uses OpenAI's GPT-4 model to generate accurate and context-appropriate commands.

## Features

- Supports multiple shell environments (cmd, PowerShell, Bash)
- Uses natural language processing to understand task descriptions
- Generates shell commands using OpenAI's GPT-4o mini model
- Colorized output for better readability
- Option to copy generated commands to clipboard

## Core Technologies

- Python 3.11+
- LangChain for AI model integration
- OpenAI's GPT-4o mini model (multimodal capabilities)
- Colorama for terminal color output
- Pyperclip for clipboard functionality

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/timkitch/ai-shell-command-generator
   cd shell-command-generator
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Copy `.env-example` to `.env`
   - Replace the placeholder API key in `.env` with your actual OpenAI API key

5. Obtaining an OpenAI API key:
   - Go to https://platform.openai.com/signup
   - Create an account or sign in
   - Navigate to the API keys section
   - Generate a new API key
   - Copy the key and paste it into your `.env` file

## Usage

Run the application using the following command:

```
python cli.py
```

You will be prompted to:
1. Select your shell environment (cmd, PowerShell, or Bash)
2. Describe the task you want to perform

The application will then generate a suitable command and display it with formatting. You'll have the option to copy the command to your clipboard.

Alternatively, you can specify the shell and task directly as command-line arguments:

```
python cli.py --shell bash --task "list all files in the current directory"
```

## Development

To run tests and verify the setup:

1. Run the query processor tests:
   ```
   python query_processor.py
   ```

2. Run the output formatter tests:
   ```
   python output_formatter.py
   ```

3. Run the LangChain integration tests:
   ```
   python langchain_integration.py
   ```

4. Verify the development environment setup:
   ```
   python verify_setup.py
   ```

5. Ensure your `.env` file is properly configured with your OpenAI API key

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
