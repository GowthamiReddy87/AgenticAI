file_name_w = "my_new_file_w.txt"

try:
    with open(file_name_w, 'w') as f:
        f.write("Hello from write mode!\n")
        f.write("This content will overwrite any previous content.\n")
    print(f"File '{file_name_w}' created/overwritten successfully.")

    # Verify content
    with open(file_name_w, 'r') as f:
        print(f"Content of '{file_name_w}':\n{f.read()}")

except IOError as e:
    print(f"Error creating file '{file_name_w}': {e}")