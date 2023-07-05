import os
import re

source_directory = "/app/images/source"

try:
    # Get a list of all image files in the source directory
    image_files = [f for f in os.listdir(source_directory) if f.lower().endswith(('.jpg', '.jpeg'))]
    
    print("Source length", len(image_files))
    # Rename the files
    for filename in image_files:
        # Extract the numeric part from the filename
        match = re.search(r'\d+', filename)
        if match:
            number = match.group()
            print("Page Number", number)
            new_filename = f'{int(number):03d}.jpg'
            old_path = os.path.join(source_directory, filename)
            new_path = os.path.join(source_directory, new_filename)

            try:
                os.rename(old_path, new_path)
                print(f'✅ Renamed: {filename} -> {new_filename}')
            except Exception as e:
                print(f'❌ An error occurred during the renaming process.')
                print(f'Exception: {str(e)}')
        else:
            print(f'❌ Could not find a numeric part in the filename: {filename}')
except Exception as e:
    print("❌ An error occurred during the renaming process.")
    print("Exception:", str(e))
