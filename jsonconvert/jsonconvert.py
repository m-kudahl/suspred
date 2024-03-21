import json
import os

def process_git_output(file_path):
    git_data = []
    with open(file_path, 'r') as f:
        current_data = ''
        for line in f:
            # If the line is not empty, append it to the current data
            if line.strip():
                current_data += line
            else:
                # If the line is empty, parse the accumulated data as JSON
                try:
                    git_data.append(json.loads(current_data))
                except json.decoder.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}. Skipping line.")
                current_data = ''
        
        # Parse any remaining data at the end of the file
        if current_data:
            try:
                git_data.append(json.loads(current_data))
            except json.decoder.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}. Skipping line.")

    # Process the parsed git data
    for index, data in enumerate(git_data):
        process_git_data(data, index)

def process_git_data(git_data, index):
    # Here you can process each git_data object as needed
    # For example, you can access specific fields of the git_data dictionary
    # and perform any analysis or manipulation required
    print("Processing git data:")
    print(json.dumps(git_data, indent=4))  # Example: printing the parsed data
    
    # Save the parsed JSON data to a new file
    output_file_path = f"parsed_data_{index}.json"
    with open(output_file_path, 'w') as outfile:
        json.dump(git_data, outfile, indent=4)
    print(f"Processed data saved to {output_file_path}")

# Example usage
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    git_output_file_path = os.path.join(current_dir, 'incubator-crail_commit_git.txt')
    process_git_output(git_output_file_path)
