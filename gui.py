import tkinter as tk
from tkinter import filedialog, messagebox
from video import main as video_main
from camera import main as camera_main

class gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Vision Project")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f8ff")

        title_label = tk.Label(root, text="Color and Shape Detection", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#4682b4")
        title_label.pack(pady=10)


        subtitle_label = tk.Label(root, text="Name: Tahsin Efe YILMAZ | Student No: 22MISY1015", font=("Arial", 14), bg="#f0f8ff", fg="#6a5acd")
        subtitle_label.pack(pady=5)

        select_video_btn = tk.Button(root, text="Select Video to Detect", command=self.run_video_script, font=("Arial", 14), bg="#4682b4", fg="white", width=20)
        select_video_btn.pack(pady=10)
        
        camera_btn = tk.Button(root, text="Select Camera Detection", command=self.run_camera_script, font=("Arial", 14), bg="#4682b4", fg="white", width=20)
        camera_btn.pack(pady=10)

        exit_btn = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 14), bg="#ff4500", fg="white", width=20)
        exit_btn.pack(pady=20)

    def run_video_script(self):
        try:
            video_main()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while running the video script: {e}")

    def run_camera_script(self):
        try:
            camera_main()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while running the camera script: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = gui(root)
    root.mainloop()
