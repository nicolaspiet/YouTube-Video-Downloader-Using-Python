try:
    from checkv import *
    import ttkthemes.themed_tk
    import tkinter
    from tkinter import ttk, StringVar
    from tkinter import filedialog
    import tkinter.font as tkFont
    from pytube import YouTube
    import os

    global youtube_path
    global downloading_label
    global value_inside
    global value_inside2
    global resolution_r
    global youtube_video

    def set_download_text():
        download_button["text"] = "Download"

    def get_video():
        global youtube_video
        try:
            youtube_link = video_link.get()
            youtube_video = YouTube(youtube_link)
            select_quality()
        except Exception as error:
            download_button["text"] = "An error occurred, verify the link and try again."
            print(error)
            main_window.after(3000, set_download_text)

    def select_quality():
        global resolution_r
        global value_inside
        global value_inside2
        # Window
        resolution_r = tkinter.Toplevel()
        resolution_r.title("Download Settings")
        resolution_r.geometry("270x130")
        resolution_r.resizable(False, False)
        resolution_r.iconbitmap("download.ico")
        # Getting available resolutions for the video
        video_formats = ["MP4", "MP4", "MP3"]
        video_resolutions = [stream.resolution for stream in youtube_video.streams.filter(progressive=True)]
        video_resolutions.insert(0, '')
        value_inside = tkinter.StringVar(resolution_r)
        value_inside2 = tkinter.StringVar(resolution_r)
        value_inside.set(video_resolutions[-1])
        value_inside2.set(video_formats[1])
        question_menu = ttk.OptionMenu(resolution_r, value_inside, *video_resolutions)
        question_menu.grid(column=0, row=0, padx=(65, 3), pady=15)
        format_menu = ttk.OptionMenu(resolution_r, value_inside2, *video_formats)
        format_menu.grid(column=1, row=0)
        next_button = ttk.Button(resolution_r, text="Next", command=select_path)
        next_button.place(x=88, y=65)

    def select_path():
        global youtube_path
        resolution_r.destroy()
        youtube_path = filedialog.askdirectory(title="Select a Directory")
        if youtube_path == '':
            pass
        else:
            download_button['text'] = "Downloading..."
            if value_inside2.get() == "MP4":
                main_window.after(30, download_mp4)
            else:
                main_window.after(30, download_mp3)

    def download_mp3():
        final_video = youtube_video.streams.filter(only_audio=True).first()
        out_file = final_video.download(youtube_path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        download_button['text'] = "Successfully downloaded!"
        main_window.after(2500, set_download_text)

    def download_mp4():
        youtube_video.streams.filter(res=value_inside.get()).first().download(youtube_path)
        download_button['text'] = "Successfully downloaded!"
        main_window.after(2500, set_download_text)

    def grid_widgets():
        instruction_text.grid(column=0, row=0, padx=12, pady=9)
        video_link.grid(column=0, row=1, padx=47, pady=10)
        download_button.grid(column=0, row=2, padx=10, pady=10)

    # Window
    main_window = ttkthemes.themed_tk.ThemedTk(theme='breeze', themebg=True, toplevel=True)

    main_window.title("YouTube Video Downloader")
    main_window.geometry("405x170")
    main_window.resizable(False, False)
    main_window.iconbitmap("download.ico")
    font_style = tkFont.Font(family="Lucid Grande", size=12)

    # Widgets
    instruction_text = ttk.Label(main_window, text="Insert the YouTube video link below:", font=font_style)
    video_link = ttk.Entry(main_window, width=43)
    download_button = ttk.Button(main_window, text="Download", command=get_video)
    grid_widgets()
    # Centering the screen
    main_window.eval(f'tk::PlaceWindow . center')
    # Checking if user has outdated packages
    check_version()

    main_window.mainloop()

except ModuleNotFoundError:
    print("Unable to find one or more of the required packages, please install or update them.\nPackages:\n\n- pytube\n"
          "- ttkthemes\n")
    input("Press ENTER to exit the application.")
except Exception as err:
    print("An error has occurred, please restart the program and try again."
          f"\nError: {err}")
