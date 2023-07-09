import os
import re
from datetime import datetime

source_directory = "../text/source"
output_directory = "../text/output"

def process_text_files(source_directory, output_directory):
    # Get a list of .txt files in the source directory
    txt_files = [f for f in os.listdir(source_directory) if f.lower().endswith(".txt")]

    # Process each .txt file
    for filename in txt_files:
        # Read the text from the input file
        with open(os.path.join(source_directory, filename), "r") as file:
            text = file.read()

        # Remove symbols and replace middle dashes
        processed_text = re.sub(r"(?<=\w)-\n(?=\w)", "", text)

        # Remove line breaks from inside paragraphs
        paragraphs = processed_text.split("\n\n")
        paragraphs = [re.sub(r"\n", " ", p.strip()) for p in paragraphs]
        processed_text = "\n\n".join(paragraphs)

        # Generate a timestamp for the output filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Define the output filename
        output_filename = f"{os.path.splitext(filename)[0]}-{timestamp}.txt"

        # Write the processed text to the output file
        with open(os.path.join(output_directory, output_filename), "w") as file:
            file.write(processed_text)

process_text_files(source_directory, output_directory)
