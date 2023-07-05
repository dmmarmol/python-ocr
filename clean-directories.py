import os
import shutil

def delete_directory_contents(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print(f'Deleted: {file_path}')
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {str(e)}')

output_directory = '/app/images/output'
temp_directory = '/app/images/temp'

# Delete the contents of the output directory
delete_directory_contents(output_directory)

# Delete the contents of the temp directory
delete_directory_contents(temp_directory)
