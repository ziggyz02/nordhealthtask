# Nordhealth Task  🐾  🐾  🐾 
## Veterinary Discharge Note Generator

This tool generates discharge notes from consultation data using DeepSeek's large language model (LLM). It helps automate one of the common workflows at Nordhealth: turning clinical notes into clear, professional instructions for pet owners after a visit.



## What It Does

- Reads structured JSON files containing veterinary consultation data  
- Sends the data to DeepSeek's LLM using a prompt template  
- Receives a human-readable discharge note  
- Saves the note to the `solution/` folder



## Requirements

- Python 3.7 or higher  
- DeepSeek API Key  


## Setup and run

1. Clone this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your DeepSeek API key as an environment variable:
   ```bash
   export DEEPSEEK_API_KEY='your_api_key_here'
   ```
4. Run the script with a path to a consultation JSON file:
   ```bash
   python3 generate_discharge_note.py data/consultation1.json
   ```

The script will generate a discharge note and save it in the `solution` directory with the name `consultation1_output.json`.
