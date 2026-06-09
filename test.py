import tkinter as tk 
from tkinter import filedialog
from pydub import AudioSegment

def cut(audio):
    audio = AudioSegment.from_file(audio)
    start = int(input("Start second: "))
    end = int(input("End second: "))
    clip = audio[start * 1000:end * 1000]
    clip.export("output.mp3", format="mp3")
    clip = cut(file_path)

    save_path = filedialog.asksaveasfilename(
    title="Save MP3",
    defaultextension=".mp3",
    filetypes=[("MP3 Files", "*.mp3")])

    clip.export(save_path, format="mp3")


def main() -> None:
    root = tk.Tk()
    root = root.withdraw()
    file_path = filedialog.askopenfilename(
        title="choose MP3",
        filetypes=[("MP3 Files", "*.mp3")]
    )
    file_path = cut(file_path)
 

if __name__ == "__main__":
    main()