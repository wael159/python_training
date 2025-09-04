import os
import shutil
import openai
import json

openai.api_key = "YOUR_API_KEY"

source = os.path.expanduser("~/Downloads")
destination = os.path.expanduser("~/Organized_Files_AI")
os.makedirs(destination, exist_ok=True)

# Get all filenames
filenames = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]

# Prepare prompt
prompt = f"""
You are a file organizer. I will give you a list of filenames. 
For each file, suggest a single short category it belongs to (like Finance, Music, Videos, Documents, Data, Presentations, Archives, Images, Other). 
Return the result as a JSON object in this format: {{ "filename": "category" }}.

Filenames: {filenames}
"""

# Call OpenAI
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0
)

# Get model response and parse JSON
model_output = response['choices'][0]['message']['content'].strip()

try:
    file_categories = json.loads(model_output)
except json.JSONDecodeError:
    print("Error parsing JSON from model output")
    file_categories = {}

# Move files
for file, category in file_categories.items():
    file_path = os.path.join(source, file)
    if os.path.isfile(file_path):
        category_folder = os.path.join(destination, category)
        os.makedirs(category_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(category_folder, file))
        print(f"Moved {file} → {category}")
