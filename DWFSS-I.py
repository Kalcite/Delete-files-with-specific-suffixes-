import tkinter as tk
from tkinter import messagebox, filedialog
import os
import shutil
import fnmatch

def move_files_to_temp(extension, temp_dir):
    directory = filedialog.askdirectory(title="Select Folder")
    if not directory:
        return

    # Create temporary directory if it doesn't exist
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Normalize the extension to include dot and make it case-insensitive
    normalized_extension = f".{extension.lower().lstrip('.')}"

    moved_files = []
    for filename in os.listdir(directory):
        if fnmatch.fnmatch(filename.lower(), f"*{normalized_extension}"):
            file_path = os.path.join(directory, filename)
            temp_file_path = os.path.join(temp_dir, filename)
            shutil.move(file_path, temp_file_path)
            moved_files.append(file_path)

    if moved_files:
        message = "\n".join(moved_files)
        messagebox.showinfo("Files Moved", f"The following files have been moved to {temp_dir}:\n{message}")
    else:
        messagebox.showinfo("No Files Found", "No files with the specified extension were found.")

def restore_files_from_temp(temp_dir):
    if not os.path.exists(temp_dir):
        messagebox.showwarning("Warning", "No temporary folder found.")
        return

    restored_files = []
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        original_file_path = os.path.join(original_directory, filename)
        shutil.move(file_path, original_file_path)
        restored_files.append(file_path)

    if restored_files:
        message = "\n".join(restored_files)
        messagebox.showinfo("Files Restored", f"The following files have been restored:\n{message}")
    else:
        messagebox.showinfo("No Files Found", "No files to restore.")

def delete_files_from_temp(temp_dir):
    if not os.path.exists(temp_dir):
        messagebox.showwarning("Warning", "No temporary folder found.")
        return

    deleted_files = []
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        os.remove(file_path)
        deleted_files.append(file_path)

    if deleted_files:
        message = "\n".join(deleted_files)
        messagebox.showinfo("Files Deleted", f"The following files have been permanently deleted:\n{message}")
    else:
        messagebox.showinfo("No Files Found", "No files to delete.")

def main():
    root = tk.Tk()
    root.title("File Deleter")

    label = tk.Label(root, text="Enter file extension:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    def on_button_click():
        extension = entry.get()
        temp_dir = os.path.join(original_directory, ".temp")
        move_files_to_temp(extension, temp_dir)

    def on_confirm_delete():
        temp_dir = os.path.join(original_directory, ".temp")
        delete_files_from_temp(temp_dir)

    def on_restore_files():
        temp_dir = os.path.join(original_directory, ".temp")
        restore_files_from_temp(temp_dir)

    button_move = tk.Button(root, text="Move Files to .temp", command=on_button_click)
    button_move.pack()

    button_delete = tk.Button(root, text="Confirm Delete", command=on_confirm_delete)
    button_delete.pack()

    button_restore = tk.Button(root, text="Restore Files", command=on_restore_files)
    button_restore.pack()

    # Request the user to select the original folder
    def select_original_directory():
        global original_directory
        original_directory = filedialog.askdirectory(title="Select Original Folder")
        if not original_directory:
            messagebox.showwarning("Warning", "Please select an original folder first.")

    button_select_dir = tk.Button(root, text="Select Original Directory", command=select_original_directory)
    button_select_dir.pack()

    root.mainloop()

if __name__ == "__main__":
    main()