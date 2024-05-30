import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# --- Functions ---

def set_system_volume(volume):
    """Sets the system's master volume level.

    Args:
        volume (float): The desired volume level between 0.0 (mute) and 1.0 (max).
    """
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume_interface = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume_interface.SetMasterVolume(volume, None)

# --- Main Script ---

cap = cv2.VideoCapture(1)  # Use 0 for default camera, 1 for external camera
detector = FaceMeshDetector(maxFaces=1)

# Define volume levels based on distance ranges
volume_levels = {
    (50, 80): 0.15,    # Set volume to 15% for distances between 50cm and 80cm
    (90, 100): 0.25,    # Set volume to 25% for distances between 90cm and 100cm
    (110, 115): 0.4,    # Set volume to 40% for distances between 110cm and 115cm
    (130, 145): 0.6,   # Set volume to 60% for distances between 130cm and 145cm
    (160, 180): 0.8,   # Set volume to 80% for distances between 160cm and 180cm
    (200, 400): 1.0    # Set volume to 100% for distances between 200cm and 400cm
}

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        w, _ = detector.findDistance(pointLeft, pointRight)
        d = (6.3 * 840) / w  # Calculate distance

        # Determine volume based on distance
        for distance_range, volume_level in volume_levels.items():
            if distance_range[0] < d <= distance_range[1]:
                current_volume = volume_level
                break
        else:
            current_volume = 0  # Default volume if no range matches

        # Set system volume
        set_system_volume(current_volume)

        # Display information
        volume_text = f'Volume: {int(current_volume * 100)}%'
        cvzone.putTextRect(img, volume_text, (50, img.shape[0] - 50), scale=2)

        # Visualize volume percentage with a bar
        bar_length = int(current_volume * 300)
        cv2.rectangle(img, (50, img.shape[0] - 100), (50 + bar_length, img.shape[0] - 80), (0, 255, 0), -1)
        cv2.rectangle(img, (50, img.shape[0] - 100), (350, img.shape[0] - 80), (255, 255, 255), 2)

        # Display depth
        cvzone.putTextRect(img, f'Depth: {int(d)}cm', (face[10][0] - 100, face[10][1] - 50), scale=2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()