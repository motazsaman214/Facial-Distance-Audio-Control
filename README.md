# Face-Controlled-Volume

This repository contains a Python script that utilizes facial landmark detection to estimate the distance between a user's eyes and a camera. This distance is then used to dynamically adjust the system's audio volume, creating a hands-free volume control system.

## Requirements
- Python 3.x
- OpenCV
- cvzone
- pycaw
## Installation
- Install the required packages using:
 
    ```bash
        pip install -r requirements.txt
    ```
## Usage :
1. Run the script:

        python facial_depth_estimation.py
        
2. The script will open a window displaying the live camera feed.
3. The estimated depth and current volume level will be displayed on the image.
4. Move your face closer or further away from the camera to adjust the system volume.

## How it works
1. The script uses the FaceMeshDetector from cvzone to detect facial landmarks.
2. It calculates the distance between the left and right eye corners.
3. This distance is used to estimate the depth using a pre-defined focal length and a known width of a face.
4. The estimated depth is then mapped to a corresponding volume level based on pre-defined ranges.
5. The system's master volume is adjusted accordingly using the pycaw library.

## Notes
1. The script assumes a known width of the face (6.3 cm).
2. The accuracy of the depth estimation depends on the quality of the camera and the lighting conditions.
3. The script uses a pre-defined focal length, which may need to be calibrated for optimal results.
4. You may need to adjust the volume level ranges defined in the volume_levels dictionary to suit your preferences.
## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.


