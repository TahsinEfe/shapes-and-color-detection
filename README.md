# Features

* Color Detection: Identifies five different colors: Red, Blue, Green, Yellow, and Orange.

* Shape Detection: Recognizes common geometric shapes, including:
   * Triangle
    * Square
    * Rectangle
    * Hexagon
    * Circle
    * Unknown (for unclassified shapes)
* User Interface: A simple but beautiful GUI that allows users to:
   * Select and analyze video files.
   * Capture real-time camera feeds for object detection.
    * View the detected shapes and colors with dynamically colored bounding boxes.
    * Object Tracking: Draws bounding boxes around detected shapes in the same color as the identified object.
    * Dynamic Thresholding: Uses HSV color space for accurate color segmentation and contour detection.

# Technologies Used

* Python – The core programming language.
* OpenCV – For image processing and object detection.
* Tkinter – For building the graphical user interface.
* NumPy – For efficient numerical operations.

## How to Run the Project

1.  Clone the repository:

```javascript
git clone https://github.com/yourusername/computer-vision-project.git
cd computer-vision-project

```

2.  Install required dependencies:

```javascript
pip install opencv-python numpy

```

3.  Run the GUI:

```javascript
python main_gui.py
```

4.  Choose an option:

* "Select Video": Choose an .mp4 file from your system.
* "Camera Detection": Start live object detection via webcam.


5.  Press q to exit the detection window.

## Project Structure

```javascript
computer-vision-project/
│-- main_gui.py           # The main GUI for user interaction
│-- video.py              # Handles video file processing
│-- project.py            # Handles live camera processing
│-- README.md             # Project documentation
└-- requirements.txt      # List of required dependencies
```
