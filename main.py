#!/bin/python3

# Importing Libraries
import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import font
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import time

from playsound import playsound

background_path = r'assets/spaceship_art_fiction.jpg'
bg_music_path = r'assets/spiderman-meme-song.mp3'

class Pomodoro:
    def __init__(self, root):
        self.timer = 0
        self.root = root


    def work_break(self, timer):
        minutes, seconds = divmod(timer, 60)
        self.min.set(f"{minutes:02d}")
        self.sec.set(f"{seconds:02d}")
        self.root.update()
        time.sleep(1)
        
    def work(self):
        self.timer = 50*60
        while self.timer >= 0:
            pomo.work_break(self.timer)
            if self.timer == 0:
                playsound(bg_music_path)
                tmsg.showinfo("Break Time", "Take A Break, \n Click Break Button")
            self.timer -= 1

    def break_(self):
        self.timer = 10*60
        while self.timer >= 0:
            pomo.work_break(self.timer)
            if self.timer == 0:
                playsound(background_path)
                tmsg.showinfo("Time to work!", "Get Back to Work\n Click Work Button")
            self.timer -= 1

    def close(self):
        self.timer = -1
        self.root.destroy()

    def main(self):
        # GUI window configuration
        self.root.geometry("450x450")
        self.root.resizable(False, False)
        self.root.title("Pomodoro Timer")

        # Labels
        self.min = tk.StringVar(self.root)
        self.min.set("50")
        self.sec = tk.StringVar(self.root)
        self.sec.set("00")

        self.min_label = tk.Label(self.root, textvariable=self.min, font=("Cascadia Code", 22, "bold"), bg="red", fg='black')
        self.min_label.pack()

        self.sec_label = tk.Label(self.root, textvariable=self.sec, font=("JetBrains Mono", 22, "bold"), bg="black", fg='white')
        self.sec_label.pack()

        # add background image for GUI using Canvas widget
        canvas = tk.Canvas(self.root)
        canvas.pack(expand=True, fill="both")
        img = Image.open(background_path)
        bg = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, image=bg, anchor="nw")

        # create three buttons with countdown function command
        btn_work = tk.Button(self.root, text="Start", bd=5, command=self.work,
                             bg="red", font=("JetBrains Mono", 15, "bold")).place(x=140, y=380)
        btn_break = tk.Button(self.root, text="Break", bd=5, command=self.break_,
                              bg="red", font=("JetBrains Mono", 15, "bold")).place(x=240, y=380)

        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.root.mainloop()


if __name__ == '__main__':
    pomo = Pomodoro(tk.Tk())
    pomo.main()
