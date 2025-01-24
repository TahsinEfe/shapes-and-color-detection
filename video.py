import cv2
import numpy as np
from tkinter import Tk, filedialog

colors = {
    "Red": [(0, 100, 100), (10, 255, 255), (0, 0, 255)],  
    "Blue": [(100, 150, 0), (140, 255, 255), (255, 0, 0)],   
    "Green": [(40, 50, 50), (80, 255, 255), (0, 255, 0)],   
    "Yellow": [(20, 100, 100), (30, 255, 255), (0, 255, 255)], 
    "Orange": [(10, 100, 100), (20, 255, 255), (0, 165, 255)], 
}

def detect_shape(contour):
    approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    if len(approx) == 3:
        return "Triangle"
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)    
        if 0.95 <= aspect_ratio <= 1.05:
            return "Square"
        else:
            return "Rectangle"
    elif len(approx) == 6:
        return "Hexagon"
    else:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        circularity = 4 * np.pi * (area / (perimeter * perimeter))
        if circularity > 0.1:
            return "Circle"
        else:
            return "Unknown"

def select_video_file():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\Efe\\Desktop\\archive\\videos", title="Select a Video File", filetypes=[("MP4 files", "*.mp4")])
    return file_path

def detect_color(hsv, contour):
    mask = np.zeros(hsv.shape[:2], dtype="uint8")
    cv2.drawContours(mask, contour, -1, 255, -1)
    mean_color = cv2.mean(hsv, mask=mask)[:3]

    for color_name, (lower, upper, bgr) in colors.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        if lower[0] <= mean_color[0] <= upper[0] and lower[1] <= mean_color[1] <= upper[1]:
            return color_name, bgr
    return "Unknown", (255, 255, 255)  

def main():
    video_path = select_video_file()

    if video_path:
        cap = cv2.VideoCapture(video_path)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            for color_name, (lower, upper, bgr_color) in colors.items():
                mask = cv2.inRange(hsv_frame, np.array(lower), np.array(upper))
                contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                
                for contour in contours:
                    if cv2.contourArea(contour) < 1500:
                        continue
                    
                    shape_name = detect_shape(contour)
                    _, bgr_color = detect_color(hsv_frame, contour)
                    
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), bgr_color, 2)
                    label = f"{color_name}, {shape_name}"
                    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, bgr_color, 2)

            cv2.imshow("Video Detection", frame)
            cv2.imshow("mask", mask)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    else:
        print("No video file selected.")

if __name__ == "__main__":
    main()
