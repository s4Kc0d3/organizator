# organizator
## Description
This script is used to organize files downloaded into specific folders based on their file extension. It's designed to 
run on macOS, but can be modified to run on other operating systems.

## Usage
1. Download the script and save it to a location on your computer.
2. Open the terminal and navigate to the directory where the script located.
3. Run the following command to execute the script:
   ```python organize.py```

## Features
The script currently supports the following file extensions and corresponding folders:
* `.jpg`, `.jpeg`, `.png`: `Pictures/`
* `.mp3`, `.wav`: `Music/`
* `.mp4`: `Videos/`
* `.gp5`, `.gpx`: `Tabs/`
* `.pdf`: `PDFx/`

If a file has no extension, it's assumed to be a folder and is deleted from the Downloads directory.
Any other file extensions are also deleted from the Downloads directory.

When a picture file is found, it's compressed using the `Pillow` library with a quality of 60 and saved to the 
`Pictures/` directory with a filename starting with "compressed_". The original file is then deleted from the 
Downloads directory.

## Customization
To add additional file extensions and corresponding folders, simply add an `if` statement with the desired file
extension and destination folder to the script.
