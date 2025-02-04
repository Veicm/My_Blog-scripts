import os

# path to directory
html_folder = '/path/to/github/folder/'
url = 'https://user_name.github.io/blog/' # add the url to your blog in here

def update_html_files():
	for root, dirs, files in os.walk(html_folder):
		for file in files:
			if file.endswith('.html'):
				html_file = os.path.join(root, file)
				with open(html_file, 'r') as f:
					content = f.read()
				updated_content = replace_image_syntax(content)
				with open(html_file, 'w') as f:
					f.write(updated_content)

def replace_image_syntax(content):
	while '![[' in content and ']]' in content:
		start = content.find('![[') + 3
		end = content.find(']]', start)
		if start != -1 and end != -1:
			image_name = content[start:end]
			img_tag = f'<img src="{url}{image_name}" alt="{image_name}">'
			content = content.replace(f'![[{image_name}]]', img_tag)
		else:
			break
	return content

  

if __name__ == "__main__":
	update_html_files()