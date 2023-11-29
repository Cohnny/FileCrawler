import os


# Opens a file and compare its content with the keyword the user entered. Throws an error if it fails to read.
def search_in_file(path, answer):
    try:
        # Encodes the text to make åäö possible to read
        with open(path, 'r', encoding='utf-8') as text:
            # Remove .lower() to make it case sensitive
            content = text.read().lower()
            # Remove .lower() to make it case sensitive.
            # Remove .strip() to remove whitespace check on input.
            if answer.lower().strip() in content:
                return True
            else:
                return False
    except Exception as e:
        print(f"Error: {e}. Can't open file at path: {path}")


# Takes a path and loops through the directory checking for files.
# When all files are checked it then loops through the directory looking for a folder.
# If a folder is found the function calls itself with the new folder path and starts over.
def search_in_folder(path, answer):
    initial_path = path
    items = os.listdir(initial_path)
    found_files = []

    for item in items:
        current_path = os.path.join(initial_path, item)
        if os.path.isfile(current_path):
            found = search_in_file(current_path, answer)
            if found:
                print(current_path)
                found_files.append(current_path)
                # return uncomment if you only want the first file containing the keyword to be shown.

    for item in items:
        current_path = os.path.join(initial_path, item)
        if os.path.isdir(current_path):
            found_files += search_in_folder(current_path, answer)

    return found_files


# Asks user for input, changes the current directory to '\TestData', sets new path and then calls the search function.
def main():
    answer = input("Enter a keyword: ")
    os.chdir('TestData')
    current_path = os.getcwd()

    search_in_folder(current_path, answer)


if __name__ == '__main__':
    # Calls the main function to get the program started.
    main()
