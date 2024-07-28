import tkinter as tk
from tkinter import messagebox
import os

def generate_prompt():
    action = action_entry.get("1.0", tk.END).strip()
    subject = subject_entry.get("1.0", tk.END).strip()
    purpose = purpose_entry.get("1.0", tk.END).strip()
    keywords = keywords_entry.get("1.0", tk.END).strip()
    headers = headers_entry.get("1.0", tk.END).strip().splitlines()
    important = important_entry.get("1.0", tk.END).strip()
    model = model_var.get()

    if not action or not subject or not purpose or not headers:
        messagebox.showerror("Input Error", "Action, Subject, Purpose, and Headers are required fields.")
        return

    # Format headers for JSON structure
    header_fields = ""
    for header in headers:
        header_fields += f'        "{header}": "[response]",\n'

    # Remove trailing comma from the last header field
    header_fields = header_fields.rstrip(",\n")

    # Formatting the prompt
    prompt = f"""Task: {action} {subject} {purpose}

Keywords: {keywords.splitlines()}

Extract:

{headers}

Model: {model}

Output Format: Provide the data in valid JSON format, structured as follows:
[
    {{"Title": "A title summarized from the task"}},
    {{
{header_fields}
    }},
    {{
{header_fields}
    }}
]

Important:
{important}
"""
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, prompt)

    # Write the generated prompt to prompt.txt in the root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, '..'))

    prompt_file_path = os.path.join(root_dir, 'prompt.txt')
    with open(prompt_file_path, 'w') as f:
        f.write(prompt)
    messagebox.showinfo("Success", f"Prompt saved to {prompt_file_path}")

    # Schedule the window to close after 5 seconds
    root.after(5000, root.destroy)

# GUI setup
root = tk.Tk()
root.title("Custom Prompt Generator")

# Task Section
task_frame = tk.LabelFrame(root, text="Task (Action / Subject / Purpose)", padx=10, pady=10)
task_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

tk.Label(task_frame, text="Action:").grid(row=0, column=0, sticky=tk.W)
action_entry = tk.Text(task_frame, height=2, width=50, wrap="word")
action_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(task_frame, text="Subject:").grid(row=1, column=0, sticky=tk.W)
subject_entry = tk.Text(task_frame, height=2, width=50, wrap="word")
subject_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(task_frame, text="Purpose:").grid(row=2, column=0, sticky=tk.W)
purpose_entry = tk.Text(task_frame, height=2, width=50, wrap="word")
purpose_entry.grid(row=2, column=1, padx=10, pady=5)

# Keywords Section
tk.Label(root, text="Keywords: (one per line)").grid(row=1, column=0, sticky=tk.W)
keywords_entry = tk.Text(root, height=5, width=50, wrap="word")
keywords_entry.grid(row=1, column=1, padx=10, pady=5)

# Headers Section
tk.Label(root, text="Headers to Extract: (one per line)").grid(row=2, column=0, sticky=tk.W)
headers_entry = tk.Text(root, height=5, width=50, wrap="word")
headers_entry.grid(row=2, column=1, padx=10, pady=5)

# Model Selection Section
tk.Label(root, text="Select Model:").grid(row=3, column=0, sticky=tk.W)
model_var = tk.StringVar(value="gpt-3.5-turbo")
model_options = ["gpt-3.5-turbo", "gpt-4o", "gpt-4o-mini", "gpt-4-turbo"]
model_menu = tk.OptionMenu(root, model_var, *model_options)
model_menu.grid(row=3, column=1, padx=10, pady=5)

# Important Notes Section
tk.Label(root, text="Important Notes: (optional)").grid(row=4, column=0, sticky=tk.W)
important_entry = tk.Text(root, height=3, width=50, wrap="word")
important_entry.grid(row=4, column=1, padx=10, pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Prompt", command=generate_prompt)
generate_button.grid(row=5, column=1, pady=10)

# Result Text Field
tk.Label(root, text="Generated Prompt:").grid(row=6, column=0, sticky=tk.W)
result_text = tk.Text(root, height=10, width=50, wrap="word")
result_text.grid(row=6, column=1, padx=10, pady=5)

root.mainloop()
