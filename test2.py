def create_phrase_dictionary(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove leading and trailing whitespace from each line
    lines = [line.strip() for line in lines]

    # Filter out empty lines
    phrases = [line for line in lines if line]

    # Check if there are any phrases before creating the dictionary
    if not phrases:
        print("No phrases found in the text.")
        return {}

    # Create a dictionary with phrases and their positions
    phrase_dict = {f'Phrase {i + 1}': phrase for i, phrase in enumerate(phrases)}

    return phrase_dict

result_dict = create_phrase_dictionary(r"C:\Users\seqqal\Desktop\etapes.txt")
for key, value in result_dict.items():
    print(f'{key}: {value}')