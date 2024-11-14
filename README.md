# Bee Image Annotation Tool

## Project Overview

This project is a web-based tool for annotating bee images using bounding boxes. It allows users to view images of bees, select images for cropping, and modify the bounding boxes using the Cropper.js library. The tool is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend.

## Features

- **Image Gallery**: Display a gallery of bee images with annotated bounding boxes.
- **Image Cropping**: Users can click on an image to open it in a modal for cropping.
- **Bounding Box Editing**: Users can adjust the bounding boxes using Cropper.js and save the updated coordinates.
- **Live Updates**: Bounding boxes are updated dynamically after saving changes without needing to reload the page.

## Installation

### Prerequisites

- Python 3.x
- Flask
- Jinja2 (included with Flask)
- jQuery
- Cropper.js

### Setting Up the Project

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set Up a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install flask
    ```

4. **Prepare the Dataset**:
    - Place your bee images in the `all_datasets/images/` directory.
    - Place the corresponding label files (in YOLO format) in the `all_datasets/labels/` directory.

5. **Run the Flask Application**:
    ```bash
    python app.py
    ```
    - The application will be available at `http://127.0.0.1:5000/`.

## Directory Structure

```plaintext
├── app.py                  # Flask application
├── static
│   ├── css
│   │   ├── style.css       # Custom styles
│   │   └── cropper.css     # Cropper.js styles
├── templates
│   └── gallery.html        # HTML template for the gallery
├── all_datasets            # Directory containing images and labels
│   ├── images              # Bee images
│   └── labels              # YOLO format labels
├── README.md               # Project documentation
└── venv                    # Virtual environment
```
## Code Explanation
### app.py

*   **Purpose**: Backend logic for loading images and labels, serving images, and saving updated labels.
    
*   **Routes**:
    
    *   /: Renders the gallery of images.
        
    *   /images/: Serves the image files.
        
    *   /save-coordinates/: Saves the updated label coordinates after cropping.
        
    *   /replace-labels/: Replaces all label data for a given image.
        

### gallery.html

*   **Purpose**: Frontend template for displaying the image gallery.
    
*   **Key Components**:
    
    *   **Gallery Grid**: Displays images with their associated bounding boxes.
        
    *   **Modal**: Opens when an image is clicked, allowing the user to crop the image and adjust the bounding boxes.
        
    *   **JavaScript Functions**:
        
        *   updateBoundingBoxes(): Dynamically updates the bounding boxes on the image.
            
        *   save-button.onclick: Saves the updated bounding box data and updates the display without refreshing the page.

### cropper.css

*   **Purpose**: Custom styling for the modal and Cropper.js interface.
    

### style.css

*   **Purpose**: Custom styling for the gallery and overall layout.
    

## Usage Instructions
1. **Run the code**:
```bash
python3 app.py
```
3.  **View Images**: Open the application in your browser. The gallery of images will be displayed with bounding boxes.
    
4.  **Edit Bounding Boxes**:
    
    *   Click on an image to open the cropping modal.
        
    *   Adjust the bounding box as needed using Cropper.js.
        
    *   Click "Save" to update the bounding box. The changes will be reflected immediately in the gallery.
        
5.  **Save Coordinates**: The coordinates are automatically sent to the server and saved to the respective label file.
    

## Troubleshooting
*   **Bounding Boxes Not Updating**: Ensure that the AJAX request is successfully sending the updated labels to the server and that the server is correctly updating the label files.
    
*   **Image Not Displaying**: Check that the image files are correctly placed in the all\_datasets/images/ directory and that their filenames match the label files.
    

## Future Improvements
*   **Multiple Bounding Boxes**: Extend the functionality to allow multiple bounding boxes per image.
    
*   **Undo/Redo**: Implement undo/redo functionality for easier adjustments.
    
*   **User Authentication**: Add user authentication for secure access to the annotation tool.
    

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
