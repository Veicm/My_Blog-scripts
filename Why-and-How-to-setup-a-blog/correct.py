import os

def replace_text_in_html(root_dir, text_to_remove, text_to_insert):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".html"):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                content = content.replace(text_to_remove, text_to_insert)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"text '{text_to_remove}' become '{text_to_insert}' in {file_path}.")

if __name__ == "__main__":
    root_dir = "/path/to/GitHub/directory" # paste the path to your GitHub directory in here
    text_to_remove = "http://localhost:1313"
    text_to_insert = "https://user.github.io/repo" #paste user name and repo name here
    replace_text_in_html(root_dir, text_to_remove, text_to_insert)