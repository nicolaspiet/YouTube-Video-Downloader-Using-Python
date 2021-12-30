import ttkthemes.themed_tk
from pytube import YouTube
import tkinter
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as tkFont

# Functions


def download_text():
    download_button["text"] = "Download"


def info():
    try:
        global youtube_video
        youtube_link = video_link.get()
        youtube_video = YouTube(youtube_link)
        select_quality()
    except Exception:
        download_button["text"] = "Some error ocurred, verify the link and try again."
        main_window.after(3000, download_text)


def download():
    global youtube_path
    global downloading_label
    resolution_r.destroy()
    youtube_path = filedialog.askdirectory(title="Select a File")
    if youtube_path == '':
        pass
    else:
        download_button['text'] = "Downloading..."
        main_window.after(30, download_r)


def download_r():
    youtube_video.streams.filter(res=value_inside.get()).first().download(youtube_path)
    download_button['text'] = "Successfully downloaded!"
    main_window.after(2500, download_text)


def select_quality():
    global value_inside
    global resolution_r
    resolution_r = tkinter.Toplevel()
    resolution_r.title("Select Quality")
    resolution_r.geometry("220x130")
    resolution_r.resizable(False, False)
    resolution_r.iconbitmap("download.ico")
    video_resolutions = [stream.resolution for stream in youtube_video.streams.filter(progressive=True)]
    video_resolutions.insert(0, '')
    value_inside = tkinter.StringVar(resolution_r)
    print(video_resolutions)
    value_inside.set(video_resolutions[-1])
    question_menu = ttk.OptionMenu(resolution_r, value_inside, *video_resolutions)
    question_menu.grid(column=0, row=0, padx=65, pady=10)
    next_button = ttk.Button(resolution_r, text="Next", command=download)
    next_button.grid(column=0, row=1, padx=65, pady=10)


# Window

main_window = ttkthemes.themed_tk.ThemedTk(theme='breeze', themebg=True)
main_window.title("YouTube Video Downloader")
main_window.geometry("405x170")
main_window.resizable(False, False)
main_window.iconbitmap("download.ico")
font_style = tkFont.Font(family="Lucida Grande", size=11)

# Widgets

instruction_text = ttk.Label(main_window, text="Insert the YouTube video link down below:", font=font_style)
video_link = ttk.Entry(main_window, width=43)
download_button = ttk.Button(main_window, text="Download", command=info)

# Grids

instruction_text.grid(column=0, row=0, padx=12, pady=9)
video_link.grid(column=0, row=1, padx=47, pady=10)
download_button.grid(column=0, row=2, padx=10, pady=10)

main_window.mainloop()
