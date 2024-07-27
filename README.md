## Overview
This project demonstrates how to use OpenAI's API to generate responses using the gpt-3.5-turbo model and save the output to an Excel file. It consists of a Python script that reads a prompt from a text file, sends it to the OpenAI API, and writes the response to an Excel file in a specific format. ChatGPT can make mistakes, be sure to validate important info. 

The project was generated to assist with my personal research on topics, but I am currently working to customize it to be generalizable. Potentially useful topics to use it for:
1. Identifying potential business partnership collaborators
2. Sourcing supplies for components, supply chain management
3. Investor outreach
4. Market research, competetor analysis
5. Recruitment
6. Job searching
7. Finding organizations to get involved with related to a specific topic
8. Sales and distribution channel expansion

Ongoing Work:
1. Making the fields it returns more easily configurable. Currently this must be done through modifying the prompt.txt
2. Addressing problems with hallucination or adding secondary validation to information
3. Making the prompt more customizable
4. Allow better output format as currently new outputs overwrite old outputs.
5. Expand the script to enable handling over larger number of outputs. Currently successful up to 10 contacts generated per prompt but ocassionally fails with larger generations.

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
IMPORTANT -- DO NOT REVEAL YOUR API KEY. Ensure that it is placed only in the .env file you create.
   - Create a .env file in the root directory in the format:
    OPENAI_API_KEY=your_API_key

5. **Prepare the prompt file**:
   - Modify the prompt file to fit your specifications

## Usage
1. Before using the script modify the prompt.txt to fit your needs. For an example see prompt.txt. JSON keys represent excel columns and the values 
will be the data that ChatGPT provides. Overall the script will:

   - Read the prompt from prompt.txt.
   - Send the prompt to the OpenAI API and get a response.
   - Convert the response (expected to be a JSON string) into a list of dictionaries.
   - Write the response data to an Excel file located in the data directory, named responses.xlsx.


## Error Handling
- If the response is not a valid JSON string or not a list of dictionaries, the script will print an error message and exit.
