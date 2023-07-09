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

def cleanDirectories():
    print(f"⌛️ About to clean the following directories:")
    directories = [
        '../images/output',
        '../images/temp',
        '../text/output'
    ]
    
    # Delete the contents of each directory
    for directory in directories:
        delete_directory_contents(directory)
        print(f"✅ Clean ${directory}")
        
cleanDirectories()