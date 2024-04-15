import os

def delete_files_by_extension(directory, extension):
    try:
        if not os.path.exists(directory):
            print(f"Error: Directory '{directory}' does not exist.")
            return
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(extension.lower()):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")

        print("Deletion completed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

PATH = input("Enter path: ")
FILETYPE = input("Enter file type: ")

delete_files_by_extension(PATH, FILETYPE)
