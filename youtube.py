import ssl
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

# Disable SSL certification verification
ssl._create_default_https_context = ssl._create_unverified_context


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams=yt.streams.filter(progressive=True, file_extension="mp4 ")
        highest_resolution_stream = streams.get_highest_resolution()
        highest_resolution_stream.download(output_path=save_path)
        print("Your video has been downloaded successfully!")

    except Exception as e:
        print(e)

def open_file_dialog():
     folder = filedialog.askdirectory()
     if folder:
         print(f"Selected Folder: {folder}")

     return folder

if __name__ == "__main__":
    root = tk.Tk( )
    root.withdraw 

    video_url = input("Enter Youtube url:  ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Downloading...")
        download_video(video_url,save_dir)
             
    else:
       print("Invalid folder....") 
