import tkinter as tk 
from tkinter import filedialog
from pydub import AudioSegment


def MP3_saver():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title = "Choose MP3",
        filetypes = [("MP3 Files", "*.mp3")]
    )

    return file_path


def get_seconds(duration):
    while True:
        start = input("Start second: ")
        end = input("End second: ")

        if not start.isdigit() or not end.isdigit():
            print("Please enter numbers only")
            continue

        start = int(start)
        end = int(end)

        if start < 0:
            print("Start cannot be negative")
            continue

        if end <= start:
            print("End must be greater than Start")
            continue

        if end > duration:
            print(f"End is too large. Max duration is {duration} seconds")
            continue

        return start, end
    
def cut_audio(file_path):
    audio = AudioSegment.from_file(file_path)

    duration = len(audio) // 1000 

    start, end = get_seconds(duration)

    clip = audio[start * 1000:end * 1000]

    return clip

def save_audio(clip):
    save_path = filedialog.asksaveasfilename(
        title = "Save MP3",
        defaultextension = ".mp3",
        filetypes = [("MP3 Files", "*.mp3")]
    )

    if save_path:
        clip.export(save_path, format="mp3")


def main() -> None:
    file_path = MP3_saver()

    if file_path:
        clip = cut_audio(file_path)
        save_audio(clip)
    
 

if __name__ == "__main__":
    main()
