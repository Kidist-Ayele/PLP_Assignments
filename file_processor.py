# Simple File Read & Write Program for Beginners
# This program reads a file and creates a modified version

def main():

    # Ask user for filename
    filename = input("Enter the name of the file to read: ")
    filename = f"PLP_Assignments/{filename}"
    # Try to read the file
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(f"Successfully read {len(lines)} lines from {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return
    except:
        print(f"Error: Could not read file '{filename}'")
        return
    
    # Modify the content (add line numbers)
    modified_lines = []
    for i in range(len(lines)):
        line_number = i + 1
        modified_line = f"Line {line_number}: {lines[i]}"
        modified_lines.append(modified_line)
    
    # Create output filename
    output_filename = filename.replace('.txt', '_modified.txt')
    if output_filename == filename:
        output_filename = filename + '_modified.txt'
    
    # Write the modified content to new file
    try:
        with open(output_filename, 'w') as file:
            for line in modified_lines:
                file.write(line)
        print(f"Successfully created: {output_filename}")
        print("File processing completed!")
    except:
        print(f"Error: Could not write to {output_filename}")


main()
