import cv2
import mediapipe as mp
import pyautogui
import pygetwindow as gw
import time

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

cap = cv2.VideoCapture(0)
last_action_time = 0
cooldown = 1.5  # seconds
gesture = "None"  # Initialize outside to persist across frames

# Function to focus YouTube window
def focus_youtube_tab():
    for window in gw.getWindowsWithTitle("YouTube"):
        try:
            if window.isMinimized:
                window.restore()
            window.activate()
            time.sleep(0.4)  # Give time to focus
            break
        except:
            continue

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # Mirror view
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    fingers = []

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        lm_list = []
        h, w, _ = img.shape
        for lm in hand_landmarks.landmark:
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append((cx, cy))

        if lm_list:
            # Thumb
            if lm_list[4][0] > lm_list[3][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other fingers
            for i in range(1, 5):
                if lm_list[tip_ids[i]][1] < lm_list[tip_ids[i] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            current_time = time.time()

            if fingers == [1, 0, 0, 0, 0]:  # Thumb up
                gesture = "Play"
                if current_time - last_action_time > cooldown:
                    focus_youtube_tab()
                    pyautogui.press('k')
                    last_action_time = current_time

            elif fingers == [0, 0, 0, 0, 0]:  # Fist
                gesture = "Pause"
                if current_time - last_action_time > cooldown:
                    focus_youtube_tab()
                    pyautogui.press('k')
                    last_action_time = current_time

            elif fingers == [0, 1, 0, 0, 0]:  # Index up
                gesture = "Forward"
                if current_time - last_action_time > cooldown:
                    focus_youtube_tab()
                    pyautogui.press('l')
                    last_action_time = current_time

            elif fingers == [0, 0, 1, 0, 0]:  # Middle up
                gesture = "Backward"
                if current_time - last_action_time > cooldown:
                    focus_youtube_tab()
                    pyautogui.press('j')
                    last_action_time = current_time

        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.putText(img, f'Gesture: {gesture}', (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("YouTube Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
