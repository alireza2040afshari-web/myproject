import tkinter as tk 
from tkinter import filedialog


def main() -> None:
    root = tk.Tk()
    root = root.withdraw()
    file_path = filedialog.askopenfilename(
        title="choose MP3",
        filetypes=[("MP3 Files", "*.mp3")]
    )
 

if __name__ == "__main__":
    main()