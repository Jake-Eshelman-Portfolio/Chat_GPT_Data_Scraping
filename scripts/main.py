from openai import OpenAI
import openpyxl
import sys
import os
import json

config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config'))
sys.path.append(config_path)

import config

client = OpenAI(
    api_key=config.OPENAI_API_KEY
)

def get_chatgpt_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", #gpt-4o, gpt-3.5-turbo
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Write responses to an Excel file
def write_to_excel(data):
    script_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.abspath(os.path.join(script_path, '..', 'data', 'responses.xlsx'))

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Add headers
    sheet["A1"] = "Company"
    sheet["B1"] = "Contact"
    sheet["C1"] = "Role"
    sheet["D1"] = "Phone Number"
    sheet["E1"] = "Location"
    sheet["F1"] = "Factors to Qualify Lead"

    # Write data
    for i, entry in enumerate(data, start=2):
        sheet[f"A{i}"] = entry["Company"]
        sheet[f"B{i}"] = entry["Contact"]
        sheet[f"C{i}"] = entry["Role"]
        sheet[f"D{i}"] = entry["Phone Number"]
        sheet[f"E{i}"] = entry["Location"]
        sheet[f"F{i}"] = entry["Factors to Qualify Lead"]

    # Save the workbook
    workbook.save(data_path)

def main():
    # Read the prompt from a text file
    script_path = os.path.dirname(os.path.abspath(__file__))
    prompt_path = os.path.abspath(os.path.join(script_path, '..', 'prompt.txt'))
    with open(prompt_path, 'r') as file:
        prompt = file.read()

    data = []
    response = get_chatgpt_response(prompt)
    
    # Response must be a JSON string that can be converted into a list of dictionaries
    try:
        response_list = json.loads(response.strip())
        if isinstance(response_list, list):
            data.extend(response_list)
        else:
            print("Error: Response is not a list")
            return
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return


    write_to_excel(data)

if __name__ == "__main__":
    main()