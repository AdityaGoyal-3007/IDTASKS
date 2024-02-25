import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

window = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

window.title("YouTube Video Downloader")
window.geometry("720x480")
window.minsize(720, 480)
window.maxsize(1080, 720)

def download_video():
    url = entry_url.get()
    resolution = quality_var.get()
    progress_label.pack(pady = (10, 5))
    progress_bar.pack(pady = (10, 5))
    status_label.pack(pady = (10, 5))
    try:
        yt = YouTube(url, on_progress_callback= on_progress)
        stream = yt.streams.filter(res = resolution).first()
        os.path.join("Downloads", f"{yt.title}.mp4")
        stream.download(output_path = "Downloads")
        status_label.configure(text = " Downloaded ", text_color = "white", fg_color = "green")

    except Exception as e:
        status_label.configure(text = f"Error:{str(e)}", text_color = "white", fg_color = "red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = bytes_downloaded/total_size * 100
    progress_label.configure(text = str(int(percent)) + "%")
    progress_label.update()
    progress_bar.set(float(percent/100))
        


content_frame = ctk.CTkFrame(window)
content_frame.pack(fill = ctk.BOTH, expand = True, padx = 10, pady = 10)

url_label = ctk.CTkLabel(content_frame, text = "Paste The URL Here:")
entry_url = ctk.CTkEntry(content_frame, width = 400, height =40)
url_label.pack(pady=(10, 5))
entry_url.pack(pady = (10, 5))

download_button = ctk.CTkButton(content_frame, text = "Download", command = download_video)
download_button.pack(pady=(10,5))

quality = ["1080p", "720p", "360p", "240p"]
quality_var = ctk.StringVar()
quality_box = ttk.Combobox(content_frame, values = quality, textvariable = quality_var)
quality_box.pack(pady=(10,5))
quality_box.set("1080p")

progress_label = ctk.CTkLabel(content_frame, text = "0%")

progress_bar = ctk.CTkProgressBar(content_frame, width = 400)
progress_bar.set(0)

status_label = ctk.CTkLabel(content_frame, text = "")

window.mainloop()
