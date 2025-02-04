def replace_text_in_single_file(file_path, text_to_remove, text_to_insert):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace(text_to_remove, text_to_insert)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Text '{text_to_remove}' wurde durch '{text_to_insert}' in {file_path} ersetzt.")

if __name__ == "__main__":
    file_path = "/path/to/GitHub/directory/index.html"  # paste the path to the index file in your GitHub directory in here
    text_to_remove = "/posts/" 
    text_to_insert = "/repo_name/posts/"  # paste your repo name in here
    replace_text_in_single_file(file_path, text_to_remove, text_to_insert)

if __name__ == "__main__":
    file_path = "/path/to/GitHub/directory/index.html"  # paste the path to the index file in your GitHub directory
    text_to_remove = "repo_name/repo_name" #paste your repo name both time in here
    text_to_insert = "repo_name"  # paste your repo name in here
    replace_text_in_single_file(file_path, text_to_remove, text_to_insert)