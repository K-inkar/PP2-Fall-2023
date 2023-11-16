# 1.Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def list_items_in_path(target_path):
    directories = [d for d in os.listdir(target_path) if os.path.isdir(os.path.join(target_path, d))]
    files = [f for f in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, f))]
    all_items = os.listdir(target_path)

    return directories, files, all_items

def main():
    user_path = input("Enter the path: ")
    directories, files, all_items = list_items_in_path(user_path)

    print(directories)
    print(files)
    print(all_items)

if __name__ == "__main__":
    main()

# 2.Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os

def check_path_permissions(user_path):
    exists = os.path.exists(user_path)
    readable = os.access(user_path, os.R_OK)
    writable = os.access(user_path, os.W_OK)
    executable = os.access(user_path, os.X_OK)
    return exists, readable, writable, executable

def main():
    user_path = input("Enter the path: ")
    exists, readable, writable, executable = check_path_permissions(user_path)
    
    print(exists)
    print(readable)
    print(writable)
    print(executable)

if __name__ == "__main__":
    main()


# 3.Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

def analyze_path():
    path = input("Enter the path: ")
    
    if os.path.exists(path):
        dirname, filename = os.path.split(path)
        print(f"Path exists.")
        print(f"Directory: {dirname}")
        print(f"Filename: {filename}")
    else:
        print(f"Path '{path}' does not exist.")
analyze_path()


# 4.Write a Python program to count the number of lines in a text file.
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            print(f"The number of lines in '{filename}' is: {line_count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_name = input()
    count_lines(file_name)


# 5.Write a Python program to write a list to a file.
def write_list_to_file(filename, my_list):
    try:
        with open(filename, 'w') as file:
            for item in my_list:
                file.write(str(item) + '\n')
        print(filename)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        input_list_str = input("Enter a list:")
        input_list = [item.strip() for item in input_list_str.split(',')]
        file_name = input("Enter the filename:")
        write_list_to_file(file_name, input_list)

    except Exception as e:
        print(f"An error occurred: {e}")


# 6.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os
import string

def generate_files():
    try:
        for letter in string.ascii_uppercase:
            filename = f"{letter}.txt"
            with open(filename, 'w') as file:
                file.write(filename)
        print("Text files generated successfully.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        current_directory = os.getcwd()
        os.chdir(current_directory)
        generate_files()
    except Exception as e:
        print(e)
    finally:
        os.chdir(current_directory)


# 7.Write a Python program to copy the contents of a file to another file
def copy_content(src_file, dest_file):
    with open(src_file, 'r') as src:
        content = src.read()
        with open(dest_file, 'w') as dest:
            dest.write(content)

def main():
    src_file = "source_text.txt"
    dest_file = "destination_text.txt"
    copy_content(src_file, dest_file)

if __name__ == "__main__":
    main()


# 8.Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

def remove_file(file_to_remove):
    if os.path.exists(file_to_remove):
        os.remove(file_to_remove)
        print(f"File: '{file_to_remove}' deleted successfully.")
    else:
        print(f"Error: File: '{file_to_remove}' not found.")

def execute_deletion():
    file_to_delete = input("Enter the path of the file to delete: ")

    if os.access(file_to_delete, os.F_OK):
        remove_file(file_to_delete)
    else:
        print(f"Error: File: '{file_to_delete}' not found.")

if __name__ == "__main__":
    execute_deletion()

