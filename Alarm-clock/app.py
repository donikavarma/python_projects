import tkinter as tk
from tkinter import ttk
import datetime
import time
import pygame
import threading

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

def play_alarm():
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()

def check_alarm():
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time.get():
            # Schedule GUI + sound on main thread
            root.after(0, trigger_alarm)
            break
        time.sleep(1)

def trigger_alarm():
    show_alarm_popup()
    play_alarm()

def set_alarm():
    alarm_label.config(text=f"Alarm Set For: {alarm_time.get()}")
    threading.Thread(target=check_alarm, daemon=True).start()

def show_alarm_popup():
    popup = tk.Toplevel(root)
    popup.title("Alarm")
    popup.geometry("300x150")
    popup.configure(bg="#1e1e1e")

    msg = tk.Label(
        popup,
        text="⏰ Wake Up!",
        font=("Segoe UI", 20, "bold"),
        fg="white",
        bg="#1e1e1e"
    )
    msg.pack(pady=20)

    btn = ttk.Button(
        popup,
        text="Stop Alarm",
        command=lambda: (pygame.mixer.music.stop(), popup.destroy())
    )
    btn.pack()

def update_clock():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

# Main window
root = tk.Tk()
root.title("Modern Alarm Clock")
root.geometry("400x350")
root.configure(bg="#121212")

clock_label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 40, "bold"),
    fg="#00eaff",
    bg="#121212"
)
clock_label.pack(pady=20)

alarm_time = tk.StringVar()

time_entry = ttk.Entry(root, textvariable=alarm_time, font=("Segoe UI", 14))
time_entry.pack(pady=10)
time_entry.insert(0, "")

set_btn = ttk.Button(root, text="Set Alarm", command=set_alarm)
set_btn.pack(pady=10)

alarm_label = tk.Label(
    root,
    text="No Alarm Set",
    font=("Segoe UI", 12),
    fg="white",
    bg="#121212"
)
alarm_label.pack(pady=10)

update_clock()
root.mainloop()
