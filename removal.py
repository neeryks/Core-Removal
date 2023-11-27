import os
import sys
from bs4 import BeautifulSoup
import chardet
from tqdm import tqdm

def remove_script_tags_with_url(html_content, url):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all script tags with the specified URL
    script_tags_to_remove = soup.find_all('script', attrs={'src': lambda s: s and url in s})
    
    # Remove the script tags from the soup
    for script_tag in script_tags_to_remove:
        script_tag.extract()

    # Return the modified HTML content
    return str(soup)

def remove_lines(html_content, lines_to_remove):
    lines = html_content.split('\n')
    # Remove lines containing the specified strings
    modified_lines = [line for line in lines if not any(line_to_remove in line for line_to_remove in lines_to_remove)]
    # Join the modified lines back into HTML content
    return '\n'.join(modified_lines)

def process_html_file(file_path, url_to_remove, lines_to_remove):
    # Check if the file has an HTML extension
    if not file_path.lower().endswith('.html'):
        return

    # Detect file encoding using chardet
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    file_encoding = result['encoding']

    # Read the HTML content from the file with the detected encoding
    with open(file_path, 'r', encoding=file_encoding, errors='replace') as file:
        html_content = file.read()

    # Remove script tags with the specified URL
    modified_html_content = remove_script_tags_with_url(html_content, url_to_remove)

    # Remove lines containing the specified strings
    modified_html_content = remove_lines(modified_html_content, lines_to_remove)

    # Write the modified HTML content back to the file
    with open(file_path, 'w', encoding=file_encoding, errors='replace') as file:
        file.write(modified_html_content)

def process_directory(directory_path, url_to_remove, lines_to_remove):
    # Get the total number of HTML files in the directory and its subdirectories
    html_files = [file for file in os.listdir(directory_path) if file.lower().endswith('.html')]
    total_files = len(html_files)

    # Iterate through all files in the directory and its subdirectories
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in tqdm(filenames, desc="Processing Files", unit="file", total=total_files):
            file_path = os.path.join(foldername, filename)
            process_html_file(file_path, url_to_remove, lines_to_remove)

def main():
    # Check if the directory path is provided as a command-line argument
    if len(sys.argv) != 2:
        print('Usage: python script.py <directory_path>')
        sys.exit(1)

    # Get the directory path from the command-line argument
    directory_path = sys.argv[1]

    # Specify the URL to be removed from script tags
    url_to_remove = 'findablees.com'

    # Specify the lines added by HTTrack to be removed
    httrack_lines_to_remove = ['What to remove']

    # Process all HTML files in the directory and its subdirectories
    process_directory(directory_path, url_to_remove, httrack_lines_to_remove)

    print(f'Script tags with URL "{url_to_remove}" and Your Lines lines removed from HTML files in {directory_path}')

if __name__ == "__main__":
    main()
