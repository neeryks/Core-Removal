# HTML Content Processing Script

This Python script processes HTML files within a specified directory and its subdirectories. The script removes script tags with a specified URL and lines containing specified strings added by HTTrack.

## Usage

1. **Install Required Packages:**
   - Before running the script, make sure to install the required Python packages. You can do this by running the following command:

     ```bash
     pip install beautifulsoup4 chardet tqdm
     ```

2. **Run the Script:**
   - Execute the script by providing the directory path as a command-line argument:

     ```bash
     python script.py <directory_path>
     ```

   Replace `<directory_path>` with the path to the directory containing HTML files.

3. **Script Configuration:**
   - Open the script and configure the following variables according to your requirements:

     - `url_to_remove`: Specify the URL to be removed from script tags.
     - `httrack_lines_to_remove`: Specify the lines added by HTTrack to be removed.

## Script Details

The script performs the following tasks:

1. **Script Tag Removal:**
   - Finds and removes script tags with the specified URL (`url_to_remove`) from HTML files.

2. **Line Removal:**
   - Removes lines containing the specified strings (`httrack_lines_to_remove`) added by HTTrack.

3. **Encoding Detection:**
   - Detects the encoding of each HTML file using the `chardet` library.

4. **Processing Progress:**
   - Displays a progress bar using the `tqdm` library while processing HTML files.

## Note

- Ensure that the required Python packages are installed before running the script.
- Backup your HTML files before running the script, as it modifies the content.
- Customize the script variables based on your specific requirements.

Feel free to adapt and use this script to process HTML files according to your needs.
