import os

# Path to the directory containing the images
source_directory = "/app/images/source"
temp_directory = "/app/images/temp"
output_directory = "/app/images/output"

print("Source Directory", source_directory, len(os.listdir(source_directory)))
print("Temp Directory", temp_directory, len(os.listdir(temp_directory)))

while True:
    print("Server running")