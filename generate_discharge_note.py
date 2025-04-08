#!/usr/bin/env python3

import json
import os
import sys
from pathlib import Path
from openai import OpenAI

def load_consult_data(file_path):
    """Load consultation data"""
    with open(file_path, 'r') as f:
        return json.load(f)

def generate_discharge_note(consult_data):
    """Generate a discharge note using llm api"""
    
    # Initialize OpenAI client with DeepSeek API
    client = OpenAI(
        api_key=os.getenv('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com"
    )

    
 
    prompt = f"""You are a veterinary assistant tasked with generating a professional, friendly, and easy-to-understand discharge note for a pet owner. 

    Based on the consultation details below, write a summary that includes:
    - The reason for the visit and what was observed
    - Any treatments or procedures performed
    - Medications or prescriptions provided
    - Specific care instructions for the pet at home
    - Clear next steps, including follow-ups or warnings

    Make sure the note is concise, informative, and appropriate for a non-medical audience.

    ---

    Patient Information:
    - Name: {consult_data['patient']['name']}
    - Species: {consult_data['patient']['species']}
    - Breed: {consult_data['patient']['breed']}
    - Gender: {consult_data['patient']['gender']}
    - Weight: {consult_data['patient']['weight']}

    Consultation Details:
    - Date: {consult_data['consultation']['date']}
    - Reason for Visit: {consult_data['consultation']['reason']}
    - Visit Type: {consult_data['consultation']['type']}

    Clinical Notes:
    {consult_data['consultation']['clinical_notes']}

    Treatments Provided:
    - Procedures: {consult_data['consultation']['treatment_items']['procedures']}
    - Medications: {consult_data['consultation']['treatment_items']['medicines']}
    - Prescriptions: {consult_data['consultation']['treatment_items']['prescriptions']}
    - Foods: {consult_data['consultation']['treatment_items']['foods']}
    - Supplies: {consult_data['consultation']['treatment_items']['supplies']}

    Diagnostics/Tests Conducted:
    {consult_data['consultation']['diagnostics']}

    ---

    Write the discharge note as if you are addressing the pet owner directly, using warm, supportive and naturallanguage. Format it with clear headings and bullet points where appropriate."""


    # Call DeepSeek API
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a veterinary assistant helping to generate discharge notes for pet owners."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500,
        stream=False
    )
    
    return response.choices[0].message.content.strip()

def save_discharge_note(discharge_note, input_file):
    """Save the discharge note to a JSON file in the discharge_note dir."""
    # Create 
    discharge_note_dir = Path("solution")
    discharge_note_dir.mkdir(exist_ok=True)

    # Generate output filename
    input_filename = Path(input_file).stem
    output_file = discharge_note_dir / f"{input_filename}_output.json"

    # Save the discharge note
    output_data = {"solution": discharge_note}
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 generate_discharge_note.py <path_to_consultation_json>")
        sys.exit(1)

    input_file = sys.argv[1]
    
    try:
        # Load consultation data
        consult_data = load_consult_data(input_file)
        
        # Generate discharge note
        discharge_note = generate_discharge_note(consult_data)
        
        # Save the discharge note
        save_discharge_note(discharge_note, input_file)
        
        print(f"Discharge note generated successfully and saved to solution/{Path(input_file).stem}_output.json")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 