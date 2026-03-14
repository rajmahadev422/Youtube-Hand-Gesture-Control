import cv2
import mediapipe as mp
import time
import pyautogui

# Setup MediaPipe
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Tracking states
current_gesture = "None"
last_triggered_gesture = "None"

def result_callback(result, output_image, timestamp_ms):
  global current_gesture
  if result.gestures:
    current_gesture = result.gestures[0][0].category_name
  else:
    current_gesture = "None"

options = GestureRecognizerOptions(
  base_options=BaseOptions(model_asset_path='gesture_recognizer.task'),
  running_mode=VisionRunningMode.LIVE_STREAM,
  result_callback=result_callback
)

cap = cv2.VideoCapture(0)

is_pause = False

with GestureRecognizer.create_from_options(options) as recognizer:
  while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.flip(frame, 1)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    recognizer.recognize_async(mp_image, int(time.time() * 1000))

    if current_gesture != last_triggered_gesture:
      if current_gesture == "Thumb_Up":
        pyautogui.press("l") 
      
      elif current_gesture == "Thumb_Down":
        pyautogui.press("j")

      elif current_gesture == "Closed_Fist" and not is_pause:
        is_pause = True
        pyautogui.press('k')
      
      elif current_gesture == "Open_Palm" and is_pause:
        is_pause = False
        pyautogui.press('k')
      elif current_gesture == "Victory":
        pyautogui.click(1892,22)

      last_triggered_gesture = current_gesture 
      
    cv2.putText(frame, f"Active: {current_gesture}", (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Gesture Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()