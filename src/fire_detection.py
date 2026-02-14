import cv2
import numpy as np

# Start webcam
cap = cv2.VideoCapture(0)

print("🔥 Fire Detection Started...")
print("Press 'q' to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Fire color range (orange/yellow)
    lower = np.array([18, 50, 50])
    upper = np.array([35, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower, upper)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 800:
            x, y, w, h = cv2.boundingRect(cnt)

            # Draw rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            cv2.putText(frame, "🔥 FIRE DETECTED!", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow("Real-Time Fire Detection", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
