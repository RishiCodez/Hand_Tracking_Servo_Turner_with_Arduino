import cv2
import mediapipe as mp
import serial
import time

# SERIAL: Change this to your port
arduino = serial.Serial('/dev/tty.usbmodem00001', 9600)  # macOS/Linux
# arduino = serial.Serial('COM3', 9600)  # Windows
time.sleep(2)

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def is_thumbs_up(hand_landmarks):
    # Get landmark y-values
    tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    thumb_tip = hand_landmarks.landmark[tips[0]]
    index_tip = hand_landmarks.landmark[tips[1]]
    middle_tip = hand_landmarks.landmark[tips[2]]
    ring_tip = hand_landmarks.landmark[tips[3]]
    pinky_tip = hand_landmarks.landmark[tips[4]]

    # Thumb tip must be above other fingers (lower y value)
    if (thumb_tip.y < index_tip.y and
        thumb_tip.y < middle_tip.y and
        thumb_tip.y < ring_tip.y and
        thumb_tip.y < pinky_tip.y):
        return True
    return False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            if is_thumbs_up(handLms):
                print("👍 Thumbs up detected!")
                arduino.write(b'0\n')  # Move servo to 0°
            else:
                arduino.write(b'90\n')  # Default position

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Thumbs Up Tracker", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break.

cap.release()
cv2.destroyAllWindows()
arduino.close()