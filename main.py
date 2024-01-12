import os
import sys
import json

def process_form_data_with_model(data):
    # Your logic to process the form data
    query = data["word"]
    settings = data["settings"]

    # Getting the list of documents from the path
    path = settings["path"]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print("Received Form Data:", files)

if __name__ == "__main__":
    try:
        # Read JSON data from the command-line arguments
        data = sys.argv[1]
        data = json.loads(data)

        # Process the form data
        process_form_data_with_model(data)

        # Optionally, print a success message
        print("Form Data Processing Successful")

    except Exception as e:
        # Handle errors
        print("Error:", str(e))
