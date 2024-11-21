# YouTube Video Downloader

This project is a simple **YouTube Video Downloader** implemented in Python. It uses the `pytube` library for downloading videos and the `tkinter` library for providing a file dialog to select the destination folder for saving the downloaded video.

---

## Features

- **Download YouTube Videos**:
  - Downloads the highest resolution MP4 video from the given YouTube URL.
- **Graphical Folder Selection**:
  - Users can select the destination folder for saving the downloaded video using a GUI-based file dialog.
- **Error Handling**:
  - Handles errors such as invalid URLs or folder selection issues.

---

## File Structure
youtube_downloader.py: Main script for downloading YouTube videos.

---

## Usage Example

**Enter Youtube url**: https://www.youtube.com/watch?v=example

**Select Folder**: A file dialog will open. Select the folder where the video should be saved.

**Download Process**: The script downloads the highest resolution MP4 video and saves it in the selected folder.

**Success Message**:
After successful download, the script prints:
Your video has been downloaded successfully!

---

## Key Functions

**download_video(url, save_path)**:
Downloads the highest resolution MP4 video from the given YouTube URL to the specified folder.

**open_file_dialog()**:
Opens a graphical file dialog for selecting the destination folder.

--- 

## Troubleshooting

**Invalid URL**: If the URL is invalid, ensure you are copying the correct URL from YouTube.

**No Folder Selected**: Ensure you select a valid folder during the file dialog.

**SSL Errors**: The script disables SSL certification verification to handle potential issues with HTTPS contexts.

---
