# Python File Organizer

A simple Python automation script that organizes files in any folder by their type automatically sorting images, PDFs, videos, documents, and audio files into separate sub-folders.

## What it does

Instead of manually sorting hundreds of files by hand, this script scans a folder and moves each file into a category folder based on its extension:

- **Images**  .jpg, .jpeg, .png
- **PDFs**  .pdf
- **Videos**  .mp4, .mov
- **Documents**  .txt, .docx
- **Audio**  .mp3, .wav
- **Archives**  .zip, .rar
- **Others**  anything not listed above

## How to use

1. Run the script: `python organizer.py`
2. Enter the full path of the folder you want to organize when prompted
3. The script creates category folders and moves each file automatically
4. A summary shows how many files were organized

## Why this matters

This is a small example of the kind of automation Nexoratec builds for clients removing repetitive manual work with a simple, reliable script. The same approach applies to renaming files in bulk, sorting downloads, organizing client deliverables, or any repetitive file-management task.

## Tech used

Python (os, shutil modules) no external dependencies required.
