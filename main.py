import sys
import json

def process_form_data_with_model(data):
    # Your logic to process the form data
    print("Received Form Data:", data)

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
