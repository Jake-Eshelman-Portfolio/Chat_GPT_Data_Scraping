## Overview
This project demonstrates how to use OpenAI's API to generate responses using the gpt-3.5-turbo model and save the output to an Excel file. It consists of a Python script that reads a prompt from a text file, sends it to the OpenAI API, and writes the response to an Excel file in a specific format.

The project was generated to assist with my personal research on topics, but I am currently working to customize it to be generalizable. Future improvements include:
1. Making the fields it returns more easily configurable
2. Addressing problems with hallucination or adding secondary validation to information
3. Making the prompt more customizable

## Prerequisites
- Python 3.x
- An OpenAI API key
- openai Python package
- openpyxl Python package

## Installation

1. **Clone the repository**:
   git clone <repository-url>
   cd <repository-directory>
   
2. **Set up the virtual environment** (optional):
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\\Scripts\\activate
   
3. **Install the required packages**:
   pip install openai openpyxl pyhthon-dotenv
   
4. **Set up the configuration**:
IMPORTANT -- DO NOT REVEAL YOUR API KEY 
   - Create a .env file in the root directory in the format:
     OPENAI_API_KEY=your_API_key

5. **Prepare the prompt file**:
   - Modify the prompt file to fit your specifications

## Usage
The script will:

   - Read the prompt from prompt.txt.
   - Send the prompt to the OpenAI API and get a response.
   - Convert the response (expected to be a JSON string) into a list of dictionaries.
   - Write the response data to an Excel file located in the data directory, named responses.xlsx.

## Expected Response Format
The response from the OpenAI API should be a JSON string representing a list of dictionaries. Each dictionary should contain the following keys:
- "Company"
- "Contact"
- "Role"
- "Phone Number"
- "Location"
- "Factors to Qualify Lead"

## Error Handling
- If the response is not a valid JSON string or not a list of dictionaries, the script will print an error message and exit.
