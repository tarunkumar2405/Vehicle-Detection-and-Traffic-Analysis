Vehicle Detection and Traffic Analysis
Overview
This project is a vehicle detection system that uses OpenCV's Haar Cascade Classifier to detect cars from a live video stream. The system processes video data from a mobile phone's camera (acting as an IP camera) to analyze traffic flow in four directions—North, South, East, and West—and provides traffic updates based on vehicle counts in each direction.

Features
Real-time vehicle detection using cars.xml.
Categorizes detected vehicles based on their position in the frame.
Provides traffic analysis for North, South, East, and West directions.
Displays the live feed with bounding boxes around detected vehicles.
Requirements
Python 3.x
OpenCV (cv2)
imutils
Mobile phone with IP Webcam app or similar for live video streaming
Installation
Install required Python libraries:

bash
Copy code
pip install opencv-python imutils
Download the Haar Cascade XML file:

Ensure cars.xml is available in the project directory.
Set up the IP Webcam app on your mobile device:

Install the IP Webcam app from Google Play Store.
Start the server and note the streaming URL (e.g., http://192.168.1.101:8080/video).
Update the cam URL in the code with your mobile's IP Webcam URL:

python
Copy code
cam = cv2.VideoCapture("http://<your-ip>:8080/video")
Usage
Run the script:
bash
Copy code
python vehicle_detection.py
The live video feed will open in a new window with bounding boxes for detected vehicles.
Traffic analysis for North, South, East, and West will be printed in the console.
Press the ESC key to exit the program.
Output
Live Feed: A window displaying the video feed with bounding boxes around detected vehicles.
Console Output: Vehicle counts for North, South, East, and West directions with traffic condition updates.
Future Improvements
Integration with a database to log traffic data.
Enhance detection accuracy using deep learning models like YOLO or SSD.
Add support for detecting multiple vehicle types (e.g., bikes, trucks).
Visualize traffic analysis on a dashboard.
Acknowledgments
Haar Cascade Classifier (cars.xml) is pre-trained for vehicle detection.
Inspired by the accessibility and flexibility of OpenCV for computer vision projects.
