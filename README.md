## IMAGE COMPRESSION
Author: Melody Tanyaradzwa Tsekeni
LinkedIn: https://www.linkedin.com/in/melody-tanya-tsekeni-1a2b29119/
Email: tanyatsekenie@gmail.com

## Project Overview
The Image Compression Tool is a desktop application built with Python using the Tkinter library. This tool allows users to compress images while preserving a specified level of quality. It supports multiple image formats and allows users to choose the quality percentage before compressing the image, ensuring flexibility between file size and image quality.

This tool is especially useful for those looking to optimize image file sizes for web use, emails, or storage without significantly compromising on quality.

## Features
- User-Friendly GUI: A clean and simple graphical interface powered by Tkinter, making it easy for users to navigate.
- Select Image: The user can select an image file of various formats (JPEG, PNG, BMP, GIF, etc.) for compression.

- Image Quality Control: The app provides a dropdown menu with quality percentage options (20%, 40%, 50%, 60%, 70%, 80%, and 90%), allowing users to control the level of compression applied to the image.

- Image Path Display: The selected image's path is displayed in the app so that users can confirm the correct file is chosen.

- Real-Time Compression: Once an image is selected and a quality level is chosen, the user can compress the image with the click of a button.

- Navy Blue Themed UI: The application features a modern and elegant navy blue theme for the entire interface.

- Multiple Image Formats Supported: Compress images in formats such as JPEG, PNG, BMP, and GIF.

## Technology Used
- Python: The core programming language used to build the application.
- Tkinter: Python's standard GUI library, used for building the graphical interface.
- Pillow (PIL): Python Imaging Library, used to handle image file manipulation and compression.

## How It Works
1. Select an Image: Click the "Select Image" button and choose an image from your computer.

2. View the File Path: The file path of the selected image will be displayed in the app to confirm the correct file.

3. Choose Image Quality: Select the desired image quality from the dropdown menu (from 20% to 90%). The default is set to 60%.

4. Compress the Image: Click the "Compress Image" button, and the app will compress the image based on the selected quality.

5. Save the Compressed Image: After compression, a save dialog will appear allowing you to save the compressed image with the desired name and location.

### Prerequisities
- Python 3.x: Ensure that Python is installed on your computer.
- You can download it from the official Python website: https://www.python.org/downloads/.
- Pillow (PIL): The Python Imaging Library, used to manipulate images

### How to Run the Application
1. Clone the repository or dwnload the source code:

git clone https://github.com/Mia-Tee/image_compression.git

2. Navigate to the project directory:

cd image_compression_tool

3. Install the required dependencies (if not already installed):

pip install pillow

4. Run the application:

python CompressIt.py

## Usage
- Image Formats Supported: JPEG, PNG, BMP, GIF.
- Select Image: Choose an image from your local storage.
- Choose Compression Quality: Pick a percentage value from the dropdown menu to set the desired compression quality.
- Compress: Click "Compress Image" to reduce the image size.
- Save: Save the compressed image to a desired location.

## Future Enhancements
- Batch Compression: Add functionality to allow users to compress multiple images at once.
- Additional Image Formats: Support additional image formats such as TIFF, WebP, etc.
- Advanced Compression Settings: Provide advanced options like resizing images or adjusting specific parameters like brightness or contrast.
- Progress Bar: Add a progress bar to show the compression process for larger images.

## Contribution
Contributions are welcome! Feel free to submit issues or pull requests to improve the tool.

## How to Contribute
1. Fork the repository.

2. Create a feature branch (git checkout -b feature-branch).

3. Commit your changes (git commit -am 'Add some feature').

4. Push to the branch (git push origin feature-branch).

5. Create a new Pull Request.
