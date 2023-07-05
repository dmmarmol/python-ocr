import pytesseract
from PIL import Image
import os
import traceback
import time
import shutil

# Path to the directory containing the images
source_directory = "/app/images/source"
temp_directory = "/app/images/temp"
output_directory = "/app/images/output"

# Move and process each image in the source directory
for filename in os.listdir(source_directory):
    try:
        print("Before:", len(os.listdir(source_directory)))
        
        # Skip the iteration if the file is not an image
        if not filename.lower().endswith(('.jpg', '.jpeg')):
            print(f"└── ⚠️ Skipped non-image file: {filename}")
            continue
        
        image_path = os.path.join(source_directory, filename)
        
        # Move the image to the temp directory
        temp_image_path = os.path.join(temp_directory, filename)
        shutil.move(image_path, temp_image_path)
        print(f"└── ✅ Moved image: {filename}")
        
        try:
            # Open the image file using PIL
            image = Image.open(temp_image_path)

            # Convert the image to text using pytesseract
            text = pytesseract.image_to_string(image)

            # Print the extracted text
            print("⌛️ Processing image:", filename)
            print("└── Text:", text.strip())
            print("------------------------------------\n")

            # Write the extracted text to a file
            with open(output_directory + "/output.txt", "a") as file:
                file.write(text.strip() + "\n")
            
        except Exception as e:
            print("An exception occurred for image:", filename)
            print("Exception:", str(e))
            traceback.print_exc()

        # Move the processed image back to the source directory
        processed_image_path = os.path.join(source_directory, filename)
        shutil.move(temp_image_path, processed_image_path)
    
    except KeyboardInterrupt:
        print("🛑 Process terminated by user.")
        break
    except Exception as e:
        print("❌ An exception occurred for image:", filename)
        print("Exception:", str(e))
        traceback.print_exc()

# Move all files from temp directory back to source directory
print(f"Moving all files from {temp_directory} to {source_directory}...")
for filename in os.listdir(temp_directory):
    try:
        temp_image_path = os.path.join(temp_directory, filename)
        processed_image_path = os.path.join(source_directory, filename)
        print(f"└── {filename} -> {processed_image_path}")
        shutil.move(temp_image_path, processed_image_path)
    except Exception as e:
        print(f"❌ An exception occurred while moving files back to: {source_directory}")
        print("Exception:", str(e))
        traceback.print_exc()
        
    print("✅ Processing completed. All files moved back to source directory.")
