import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame
import os

class PygameMediaPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Media Player")
        self.master.geometry("400x350")
        self.master.configure(bg="#2c3e50")  # Set background color

        pygame.init()  # Initialize pygame
        pygame.font.init()  # Initialize font system

        self.font = pygame.font.Font(None, 20)  # Use default font
        self.playing = False
        self.music_file = None  # Initialize music_file

        # Create widgets and apply CSS styling
        self.create_widgets()
        self.style_widgets()

    def create_widgets(self):
        # Music file label
        self.file_label = tk.Label(self.master, text="No music selected", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 10))
        self.file_label.grid(row=0, column=0, columnspan=5, padx=10, pady=(20, 5), sticky="ew")

        # Select music button
        self.select_button = tk.Button(self.master, text="Select Music", command=self.select_music, bg="#3498db", fg="#ecf0f1", relief=tk.FLAT)
        self.select_button.grid(row=1, column=0, padx=10, pady=(10, 5), sticky="ew")

        # Play button
        self.play_button = tk.Button(self.master, text="▶️ Play", command=self.play_music, state=tk.DISABLED, bg="#2ecc71", fg="#ecf0f1", relief=tk.FLAT)
        self.play_button.grid(row=1, column=1, padx=10, pady=(10, 5), sticky="ew")

        # Pause button
        self.pause_button = tk.Button(self.master, text="⏸️ Pause", command=self.pause_music, state=tk.DISABLED, bg="#e74c3c", fg="#ecf0f1", relief=tk.FLAT)
        self.pause_button.grid(row=1, column=2, padx=10, pady=(10, 5), sticky="ew")

        # Stop button
        self.stop_button = tk.Button(self.master, text="⏹️ Stop", command=self.stop_music, state=tk.DISABLED, bg="#95a5a6", fg="#ecf0f1", relief=tk.FLAT)
        self.stop_button.grid(row=1, column=3, padx=10, pady=(10, 5), sticky="ew")

        # Next button
        self.next_button = tk.Button(self.master, text="➡️ Next", command=self.next_track, state=tk.DISABLED, bg="#f39c12", fg="#ecf0f1", relief=tk.FLAT)
        self.next_button.grid(row=2, column=3, padx=10, pady=(10, 5), sticky="ew")

        # Previous button
        self.prev_button = tk.Button(self.master, text="⬅️ Previous", command=self.prev_track, state=tk.DISABLED, bg="#f39c12", fg="#ecf0f1", relief=tk.FLAT)
        self.prev_button.grid(row=2, column=0, padx=10, pady=(10, 5), sticky="ew")

        # Volume label
        self.volume_label = tk.Label(self.master, text="Volume:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 10))
        self.volume_label.grid(row=3, column=0, padx=10, pady=(10, 5), sticky="w")

        # Volume control slider
        self.volume_slider = ttk.Scale(self.master, from_=0, to=100, orient="horizontal", command=self.set_volume, length=200)
        self.volume_slider.set(50)  # Set default volume to 50%
        self.volume_slider.grid(row=3, column=1, columnspan=3, padx=10, pady=(10, 5), sticky="ew")

        # Progress bar for track position
        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", length=300, mode="determinate", value=0)
        self.progress_bar.grid(row=4, column=0, columnspan=5, padx=10, pady=5)

    def style_widgets(self):
        # Apply CSS styling
        self.master.option_add("*TButton", {"font": ("Helvetica", 10), "borderwidth": 0})
        self.master.option_add("*TScale", {"troughcolor": "#34495e", "background": "#34495e", "sliderlength": 20, "sliderrelief": "flat"})
        self.master.option_add("*Horizontal.TProgressbar", {"background": "#3498db", "border": 0})

    def select_music(self):
        music_file = filedialog.askopenfilename(title="Select Music File", filetypes=[("MP3 Files", "*.mp3")])
        if music_file:
            if os.path.exists(music_file):
                self.music_file = music_file
                self.file_label.config(text=f"Selected: {os.path.basename(self.music_file)}")
                self.enable_buttons()  # Enable buttons after selection
            else:
                print("Music file not found!")

    def enable_buttons(self):
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.prev_button.config(state=tk.NORMAL)

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume) / 100)

    def load_music(self):
        if self.music_file:
            pygame.mixer.music.load(self.music_file)

    def play_music(self):
        self.load_music()
        pygame.mixer.music.play()
        self.playing = True
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)

    def pause_music(self):
        pygame.mixer.music.pause()
        self.playing = False
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

    def next_track(self):
        pass  # Add functionality to play the next track

    def prev_track(self):
        pass  # Add functionality to play the previous track

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    player = PygameMediaPlayer(root)
    root.mainloop()
