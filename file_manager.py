import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = input("Enter path: ")
while not os.path.isdir(path):
    print(f"Error: '{path}' is not a valid directory.")
    path = input("Enter path: ")


"""Sort existing files to respective directories"""
files = os.scandir(path)
for file in files:
    if file.is_file():
        name, extension = os.path.splitext(file.name)

        target_dir = os.path.join(path, extension[1:])  # Removing the dot from the extension
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Check if the file exists in the target directory
        file_destination = os.path.join(target_dir, file.name)
        if os.path.exists(file_destination):
            # Rename the file to avoid conflicts
            base_name = os.path.basename(name)
            counter = 1
            while os.path.exists(os.path.join(target_dir, f"{base_name}_{counter}{extension}")):
                counter += 1
            new_file_name = f"{base_name}_{counter}{extension}"
            shutil.move(file.path, os.path.join(target_dir, new_file_name))
        else:
            shutil.move(file.path, file_destination)

"""Watch for files to be added and sort it immediately"""
class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:  # Check if the created item is a directory
            return
        
        created_file_path = event.src_path
        name, extension = os.path.splitext(os.path.basename(created_file_path))

        # Target directory based on extension
        target_dir = os.path.join(os.path.dirname(created_file_path), extension[1:])
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Move the file to the target directory with retries in case of PermissionError
        retries = 3
        while retries > 0:
            try:
                file_destination = os.path.join(target_dir, os.path.basename(created_file_path))
                if os.path.exists(file_destination):
                    # Rename the file to avoid conflicts
                    base_name = os.path.splitext(name)[0]
                    counter = 1
                    while os.path.exists(os.path.join(target_dir, f"{base_name}_{counter}{extension}")):
                        counter += 1
                    new_file_name = f"{base_name}_{counter}{extension}"
                    shutil.move(created_file_path, os.path.join(target_dir, new_file_name))
                else:
                    shutil.move(created_file_path, file_destination)
                print(f"Moved {os.path.basename(created_file_path)} to: {"\\".join(file_destination.split("\\")[:-1])}")
                break
            except PermissionError:
                retries -= 1
                time.sleep(1)  # Wait for a short duration before retrying

def watch_directory(path):
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    directory_to_watch = path
    watch_directory(directory_to_watch)
