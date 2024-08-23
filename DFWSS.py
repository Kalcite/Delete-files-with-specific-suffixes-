import tkinter as tk
from tkinter import messagebox, filedialog
import os
import fnmatch

def delete_files_with_extension(extension):
    # Retrieve the directory selected by the user
    directory = filedialog.askdirectory(title="Select Folder")
    
    if not directory:
        return
    
    # Normalize the extension to include dot and make it case-insensitive
    normalized_extension = f".{extension.lower().lstrip('.')}"

    deleted_files = []
    for filename in os.listdir(directory):
        if fnmatch.fnmatch(filename.lower(), f"*{normalized_extension}"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            deleted_files.append(file_path)
            
    # Determine whether to delete the file
    
    if deleted_files:
        message = "\n".join(deleted_files)
        messagebox.showinfo("Files Deleted", f"The following files have been deleted:\n{message}")
    else:
        messagebox.showinfo("No Files Found", "No files with the specified extension were found.")

def main():
    root = tk.Tk()
    root.title("File Deleter")

    label = tk.Label(root, text="Enter file extension:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    def on_button_click():
        extension = entry.get()
        delete_files_with_extension(extension)

    button = tk.Button(root, text="Delete Files", command=on_button_click)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()