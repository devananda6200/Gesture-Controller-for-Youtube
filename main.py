import cv2

# Try multiple camera indexes
for i in range(3):  # Try 0, 1, 2
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Webcam found at index {i}")
        break
else:
    print("❌ Could not find a working webcam.")
    exit()

while True:
    success, img = cap.read()

    if not success or img is None:
        print("❌ Failed to grab frame. Exiting.")
        break

    cv2.imshow("Webcam Feed", img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
