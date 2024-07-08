import tkinter as tk
from tkinter import filedialog
import pygame
import os


def load_music():
    folder_path = tk.filedialog.askdirectory()

    if folder_path:
        playlist.delete(0, tk.END)
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(".mp3"):
                    playlist.insert(tk.END, os.path.join(root, file))
    else:
        print("No folder selected.")

def play_music():
    selected_song = playlist.get(tk.ACTIVE)
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

# Initialize pygame
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.title("Music Player")
root.geometry('1500x800')

# Styling and layout improvements
root.configure(bg="turquoise")  # Set background color
canvas = tk.Canvas(root, width=1500, height=70, bg="teal")
canvas.create_text(750, 30, text=" LET'S PLAY MUSIC WITH US.. ", fill="goldenrod", font='Algerian 28 bold')
canvas.pack()


# Create buttons with icons
load_icon = tk.PhotoImage(file="C:/Users/Rishika/PycharmProjects/Rishika_Music_Player/images/load_icon (2).png")  # Replace with your icon file
play_icon = tk.PhotoImage(file="C:/Users/Rishika/PycharmProjects/Rishika_Music_Player/images/play_icon (2).png")
pause_icon = tk.PhotoImage(file="C:/Users/Rishika/PycharmProjects/Rishika_Music_Player/images/pause_icon (2).png")
stop_icon = tk.PhotoImage(file="C:/Users/Rishika/PycharmProjects/Rishika_Music_Player/images/stop_icon (2).png")

load_button = tk.Button(root, height=200, width=200, image=load_icon, command=load_music, bg="turquoise", borderwidth=0)
play_button = tk.Button(root, height=200, width=200, image=play_icon, command=play_music, bg="turquoise", borderwidth=0)
pause_button = tk.Button(root, height=200, width=200, image=pause_icon, command=pause_music, bg="turquoise", borderwidth=0)
stop_button = tk.Button(root, height=200, width=200, image=stop_icon, command=stop_music, bg="turquoise", borderwidth=0)

# Create playlist
playlist = tk.Listbox(root, height=20, width=220, bg="white", selectbackground="lightblue")
playlist.pack()
playlist.place(x=80, y=80)

# Layout buttons
load_button.place(x=100, y=450)
play_button.place(x=470, y=450)
pause_button.place(x=850, y=450)
stop_button.place(x=1200, y=450)


root.mainloop()
